from fastapi import FastAPI, HTTPException
from openai import OpenAIError
from pydantic import BaseModel

from ai.openai_engine import AIEngine

app = FastAPI()
ai = AIEngine()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "G-ONE AI Backend Running"}


@app.post("/chat")
def chat(request: PromptRequest):
    try:
        response = ai.ask(request.prompt)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except OpenAIError as exc:
        raise HTTPException(status_code=502, detail="OpenAI request failed") from exc

    return {"response": response}
