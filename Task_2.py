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


confection = get_quantity_candy()
time.sleep(random.randint(0, 10)/10)
bot = random.randint(False, True)
print(bot)

while confection:
    if bot:
        time.sleep(random.randint(0, 10) / 10)
        if confection > max_candy:
            confection -= random.randint(min_candy, max_candy)
        else:
            confection -= confection
            print('Победил БОТ')
        bot = False
    else:
        bot = True
        print(confection)
