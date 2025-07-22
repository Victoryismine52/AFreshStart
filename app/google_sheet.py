import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

SHEET_KEY = os.getenv("GOOGLE_SHEET_KEY")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")


def get_sheet_data() -> pd.DataFrame:
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, SCOPES
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_KEY).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)
