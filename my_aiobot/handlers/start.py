from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("BARAKA BOT AI ga hush kelib siz")
