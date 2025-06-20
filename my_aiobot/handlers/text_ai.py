from aiogram import Router, types
from utils.openai_utils import generate_text

router = Router()

@router.message()
async def text_ai_handler(message: types.Message):
    if message.text:
        response = await generate_text(message.text)
        await message.answer(response)
