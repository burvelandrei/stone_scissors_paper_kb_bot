from lexicon.lexicon import LEXICON_RU
from random import choice

def get_bot_choice() -> str:
    return choice['stone', 'scissors', 'paper']


def _normalize_user_choice(user_choice: str) -> str:
    for key in LEXICON_RU.keys():
        if LEXICON_RU[key] == user_choice:
            return key

def logic_game(user_choice: str) -> str:
    bot_choice = get_bot_choice()
    win = {'stone': 'scissors',
           'scissors':'paper',
           'paper': 'stone'}
    if win[user_choice] == bot_choice:
        return LEXICON_RU['user_won']
    if user_choice == bot_choice:
        return LEXICON_RU['draw']
    return LEXICON_RU['bot_won']