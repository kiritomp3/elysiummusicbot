from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ContentType
from core.handler.basic import get_start, get_photo, skin_oblogu, skin_waw
from core.settings import settings
from aiogram.filters import Command
from aiogram import F

import asyncio
import logging


async def start_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')



async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(skin_oblogu, F.content_type == ContentType.TEXT)
    dp.message.register(skin_waw, F.content_type == ContentType.AUDIO)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())