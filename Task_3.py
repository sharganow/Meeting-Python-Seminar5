# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


def get_ures_name(plr: int) -> str:
    name = input(f'Введите имя игрока №{plr}: ')
    return name


def choice_of_decision_algorithm(plrs: list, hmch: dict):
    for plr in plrs:
        while True:
            ch = input(f'Выберите метод принятия решения для игрока - {plr}\n'
                       f'\t - если игрок играет сам, то введите текст \'сам\',\n'
                       f'\t - если машина играет за него, то введите\'бот\': ')
            match ch.lower():
                case 'сам':
                    hmch[plr] = ch
                    break
                case 'бот':
                    hmch[plr] = ch
                    break
                case _:
                    print('Повторите попытку внимательнее')


def choice_sign_to_play(plrs: list, hmch: dict):
    for plr in plrs:
        while True:
            ch = input(f'Выберите персональный смвол отметки хода для игрока - {plr}: ')
            if len(ch) == 1:
                if ch not in hmch.values():
                    hmch[plr] = ch
                    break
                else:
                    print('Этот символ уже занят')
            else:
                print('Символ должен состоять из одного знака')


def showBoard(board: list):
    for i in range(len(board)):
        print(f'  {board[i][0]} | {board[i][1]} | {board[i][2]}')
        if i < len(board) - 1:
            print(f' ---|---|--- ')


gameBoard = [[(string * 3 + column) for column in range(3)] for string in range(3)]
players = [get_ures_name(i) for i in range(1, 3)]



whoMakeChoice = dict()
choice_of_decision_algorithm(players, whoMakeChoice)
userSign = dict()
choice_sign_to_play(players, userSign)

print(*sorted(whoMakeChoice.items()))
# showBoard(gameBoard)
