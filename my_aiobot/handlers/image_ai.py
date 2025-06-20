from aiogram import Router, types
from aiogram.filters import Command
from utils.replicate_utils import generate_image

router = Router()

@router.message(Command("draw"))
async def draw_image(message: types.Message):
    prompt = message.text.replace("/draw ", "")
    img_url = await generate_image(prompt)
    await message.answer(img_url)
