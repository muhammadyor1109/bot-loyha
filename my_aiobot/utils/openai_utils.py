import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
