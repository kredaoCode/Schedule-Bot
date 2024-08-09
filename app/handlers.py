from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.myrequests import get_images

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    
@router.message(Command('load'))
async def cmd_load(message: Message):
    image_urls = get_images(0)
    for url in image_urls:
        await message.answer_photo(photo=url)