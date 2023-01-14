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
            return number
        except:
            print('Должно быть введено положитеньное натуральное число')


def take_candy_from_confection(take: int, con: int) -> int:
    if take == 0:
        print('Вы не можете пропускать ход')
    elif take > max_candy:
        print(f'Больше {max_candy} конфет брать нельзя')
    elif take > con:
        print('Нельзя взять больше конфет чем имеется в остатке')
    else:
        con -= take
    return con


confection = get_quantity_candy()
time.sleep(random.randint(0, 10) / 10)
bot = random.randint(False, True)
print(bot)

while confection:
    if bot:
        time.sleep(random.randint(0, 10) / 10)
        if max_candy * 3 < confection:
            confection = take_candy_from_confection(max_candy, confection)
        elif max_candy * 2 + 1 <= confection < max_candy * 3:
            confection = take_candy_from_confection(confection - (max_candy * 2), confection)
        elif max_candy + 1 < confection < max_candy * 2:
            confection = take_candy_from_confection(confection - (max_candy + 1), confection)
        elif confection <= max_candy:
            confection = take_candy_from_confection(confection, confection)
            if not confection:
                print('Победил БОТ')
                break
        else:
            confection = take_candy_from_confection(1, confection)
            print(f'Что-то пошло не так {confection}')
        bot = False
        print(f'Ход сделал БОТ {confection}')
    else:
        own_choce = confection
        while own_choce == confection:
            own_choce = take_candy_from_confection(take_candy(), confection)
        confection = own_choce
        if not confection:
            print('Победил Пользователь')
            break
        print(f'Ход сделал пользователь {confection}')
        bot = True
