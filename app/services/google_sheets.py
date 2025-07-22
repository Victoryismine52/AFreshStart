import os
from typing import List
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


class GoogleSheetsService:
    def __init__(self):
        service_account = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
        if not service_account:
            raise ValueError("GOOGLE_SERVICE_ACCOUNT_FILE not set in .env")

        credentials = Credentials.from_service_account_file(service_account, scopes=SCOPES)
        self.service = build("sheets", "v4", credentials=credentials)
        self.sheet_id = os.getenv("GOOGLE_SHEET_ID")
        if not self.sheet_id:
            raise ValueError("GOOGLE_SHEET_ID not set in .env")

    def get_values(self, range_name: str) -> List[List[str]]:
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.sheet_id, range=range_name).execute()
        return result.get("values", [])
