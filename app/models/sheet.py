from pydantic import BaseModel
from typing import List


class SheetValues(BaseModel):
    range: str
    values: List[List[str]]
