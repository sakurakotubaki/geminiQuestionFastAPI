from fastapi import APIRouter, HTTPException
from app.domain.schemas import QuestionRequest, QuestionResponse
from app.usecase.question_service import QuestionService

router = APIRouter()
question_service = QuestionService()

@router.post("/question", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    try:
        response = await question_service.ask_question(request.prompt)
        return QuestionResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
