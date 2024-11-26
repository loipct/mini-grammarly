from fastapi import APIRouter
from app.models.schemas import TextInput, CorrectionResponse
from app.services.grammar_checker import check_and_correct_text

router = APIRouter()

@router.post("/check_and_correct", response_model=list[CorrectionResponse])
async def check_and_correct(input: TextInput):
    """
    Endpoint để kiểm tra và sửa lỗi ngữ pháp và chính tả.
    """
    return check_and_correct_text(input.text)
