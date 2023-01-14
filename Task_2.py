# 1.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

max_candy = 28
min_candy = 1
import random


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
bot = random.randint(False, True)
print(bot)

while confection:
    if bot:
        bot = False
    else:
        bot = True

