from aiogram import Router, types
from config import CHANNEL_USERNAME

router = Router()

@router.message()
async def check_subscription(message: types.Message, bot):
    user_id = message.from_user.id
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["left", "kicked"]:
            await message.answer("Kanalga obuna bo‘lishingiz kerak!")
    except:
        pass
