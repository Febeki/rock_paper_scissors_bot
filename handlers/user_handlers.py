from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU["yes_button"]))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["yes"], reply_markup=game_kb)


@router.message(Text(text=LEXICON_RU["no_button"]))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(Text(text=[LEXICON_RU["scissors"],
                           LEXICON_RU["paper"],
                           LEXICON_RU["rock"]]))
async def process_start_command(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} "
                              f" - {LEXICON_RU[bot_choice]}")
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
