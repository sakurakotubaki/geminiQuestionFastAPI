from pydantic import BaseModel

class QuestionRequest(BaseModel):
    prompt: str

class QuestionResponse(BaseModel):
    response: str
