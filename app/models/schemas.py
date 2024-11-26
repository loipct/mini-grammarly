from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class CorrectionDetail(BaseModel):
    error_text: str
    message: str
    suggestions: List[str]
    offset: int
    length: int

class CorrectionResponse(BaseModel):
    original: str
    corrected: str
    corrections: List[CorrectionDetail]
