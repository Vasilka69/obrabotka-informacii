import math
import random

numbers_of_blocks = 0
new_CBL = 0
err_index = 0

def arrCB(text, blokc_len):
    global new_CBL
    global numbers_of_blocks
    numbers_of_blocks = int(len(text) / blokc_len)
    print("количество блоков: {0}".format(numbers_of_blocks))
    CB = []
    CBL = 0
    x = 0
    k = 0
    for i in range(numbers_of_blocks):
        while blokc_len + int(math.pow(2, (x - 1)) - 1) >= int(math.pow(2, x) - 1):
            k += 1
            CB.append(int(math.pow(2, x) - 1) + ((blokc_len + CBL) * i))
            x += 1
        CBL = k
        k = 0
        x = 0
    new_CBL = blokc_len + CBL
    print("длина блока с  КБ: {0}".format(new_CBL))
    #print(CB)
    return CB


def add0CB(text, CB):
    for bit in CB:
        text = text[:bit] + '0' + text[bit:]
    if len(text) == 8:
        text = text[:-1]
    print('последовательность с добавлением нулевых КБ: {0}'.format(text))
    return text


def fillingCB(text):
    i = 0
    st2 = 1
    starsimv = []
    summa = 0
    while (st2 < len(text)):
        for j in range(st2 - 1, len(text), st2 * 2):
            if (j + st2 >= len(text)):
                starsimv.append(text[j: len(text)])
            else:
                starsimv.append(text[j: j + st2])
        print("{0} через {0}: {1}".format(st2, starsimv))
        for k in range(len(starsimv)):
            summa += int(starsimv[k])
        summa = sum(map(int, str(summa)))
        print("сумма единиц: ", + summa)
        if (summa % 2 != 0):
            text = text[:st2 - 1] + '1' + text[st2:]

        i += 1
        st2 = int(math.pow(2, i))
        summa = 0
        starsimv = []
    print('закодированная последовательность: {0}'.format(text))
    return text


def AddError(text):
    for j in range(numbers_of_blocks):
        indexerr = random.randint(new_CBL * j + 1, (new_CBL * (j + 1)) - 1)
        #indexerr = int(input("Ведите индекс элемента-ошибки: "))
        print("номер элемента-ошибки: {0}".format(indexerr))
        if text[indexerr-1] == '1':
            text = text[:indexerr - 1] + '0' + text[indexerr:]
        else:
            text = text[:indexerr - 1] + '1' + text[indexerr:]
        print('последовательность с ошибкой:      {0}'.format(text))
    return text

def Find_Fix_Error(text):
    i = 0
    st2 = 1
    starsimv = []
    summa = 0
    global err_index
    while (st2 < len(text)):
        for j in range(st2 - 1, len(text), st2 * 2):
            if (j + st2 >= len(text)):
                starsimv.append(text[j: len(text)])
            else:
                starsimv.append(text[j: j + st2])
        print("{0} через {0}: {1}".format(st2, starsimv))
        for k in range(len(starsimv)):
            summa += int(starsimv[k])
        summa = sum(map(int, str(summa)))
        print("сумма единиц: ", + summa)
        if (summa % 2 != 0):
            err_index += st2

        i += 1
        st2 = int(math.pow(2, i))
        summa = 0
        starsimv = []
    if err_index == 0:
        print("нет ошибки")
    if text[err_index - 1] == '0':
        text = text[:err_index - 1] + '1' + text[err_index:]
    else:
        text = text[:err_index - 1] + '0' + text[err_index:]
    print('исправленная последовательность: {0}'.format(text))
    return text

text = str(input("Ведите кодовую последовательность: "))
blokc_len = int(input("Ведите длину блока: "))
code_text = ''
new_CB = arrCB(text, blokc_len)
new_text = add0CB(text, new_CB)

for i in range(numbers_of_blocks):
    print('кодируемая часть/последовательность: {0}'.format(new_text[(new_CBL * i):(new_CBL * (i + 1))]))
    code_text += fillingCB(new_text[(new_CBL * i):(new_CBL * (i + 1))])
print('вся закодированная последовательность: {0}'.format(code_text))

error_text = AddError(code_text)

fix_text = ''
for i in range(numbers_of_blocks):
    print('часть/последовательность с ошибкой: {0}'.format(error_text[(new_CBL * i):(new_CBL * (i + 1))]))
    fix_text += Find_Fix_Error(error_text[(new_CBL * i):(new_CBL * (i + 1))])
    print("номер найденного элемента-ошибки: {0}".format(err_index + new_CBL * i))
    err_index = 0

print('вся правильная последовательность: {0}'.format(fix_text))