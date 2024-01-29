from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


other_router = Router()


@other_router.message()
async def other_process(message:Message):
    await message.answer(LEXICON_RU['wrong_answer'])