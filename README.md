# REST API for Equation Evaluation

This project provides a simple REST API that retrieves input variables from a Google Sheet, evaluates stored mathematical equations, and exports the results to a SQL database such as Snowflake.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with the required credentials for Google Sheets and your SQL database. Example variables:
   - `GOOGLE_SHEET_KEY`
   - `GOOGLE_SERVICE_ACCOUNT_FILE`
   - `DATABASE_URL` (SQLAlchemy connection string)

3. Run the API:
   ```bash
   python -m app.main
   ```

## Endpoints

- `POST /equations` – Add a new equation.
- `GET /equations` – List stored equations.
- `POST /run` – Retrieve variables from the Google Sheet, evaluate equations, and export results to the database.

Stored equations are simple Python expressions that operate on variables from the Google Sheet. For example:

```json
{"name": "total", "expression": "a + b * c"}
```

## Notes

- Use the Google Sheet's first row as variable names.
- Supported databases depend on the SQLAlchemy driver specified in `DATABASE_URL`.
- Snowflake is recommended for production, but any SQLAlchemy-compatible database can be used for testing.
