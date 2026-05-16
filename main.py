import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from database import init_db, create_user

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💳 To'lov tasdiqlash")],
        [KeyboardButton(text="👤 Men haqimda"), KeyboardButton(text="📜 To'lovlar tarixi")],
        [KeyboardButton(text="⚙️ Sozlamalar"), KeyboardButton(text="ℹ️ Bot haqida")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await create_user(message.from_user.id, message.from_user.full_name)
    await message.answer(
        "Assalomu alaykum! Payment Verification Botga xush kelibsiz.",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "💳 To'lov tasdiqlash")
async def payment_handler(message: Message):
    await message.answer("Iltimos buyurtma ID raqamini yuboring.")

@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("Screenshot qabul qilindi va tekshirilmoqda.")

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())