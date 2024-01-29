from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboard import yes_no_kb, game_kb
from lexicon.lexicon import LEXICON_RU

user_router = Router()

# Хэндлер который отрабатывает команду /start
@user_router.message(CommandStart())
async def start_process(message:Message):
    await message.answer(LEXICON_RU['start'], reply_markup=yes_no_kb)

# Хэндлер который отрабатывает команду /help
@user_router.message(Command(commands='help'))
async def start_process(message:Message):
    await message.answer(LEXICON_RU['help'], reply_markup=yes_no_kb)

@user_router.message(lambda msg: msg == LEXICON_RU['yes'])
async def process_yes(message:Message):
    await message.answer(LEXICON_RU['user_yes'], reply_markup=game_kb)

@user_router.message(lambda msg: msg == LEXICON_RU['no'])
async def process_no(message:Message):
    await message.answer(LEXICON_RU['user_no'])