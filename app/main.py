import json
from flask import Flask, request, jsonify
from sqlalchemy.orm import Session

from .database import init_db, Session as DBSession, Results
from .google_sheet import get_sheet_data
from .equations import add_equation, list_equations

app = Flask(__name__)
init_db()


@app.route("/equations", methods=["POST"])
def create_equation():
    data = request.get_json()
    name = data.get("name")
    expression = data.get("expression")
    if not name or not expression:
        return jsonify({"error": "name and expression required"}), 400
    with DBSession() as session:
        eq_id = add_equation(session, name, expression)
    return jsonify({"id": eq_id, "name": name, "expression": expression})


@app.route("/equations", methods=["GET"])
def get_equations():
    with DBSession() as session:
        equations = list_equations(session)
    return jsonify(equations)


@app.route("/run", methods=["POST"])
def run_equations():
    df = get_sheet_data()
    variables = df.iloc[0].to_dict()
    with DBSession() as session:
        eqs = list_equations(session)
        results = []
        for eq in eqs:
            try:
                result_value = eval(eq["expression"], {}, variables)
            except Exception as exc:
                result_value = str(exc)
            ins = Results.insert().values(equation=eq["name"], result=str(result_value))
            session.execute(ins)
            results.append({"equation": eq["name"], "result": result_value})
        session.commit()
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
