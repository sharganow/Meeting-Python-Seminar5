# 3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def compressFile(orig: str) -> str:
    compress = ''
    char = ''
    word = ''
    for i, ch in enumerate(orig):
        match len(char):
            case 0:
                char = ch
                count_repeat = 0
            case 1:
                if char == ch:
                    count_repeat += 1
                else:
                    if count_repeat > 0:
                        compress += str(count_repeat) + char
                        count_repeat = 0
                        char = ch
                    else:
                        char += ch
            case _:
                if char[-1] == ch and len(word) == 0:
                    compress += char[:-1]
                    count_repeat = 1
                    char = char[-1]
                else:
                    char += ch
                    i = 1
                    while True:
                        if i > len(char) // 2:
                            break
                        else:
                            if len(word) > 1:
                                cut = len(char) % len(word)
                                if cut:
                                    if char[-cut:] != word[:cut]:
                                        compress += str(count_repeat) + '(' + word + ')'
                                        count_repeat = 0
                                        char = char[-cut:]
                                        word = ''
                                    break
                                else:
                                    if char[-len(word):] == word:
                                        char = word[:]
                                        count_repeat += 1
                                        break
                                    else:
                                        compress += str(count_repeat) + '(' + word + ')'
                                        count_repeat = 0
                                        char = char[-len(word):]
                                        word = ''
                                        break
                            else:
                                if char[-i:] == char[-(i * 2):-i]:
                                    word = char[-i:]
                                    count_repeat = 1
                                    cut = len(char) % (2 * i)
                                    compress += char[:cut]
                                    char = char[-(i * 2):-i]
                                    break
                                else:
                                    i += 1
    match len(char):
        case 1:
            if count_repeat > 0:
                compress += str(count_repeat) + char
            else:
                compress += char
        case _:
            if len(word) == 0:
                compress += char
            else:
                cut = len(char) % len(word)
                compress += str(count_repeat) + '(' + word + ')'
                if cut:
                    compress += char[-cut:]
    return compress


def deCompressFile(comp: str) -> str:
    orig = ''
    count_repeat = ''
    char = ''
    word = ''
    i = 0
    nums = [str(i) for i in range(10)]
    while True:
        if i >= len(comp):
            break
        if len(count_repeat) > 0:
            if comp[i] in nums:
                count_repeat += comp[i]
            else:
                if len(word) > 0:
                    if comp[i] == ')':
                        orig += ''.join([word for _ in range(int(count_repeat)+1)])
                        word = ''
                        count_repeat = ''
                    else:
                        word += comp[i]
                else:
                    if comp[i] == '(':
                        i += 1
                        word += comp[i]
                    else:
                        orig += ''.join([comp[i] for _ in range(int(count_repeat) + 1)])
                        count_repeat = ''
        else:
            if comp[i] in nums:
                count_repeat += comp[i]
            else:
                orig += comp[i]
        i += 1
    return orig



while True:
    try:
        file_name = input('Введите имя файла с которым желаете работать: ')
        with open(file_name, "r") as data:
            sourse_text = data.read()
        name, file = file_name.split('.')
        match file:
            case 'txt':
                compress_text = compressFile(sourse_text)
                name += '.cmp'
                with open(name, "a") as data:
                    data.write(compress_text)
                break
            case 'cmp':
                original_text = deCompressFile(sourse_text)
                name += '.txt'
                with open(name, "a") as data:
                    data.write('\n' + original_text)
                break
    except:
        print('Запрашиваемый файл в дирректории отсутствует')
