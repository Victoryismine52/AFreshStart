from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..services.google_sheets import GoogleSheetsService
from ..models.sheet import SheetValues

router = APIRouter(prefix="/data", tags=["data"])


def get_service():
    return GoogleSheetsService()


@router.get("/", response_model=SheetValues)
def read_data(range: str, service: GoogleSheetsService = Depends(get_service)):
    try:
        values = service.get_values(range)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return SheetValues(range=range, values=values)
