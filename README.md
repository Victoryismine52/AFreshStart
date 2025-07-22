# afreshstart API

This project provides a FastAPI service that exposes a simple REST endpoint to fetch data from a Google Sheet. It can be used as a middle layer between Google Sheets and a frontend application.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** in the project root with the following variables:
   ```bash
   GOOGLE_SERVICE_ACCOUNT_FILE=/path/to/credentials.json
   GOOGLE_SHEET_ID=your_google_sheet_id
   ```
   The service account JSON file is obtained from the Google Cloud Console (see below).

3. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- `GET /data?range=Sheet1!A1:C10` – Retrieves the specified range of values from the configured Google Sheet.

## Generating Google API Credentials

1. Go to <https://console.cloud.google.com/> and create a new project (or select an existing one).
2. Enable the **Google Sheets API** for the project.
3. Navigate to **APIs & Services → Credentials** and create a **Service Account**.
4. Generate a JSON key for the service account and download the file. Save the path to this file in `GOOGLE_SERVICE_ACCOUNT_FILE` in your `.env`.
5. Share your Google Sheet with the service account's email address so it has read access.
6. Copy the sheet ID from the sheet URL (the part between `/d/` and `/edit`) and set it as `GOOGLE_SHEET_ID` in the `.env` file.

## Notes

- CORS is enabled for all origins by default so the API can be called from any frontend during development.
- Only read access is required for the service account. No user data is stored by this service.
