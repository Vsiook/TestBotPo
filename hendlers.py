from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from config import dp, bot
import default_key
from db import chek_place, dict_game, chek_user
# from inline_key import player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8
import inline_key
@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Відкриваю меню ✔', reply_markup=default_key.menu)

@dp.message_handler(Text(equals=["Правила","Читати далі(1/6)","Читати далі(2/6)",
                                 "Читати далі(3/6)","Читати далі(4/6)","Читати далі(5/6)",
                                 "Повернутись в меню"]))
async def rules(message:Message):
    if message.text=="Правила":
        await bot.send_message(message.from_user.id, 'В техасский холдем играют стандартной колодой — 52 карты. В холдеме существуют две обязательные ставки, называемые блайндами (ставки вслепую). Игра начинается с того, что два игрока, ставят заранее определенную сумму, ещё до сдачи карт. Первый игрок ставит малый блайнд и следующий игрок ставит большой блайнд. Большой блайнд, как правило, в два раза больше малого блайнда.', reply_markup=default_key.startrule)
    if message.text == "Читати далі(1/6)":
        await bot.send_message(message.from_user.id, 'Префлоп\nКаждый игрок получает по две карты. Первый круг ставок начинается сразу после сдачи карт. Первый игрок, который может делать ставки, это игрок, сидящий сразу по левую руку от игрока, поставившего большой блайнд. Первый игрок обязан принять ставку (✅ Call), поднять ставку (⏫ Raise) или же сбросить карты (❌ Fold). Принять ставку (✅ Call) – сделать ставку, которая будет равна большому блайнду. Поднять ставку (⏫ Raise) – игрок ставит большую сумму денег, чем ставка предыдущего игрока.', reply_markup=default_key.rule2)
    if message.text == "Читати далі(2/6)":
        await bot.send_message(message.from_user.id, 'Сбросить карты (❌ Fold) – игрок кладёт карты лицом вниз и передвигает их к середине стола. После этого игрок не принимает участия в игре до следующей сдачи карт, и теряет все сделанные им ставки. Следующие игроки имеют право выбора между теми же тремя действиями: принять ставку (✅ Call), поднять ставку (⏫ Raise) или сбросить карты (❌ Fold). Игроки могут повторно повысить ставку (Re-Raise), сумма которой должна составлять как минимум размер последнего повышения ставки.', reply_markup=default_key.rule3)
    if message.text == "Читати далі(3/6)":
        await bot.send_message(message.from_user.id, 'Флоп\nНа стол сдаются три общие карты. Второй круг ставок и все последующие круги начинаются с первого, ещё не сбросившего карты игрока, сидящего слева от дилера. Вдобавок к принятию ставки (✅ Call), поднятию ставки (⏫ Raise) или повторному повышению ставки (Re-Raise) игрок теперь может пропустить (✊ Check), при этом, не скидывая карты и не делая ставки, пока опять не подойдёт его очередь. В том случае если ставка была сделана, то игрок может принять её (✅ Call), поднять ставку (Raise) или повторно повысить ставку (Re-Raise). В противном случае игрок должен сбросить карты (❌ Fold). Таким образом, в конце круга все игроки сделают одинаковое количество ставок, кроме игроков, которым не хватило фишек. В таком случае он может поставить все фишки (💰 All-In), и тогда появляется один или несколько дополнительных банков (Side Pots), что ограничивает сумму, которую он может выиграть.', reply_markup=default_key.rule4)
    if message.text == "Читати далі(4/6)":
        await bot.send_message(message.from_user.id, 'Терн\nСдается четвёртая общая карта. Проходит третий круг ставок.', reply_markup=default_key.rule5)
    if message.text == "Читати далі(5/6)":
        await bot.send_message(message.from_user.id, 'Ривер\nСдается на стол последняя, пятая общая карта. Это последний круг ставок, после которого игроки вскрывают свои карты и определяется победитель. Если два или более игроков имеют одинаковую комбинацию, то выигрывает игрок, комбинация которого содержит вторую по старшинству карту (Kicker). Если ни у кого нет такой карты (Kicker), то банк делится между этими игроками.', reply_markup=default_key.rule6)
    if message.text == "Повернутись в меню":
        await bot.send_message(message.from_user.id, 'Відкриваю меню ✔', reply_markup=default_key.menu)


@dp.message_handler(Text(equals=["Комбінації"]))
async def get_button(message:Message):
    # if message.text=="Комбінації":
        # await bot.send_message(message.from_user.id, 'тест', reply_markup=default_key.menu2)
    await bot.send_message(message.from_user.id, '''Комбинации карт в порядке убывания их достоинства:\n
                9. ♥️A ♥️K ♥️Q ♥️J ♥️10 — Роял-флэш: стрит от 10 до туза из карт одинаковой масти.\n
                8. ♣️9 ♣️8 ♣️7 ♣️6 ♣️5 — Стрит-флэш: стрит от любой карты, состоящий из карт одинаковой масти.\n
                7. ♥️A ♠️A ♦️A ♣️A — Каре: любые четыре карты одинакового ранга.\n
                6. ♥️A ♠️A ♦️A ♠️K ♥️K — Фул-хаус: любые три карты одинакового ранга и пара из двух других карт.\n
                5. ♠️A ♠️9 ♠️7 ♠️6 ♠️2 — Флэш: любые пять карт одной масти в любой последовательности.\n
                4. ♥️6 ♣️5 ♦️4 ♠️3 ♥️2 — Стрит: любые пять последовательных по рангу карт разных мастей.\n
                3. ♥️A ♠️A ♦️A — Тройка: любые три карты одинакового ранга.\n
                2. ♥️A ♠️A ♣️K ♦️K — Две пары: любые две карты одного ранга вместе с любыми двумя картами одинакового достоинства.\n
                1. ♥️A ♠️A — Пара: любые две карты одного ранга.\n
                0. ♥️A — Старшая карта: любая рука, из которой невозможно сложить указанные выше комбинации в покере.''')
    # if message.text == "Інформація":
    #     pass

@dp.message_handler(Text(equals=["Баланс"]))
async def main_func(message:Message):
    await bot.send_message(message.from_user.id, "Бот знаходиться в тестовому режимі, тому кожному гравцеві будуть видаватись 1000 фішок, коли він сідає за стіл, попередні будуть анульовані.\nДякуємо за розуміння!!!")


@dp.message_handler(Text(equals=["Сісти за стіл"]))
async def main_func(message:Message):
    if chek_place()!=8 and chek_user(message.from_user.id)==1:
        numb = chek_place()
        if numb == 0:
            dict_game[0]=[message.from_user.id, 'карти', 'info', 'more info']
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_2 )
            await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=default_key.game)
        if numb == 1:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_1)
            await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=default_key.game)
            dict_game[1]=[message.from_user.id, 'карти', 'info', 'more info']
        if numb == 2:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_3)
            dict_game[2]=[message.from_user.id, 'карти', 'info', 'more info']
        if numb == 3:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_4)
        if numb == 4:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_5)
        if numb == 5:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_6)
        if numb == 6:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_7)
        if numb == 7:
            await bot.send_message(message.from_user.id, 'Одну секунду', reply_markup=inline_key.player_8)
        print(dict_game)
    else:
        await bot.send_message(message.from_user.id, "Вибачте, сталася помилка")


@dp.message_handler(Text(equals=["Call"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["Fold"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["Bet"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["Chek"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["All-in"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["Raise"]))
async def main_func(message: Message):
    pass

@dp.message_handler(Text(equals=["Вийти"]))
async def main_func(message: Message):
    await bot.send_message(message.from_user.id, 'Повертайтесь ще, ми вас чекаємо.', reply_markup=default_key.menu)







