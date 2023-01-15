# 1.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random
import time

max_candy = 28
min_candy = 1
confection = 2023


def get_ures_name(plr: int) -> str:
    name = input(f'Введите имя игрока №{plr}: ')
    return name


def get_quantity_candy() -> int:
    while True:
        try:
            number = abs(int(input(f'Задайте исходное количество конфет большее {max_candy}: ')))
            if number > max_candy:
                return number
            else:
                print(f'Вы задали меньше требуемого количеста конфет: {max_candy}')
        except:
            print('Должно быть введено положитеньное натуральное число')


def take_candy() -> int:
    while True:
        try:
            number = abs(int(input(f'Возьмите конфеты: ')))
            break
        except:
            print('Должно быть введено положитеньное натуральное число')
    return number


def take_candy_from_confection(take: int, con: int) -> int:
    if take < min_candy:
        print(f'Вы не можете забирать меньше {min_candy} конфет')
    elif take > max_candy:
        print(f'Больше {max_candy} конфет брать нельзя')
    elif take > con:
        print('Нельзя взять больше конфет чем имеется в остатке')
    else:
        con -= take
    return con


def make_choce_bot(con: int) -> int:
    time.sleep(random.randint(0, 11) / 10)  # иммитация мыслительного процесса - принятия решения
    bot_choice = con % (max_candy + min_candy)
    if bot_choice == 0:
        bot_choice = min_candy  # тянем время - ожидаем ошибку оппонента
    return bot_choice


def make_choice_user(con: int) -> int:
    own_choice = con
    while own_choice == con:
        own_choice = take_candy_from_confection(take_candy(), con)
    return con - own_choice


def choice_of_decision_algorithm(plrs: list, hmch: dict) -> dict:
    for plr in plrs:
        while True:
            ch = input(f'Выберите метод принятия решения для игрока - {plr}\n'
                       f'\t - если игрок играет сам, то введите текст \'сам\',\n'
                       f'\t - если машина играет за него, то введите\'бот\': ')
            match ch.lower():
                case 'сам':
                    hmch[plr] = make_choice_user
                    break
                case 'бот':
                    hmch[plr] = make_choce_bot
                    break
                case _:
                    print('Повторите попытку внимательнее')
    return hmch


def make_move(f, con: int) -> int:
    return take_candy_from_confection(f(con), con)


players = list()
players.append(get_ures_name(1))
players.append(get_ures_name(2))

whoMakeChoice = dict()
whoMakeChoice = choice_of_decision_algorithm(players, whoMakeChoice)

confection = get_quantity_candy()

time.sleep(random.randint(0, 10) / 10)
player = random.randint(False, True)
print(f'По результату жеребьёвки первых ходит {players[player]}')

while confection:
    confection = make_move(whoMakeChoice[players[player]], confection)
    if not confection:
        print(f'Победил {players[player]}')
        break
    else:
        print(f'Ход сделал {players[player]}, осталось {confection} конфет')
    if player:
        player = False
    else:
        player = True
