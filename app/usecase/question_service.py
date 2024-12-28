from app.infrastructure.gemini_client import GeminiClient

class QuestionService:
    def __init__(self):
        self.gemini_client = GeminiClient()

    async def ask_question(self, prompt: str) -> str:
        return await self.gemini_client.get_response(prompt)
