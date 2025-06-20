import asyncio
from aiogram import Bot, Dispatcher
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Handlerlarni ulash
from handlers import start, text_ai, image_ai, voice_ai, subscription_check, commands

dp.include_router(start.router)
dp.include_router(text_ai.router)
dp.include_router(image_ai.router)
dp.include_router(voice_ai.router)
dp.include_router(subscription_check.router)
dp.include_router(commands.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
