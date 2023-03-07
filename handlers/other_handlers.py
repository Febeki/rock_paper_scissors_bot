from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import yes_no_kb

router: Router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU["other_answer"], reply_markup=yes_no_kb)