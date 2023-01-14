# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# p.s. Реализовал с чтением из файла "text.txt" и сохранением файл результата "text_cut.txt"

def make_text_dictionary(d: dict, s: str) -> dict:
    for i in s:
        if i in d:
            continue
        else:
            d[i] = ord(i)
    return d


def get_eliminator(keys: str, text: str, ln: int) -> str:
    while True:
        try:
            ipt = input(f'Ведите фрагмент слова из {ln}-х символов: ')
            if len(ipt) == ln:
                for i in ipt:
                    if i in keys:
                        continue
                    else:
                        print(f'В тексте не встречается символ {i}')
                        break
                else:
                    if ipt.lower() in text.lower():
                        break
                    else:
                        print(f'В тексте фрагмент {ipt} не встречается')
            else:
                print(f'Вводимый фрагмент должен состоять из {ln} символов')
        except:
            print('Вы делаете что-то неверное')
    return ipt


def remove_words_with_elim(src_txt: str, elm: str, splt: str) -> str:
    while elm.lower() in src_txt.lower():
        ind = src_txt.lower().index(elm.lower())
        start_ind = ind
        if start_ind != 0:
            while (src_txt[start_ind] not in splt) and (start_ind > 0):
                start_ind -= 1
        stop_ind = ind + len(elm)
        if stop_ind < len(src_txt):
            while (src_txt[stop_ind] not in splt) and (stop_ind < len(src_txt)):
                stop_ind += 1
        if start_ind == 0:
            if len(src_txt) > stop_ind + 2:
                src_txt = src_txt[stop_ind + 1:]
            else:
                src_txt = src_txt[stop_ind:]
        elif stop_ind == len(src_txt):
            if start_ind > 0:
                src_txt = src_txt[:start_ind] + src_txt[stop_ind:]
            else:
                src_txt = ' '
        else:
            if src_txt[start_ind] == src_txt[stop_ind]:
                src_txt = src_txt[:start_ind] + src_txt[stop_ind:]
            else:
                src_txt = src_txt[:start_ind+1] + src_txt[stop_ind:]
    else:
        return src_txt


sourse_text = ''
while True:
    try:
        with open('text.txt', "r") as data:
            sourse_text = data.read()
        break
    except:
        with open('text.txt', "w") as data:
            sourse_text = ['Любимая! \n'
                           'Сказать приятно мне:\n'
                           'Я избежал паденья с кручи.\n'
                           'Теперь в Советской стороне\n'
                           'Я самый яростный попутчик.']
            data.write(sourse_text)

dct = make_text_dictionary(dict(), sourse_text.lower())
dct = make_text_dictionary(dct, sourse_text.upper())
txt_keys = sorted(dct.keys())
split_keys = [x for x in txt_keys if x < 'Ё' or 'ё' < x]
alpha_keys = [x for x in txt_keys if x not in split_keys]
elim = get_eliminator(alpha_keys, sourse_text, 3)

sourse_text = remove_words_with_elim(sourse_text, elim, split_keys)

with open('text_cut.txt', "w") as data:
    data.write(sourse_text)

# print(*sorted(dct.items()))
# print(*txt_keys)
# print(*split_keys)
# print(*alpha_keys)
