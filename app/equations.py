from typing import List
from sqlalchemy.orm import Session

from .database import Equations


def add_equation(session: Session, name: str, expression: str) -> int:
    ins = Equations.insert().values(name=name, expression=expression)
    result = session.execute(ins)
    session.commit()
    return result.inserted_primary_key[0]


def list_equations(session: Session) -> List[dict]:
    sel = Equations.select()
    rows = session.execute(sel).fetchall()
    return [{"id": r.id, "name": r.name, "expression": r.expression} for r in rows]
