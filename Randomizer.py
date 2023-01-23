# ЕЩЕ ОДНО НЕОБЯЗАТЕЛЬНОЕ ДЗ - НАПИСАТЬ СВОЙ РАНДОМАЙЗЕР (НЕ ИСПОЛЬЗОВАТЬ БИБЛИОТЕКУ RANDOM)

import textwrap
import time
import random
import math
ident_print = 10


def GetNumSigns(value: int) -> int:
    value = value if value > 0 else -value
    gns = 0
    while value > 0:
        value //= 10
        gns += 1
    return gns


def GetRandStr() -> str:
    ter = list(str(time.perf_counter()).split('.'))
    while len(ter[1]) < 7:
        ter[1] += '0'
    return ter[1]


def GetRandChar() -> str:
    one_chr = GetRandStr()
    return one_chr[-1]


def GetRandSign(limit: int) -> int:
    getSign = round((int(GetRandChar()) * limit) / 9)
    return limit - 1 if getSign >= limit else getSign


def RandInt(start: int, stop: int) -> int:
    start, stop = (stop, start) if start > stop else (start, stop)
    delta = stop - start
    if delta == 0:
        return start
    numSignDelta = GetNumSigns(delta)
    randStr = GetRandStr()
    while numSignDelta > len(randStr):
        randStr += GetRandChar()
    else:
        randStr = randStr[-numSignDelta:]

    strtLst = list(randStr)
    randLst = list()
    while len(strtLst):
        randLst.append(strtLst.pop(GetRandSign(len(strtLst))))
    semiRand = int(''.join(randLst))
    limitRand = int('9' * numSignDelta)
    deltaRand = round((delta * semiRand) / limitRand)
    return start + deltaRand


# print(f'Сгенерировано случайное число: {RandInt(100, -100)}')


#
# available_clocks = [
#     ('monotonic', time.monotonic),
#     ('perf_counter', time.perf_counter),
#     ('process_time', time.process_time),
#     ('time', time.time),
# ]
#
# for clock_name, func in available_clocks:
#     info = time.get_clock_info(clock_name)
#     rez = textwrap.dedent(f'''\
#     {clock_name}:
#         adjustable    : {info.adjustable}
#         implementation: {info.implementation}
#         monotonic     : {info.monotonic}
#         resolution    : {info.resolution}
#         current       : {func()}
#     ''')
#     print(rez)
#
# print(time.monotonic())
# print(time.perf_counter())
# print(time.process_time())
# print(time.time())


# def AlignedPrint(start, indent, second) -> None:
#     multiple = 0
#     indent_str = '\t'  # эквивалентно четырём символам
#     multiple = indent // 4 - len(str(start)) // 4
#     indent_str *= multiple
#     print('{}{}{}'.format(start, indent_str, second))
#
#
# rands = dict()
# controlCycl = 0
# for _ in range(100):
#     rand = random.randint(False, True)
#     # rand = RandInt(False, True)
#     if rand in rands:
#         rands[rand] += '*'
#     else:
#         rands[rand] = '*'
#     controlCycl += 1
#     time.sleep(1 / 10000)
#
# randKeys = list(rands.keys())
# randKeys.sort()
# for i in randKeys:
#     AlignedPrint(i, ident_print, rands[i])
#
# print(f'В заданном диапазоне значений выпало случайным образом {len(rands)} значений из {controlCycl} попыток')
