from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

yes_button = KeyboardButton(LEXICON_RU['yes'])
no_button = KeyboardButton(LEXICON_RU['no'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(yes_button,
                   no_button,
                   width=2)

yes_no_kb:ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(resize_keyboard=True,
                                     one_time_keyboard=True)

stone_button = KeyboardButton(LEXICON_RU['stone'])
scissors_button = KeyboardButton(LEXICON_RU['scissors'])
paper_button = KeyboardButton(LEXICON_RU['paper'])

game_kb_builder = ReplyKeyboardBuilder()

game_kb_builder.row(stone_button, scissors_button, paper_button, width=2)

game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(resize_keyboard=True)