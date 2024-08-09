import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from app.tokens import tg_token
from app.handlers import router



async def main():
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())