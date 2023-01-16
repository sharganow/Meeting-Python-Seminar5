# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


def get_user_name(plr: int) -> str:
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


def search_for_a_winner(board: list) -> str:
    for i in range(3):
        string = board[i][0]
        column = board[0][i]
        for j in range(3):
            if string != board[i][j]:
                string = 'No'
            if column != board[j][i]:
                column = 'No'
        if string != 'No':
            return string
        if column != 'No':
            return column
    center = board[1][1]
    for i in range(3):
        if center != board[2 - i][i]:
            center = 'No'
    if center != 'No':
        return center
    center = board[1][1]
    for i in range(3):
        if center != board[i][i]:
            center = 'No'
    return center


def enter_sign(board: list, entr: int, sign: str):
    for i in range(3):
        for j in range(3):
            if board[i][j] == entr:
                board[i][j] = sign
                break
        else:
            continue
        break
    else:
        print('Выбранная ячейка занята')

def



gameBoard = [[(string * 3 + column) for column in range(3)] for string in range(3)]
# players = [get_user_name(i) for i in range(1, 3)]
#
# whoMakeChoice = dict()
# choice_of_decision_algorithm(players, whoMakeChoice)
# userSign = dict()
# choice_sign_to_play(players, userSign)
#
# print(*sorted(whoMakeChoice.items()))
showBoard(gameBoard)
print(search_for_a_winner(gameBoard))

gameBoard[2][0] = gameBoard[1][1] = gameBoard[0][2] = 'Y'
showBoard(gameBoard)
enter_sign(gameBoard, int(input('Выберите поле: ')), 'X')
showBoard(gameBoard)

print(search_for_a_winner(gameBoard))

