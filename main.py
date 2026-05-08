import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8791449240:AAHqnmDyaPv3Z_gUKw_TnPOzAokr1C_S8OE"

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("✨ Вивьен наблюдает за вами...")

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())