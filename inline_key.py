from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import dict_game

info='hello'

async def card_1():
    if type(dict_game[0])==list:
        card_1 = dict_game[0][1]
        return card_1

async def card_2():

    if type(dict_game[1])==list:
        card_2 = dict_game[1][1]
        return card_2

async def card_3():
        if type(dict_game[2])==list:
            card_3 = dict_game[2][1]
            return card_3

async def card_4():

    if type(dict_game[3])==list:
        card_4 = dict_game[3][1]
        return card_4

async def card_5():

    if type(dict_game[4])==list:
        card_5 = dict_game[4][1]
        return card_5

async def card_6():
    if type(dict_game[5])==list:
        card_6 = dict_game[5][1]
        return card_6

async def card_7():

    if type(dict_game[6])==list:
        card_7 = dict_game[6][1]
        return card_7

async def card_8():

    if type(dict_game[7])==list:
        card_8 = dict_game[7][1]
        return card_8


player_1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'{dict_game[0][1]}', callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)


player_2= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_3= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_4= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_5= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_6= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_7= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)
player_8= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Карти 1", callback_data="test:cards1:1"),
            InlineKeyboardButton(text="Карти 2", callback_data="test:cards2:1"),
            InlineKeyboardButton(text="Карти 3", callback_data="test:cards3:1")
        ],
        [
            InlineKeyboardButton(text="Карти 4", callback_data="test:cards4:1"),
            InlineKeyboardButton(text="Стіл", callback_data="test:table"),
            InlineKeyboardButton(text="Карти 5", callback_data="test:cards5:1")
        ],
        [
            InlineKeyboardButton(text="Карти 6", callback_data="test:cards6:1"),
            InlineKeyboardButton(text="Карти 7", callback_data="test:cards7:1"),
            InlineKeyboardButton(text="Карти 8", callback_data="test:cards8:1")
        ],
    ]
)