from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboard import yes_no_kb, game_kb
from lexicon.lexicon import LEXICON_RU
from services.service import get_bot_choice, logic_game

user_router = Router()

# Хэндлер который отрабатывает команду /start
@user_router.message(CommandStart())
async def start_process(message:Message):
    await message.answer(LEXICON_RU['start'], reply_markup=yes_no_kb)

# Хэндлер который отрабатывает команду /help
@user_router.message(Command(commands='help'))
async def help_process(message:Message):
    await message.answer(LEXICON_RU['help'], reply_markup=yes_no_kb)

# Хэндлер который обрабатывает нажание кнопки Давай
@user_router.message(F.text == LEXICON_RU['yes'])
async def process_yes(message:Message):
    await message.answer(LEXICON_RU['user_yes'], reply_markup=game_kb)

# Хэндлер который обрабатывает нажание кнопки Не буду
@user_router.message(F.text == LEXICON_RU['no'])
async def process_no(message:Message):
    await message.answer(LEXICON_RU['user_no'])

# Хэндлер которы обрабатывает выбор пользователя
@user_router.message(F.text.in_((LEXICON_RU['stone'],
                                LEXICON_RU['scissors'],
                                LEXICON_RU['paper'])))
async def process_game(message:Message):
    bot_choice = get_bot_choice()
    await message.answer(f"{LEXICON_RU['bot_choice']} -  {LEXICON_RU[bot_choice]}")
    winner = logic_game(message.text, bot_choice)
    await message.answer(LEXICON_RU[winner], reply_markup=yes_no_kb)