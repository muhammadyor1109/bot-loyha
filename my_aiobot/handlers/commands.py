from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("reset"))
async def reset_cmd(message: types.Message):
    await message.answer("Session tozalandi.")

@router.message(Command("language"))
async def language_cmd(message: types.Message):
    await message.answer("Tilni tanlang: 🇺🇿 🇷🇺 🇬🇧")
