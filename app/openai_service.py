import os
from openai import OpenAI

# Considers async route:
# https://github.com/openai/openai-python?tab=readme-ov-file#async-usage

class OpenAiService():
    def __init__(self, model: str) -> None:
        self._model = model
        self._client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))

    def chat(self, prompt: str) -> str:
        try:
            result = self._client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt  # 'content' should be a string here
                    }
                ],
                model=self._model
            )

            if result and result.choices and result.choices[0].message:
                chat_result = result.choices[0].message
                return chat_result.content if chat_result.content is not None else ""

            print("OPENAI not response found")
            return ""

        except Exception as e:
            # Handle any potential exceptions (network errors, etc.)
            print(f"Error: {e}")
            return ""
