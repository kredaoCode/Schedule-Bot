import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from tokens import tg_token

bot = Bot(token=tg_token)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())