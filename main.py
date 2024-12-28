from fastapi import FastAPI
from app.presentation.api import router

app = FastAPI(title="Gemini Question API")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
