import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
from aiogram.router import Router
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Инициализация
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)

# Клавиатура
goals_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔥 Набор массы")],
        [KeyboardButton(text="💪 Сушка")],
        [KeyboardButton(text="🧘‍♀️ Здоровье")]
    ],
    resize_keyboard=True
)

# Обработка /start
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! 👋 Давай подберём тебе спортивное питание. Какая у тебя цель?",
        reply_markup=goals_kb
    )

# Обработка выбора цели
@router.message(F.text.in_({"🔥 Набор массы", "💪 Сушка", "🧘‍♀️ Здоровье"}))
async def handle_goal(message: types.Message):
    await message.answer(f"Отлично! Ты выбрал цель: *{message.text}*. Скоро мы предложим тебе подходящий бокс 💼",
                         parse_mode="Markdown")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())