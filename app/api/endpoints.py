from fastapi import APIRouter
from app.models.schemas import TextInput, CorrectionResponse
from app.services.grammar_checker import check_and_correct_text
from app.services.essay_grader import grade_essay as grade_essay_from_service  # Renamed import to avoid conflict

router = APIRouter()

@router.post("/check_and_correct", response_model=list[CorrectionResponse])
async def check_and_correct(input: TextInput):
    """
    Endpoint để kiểm tra và sửa lỗi ngữ pháp và chính tả.
    """
    return check_and_correct_text(input.text)

@router.post("/grade")
async def grade_essay(essay_text: str, task_type: int):
    """
    Endpoint để chấm điểm bài luận.
    """
    return grade_essay_from_service(essay_text, task_type)  # Call the renamed function
