from openai import OpenAI
from core.config import OPENAI_API_KEY, OPENAI_MODEL
from ai.personality import SYSTEM_PROMPT


class AIEngine:
    def __init__(self, api_key=OPENAI_API_KEY, model=OPENAI_MODEL):
        self.model = model
        self.client = OpenAI(api_key=api_key) if api_key else None

    def ask(self, prompt, history=None):
        if not self.client:
            raise RuntimeError(
                "OPENAI_API_KEY is not configured. Add it to the .env file."
            )

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if history:
            messages.extend(history)

        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content
