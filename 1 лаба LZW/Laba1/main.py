import math as m
from struct import *

def printm(mas):
    print('---')
    for i in mas:
        print(i)
    print('---')

def printm2d(mas):
    print('---')
    for i in range(len(mas[0])):
        for j in range(len(mas)):
            try:
                if i != 0 and len(str(mas[j][i])) < 4:
                    for _ in range(j-1):
                        print('', end='\t')
                if i != 0 and j > 2 and len(str(mas[j][i])) >= 4:
                    print('', end='\t')
                if i != 0 and j > 3 and len(str(mas[j][i])) >= 4:
                    print('', end='\t')

                print(mas[j][i], end='\t\t')
            except:
                print(' ', end='')
        print()
    print('---')


def LZW_table(text):
    print(f'Исходный текст: {text}')
    n = len(text)
    print(f'Длина текста: {n}')
    esc = ''
    dictionary = [esc]

    lettercost = 8

    table = list([0] * 5)

    table[0] = list(['Шаг', 0])
    table[1] = list(['Словарь', esc])
    table[2] = list(['Номер слова', '-'])
    table[3] = list(['Кодовые символы', '-'])
    table[4] = list(['Затраты (бит)', '-'])

    c = 1
    N = 0
    newword = ''
    while N < n:
        #print(f'N = {N}')
        table[0].append(c)
        temp = text[N]
        l = 1
        while dictionary.__contains__(esc + temp) or dictionary.__contains__(temp):
            if N + l < n:
                temp += text[N+l]
                l += 1
            else:
                break
        find = ''
        if len(temp) == 1:
            find = temp
        else:
            find = temp[:-1]
        num = 0
        wordfound = False
        for j in range(len(dictionary)):
            if dictionary[j] == esc + find or dictionary[j] == find:
                num = j
                wordfound = True
        if N == 0:
            table[3].append('')
        else:
            count = m.ceil(m.log2(c - 1))
            if num != 0:
                count -= len(str(bin(num))[2:])
            table[3].append('0' * count)
        if wordfound:
            table[3][len(table[3]) - 1] += str(bin(num))[2:]
        else:
            table[3][len(table[3]) - 1] += f'bin({text[N+l-1]})'
        if not wordfound:
            newword = esc + temp
        else:
            newword = temp
        dictionary.append(newword)
        table[1].append(newword)
        table[2].append(num)

        if N == 0:
            table[4].append(f'0 + {lettercost} = {0 + lettercost}')
        else:
            if wordfound:
                table[4].append(f'{len(table[3][len(table[3]) - 1])}')
            else:
                table[4].append(f'log({c-1}) + {lettercost} = {m.ceil(m.log2(c-1)) + lettercost}')
        '''
        if N + l == n:
            break
        '''
        if l != 1:
            l -= 1
        N += l
        c += 1

    printm2d(table)
    '''
    summa = 0
    for i in table[4][2:]:
        summa += int(i.split(' ')[len(i.split(' ')) - 1])
    print(summa)
    '''
    #printm(dictionary)

FILE_PATH = 'example.txt'

def encode():
    file = open(FILE_PATH)
    text = file.read()
    esc = ''
    dictionary = []

    output = []
    '''
    dictionary = {}
    for letter in text:
        dictionary[letter] = ord(letter)
    '''
    n = len(text)
    N = 0
    while N < n:
        temp = text[N]
        l = 1
        while dictionary.__contains__(esc + temp) or dictionary.__contains__(temp):
            if N + l < n:
                temp += text[N+l]
                l += 1
            else:
                break

        find = ''
        if len(temp) == 1:
            find = temp
        else:
            find = temp[:-1]

        wordfound = False
        for j in range(len(dictionary) - 1):
            if dictionary[j] == esc + find or dictionary[j] == find:
                wordfound = True

        if not wordfound:
            #output.append(dictionary[len(dictionary)])
            newword = esc + temp
        else:
            newword = temp

        dictionary.append(newword)
        if N + l == n:
            break
        if l != 1:
            l -= 1
        N += l



    print(dictionary)
    out_dict = {}
    for i in dictionary:
        out_dict[i] = dictionary.index(i)
        print(i)
    print(out_dict)
    string = ''
    for symbol in text:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            out_dict.append(dictionary[dictionary.index(string)])
            string = symbol

    out_dict.append(string)
    print(output)

    out = FILE_PATH.split(".")[0]
    output_file = open(out + '_ENCODED' + "." + FILE_PATH.split(".")[1], "wb")

    for data in out_dict:
        output_file.write(pack('>H', int(data)))

    output_file.close()
    file.close()

def encode2():
    print('---ENCODE---')
    file = open(FILE_PATH)
    text = file.read()
    file.close()
    output = []
    '''
    dictionary = {}
    for letter in text:
        dictionary[letter] = ord(letter)
    '''
    print(f'Исходный текст: {text}')
    n = len(text)
    print(f'Длина текста: {n}')
    esc = ''
    dictionary = [esc]

    lettercost = 8

    table = list([0] * 5)

    table[0] = list(['Шаг', 0])
    table[1] = list(['Словарь', esc])
    table[2] = list(['Номер слова', '-'])
    table[3] = list(['Кодовые символы', '-'])
    table[4] = list(['Затраты (бит)', '-'])

    c = 1
    N = 0

    while N < n:
        #print(f'N = {N}')
        table[0].append(c)
        temp = text[N]
        l = 1
        while (dictionary.__contains__(esc + temp) or dictionary.__contains__(temp)) and N != n-1:
            if N + l < n:
                temp += text[N+l]
                l += 1
            elif N != n-1:
                break
        find = ''
        if len(temp) == 1:
            find = temp
        else:
            find = temp[:-1]
        num = 0
        wordfound = False
        for j in range(len(dictionary)):
            if dictionary[j] == esc + find or dictionary[j] == find:
                num = j
                wordfound = True
        table[3].append('')
        if wordfound:
            table[3][len(table[3]) - 1] += str(num - 1)
        else:
            table[3][len(table[3]) - 1] += f'{ord(text[N+l-1])}'
        if not wordfound:
            newword = esc + temp
        else:
            newword = temp
        dictionary.append(newword)
        table[1].append(newword)
        table[2].append(num)

        if N == 0:
            table[4].append(f'0 + {lettercost} = {0 + lettercost}')
        else:
            if wordfound:
                table[4].append(f'{len(table[3][len(table[3]) - 1])}')
            else:
                table[4].append(f'log({c-1}) + {lettercost} = {m.ceil(m.log2(c-1)) + lettercost}')
        '''
        if N + l == n:
            break
        '''
        if l != 1:
            l -= 1
        N += l
        c += 1

    printm2d(table)
    #printm(dictionary)

    code = table[3][2:]
    print(code)
    for i in code:
        print(chr(int(i)), end='\t')
    print()
    for i in code:
        print(i, end='\t')
    print()
    out = FILE_PATH.split(".")[0]
    '''
    output_file = open(out + '_ENCODED' + "." + FILE_PATH.split(".")[1], "wb")

    for data in code:
        output_file.write(pack('>H', int(data)))
    '''
    output_file = open(out + '_ENCODED' + "." + FILE_PATH.split(".")[1], "w")

    for data in code:
        output_file.write(chr(int(data)))
        print(int(data), end=' ')
    print()
    print(code)
    output_file.close()


def decode():
    print('---DECODE---')

    filename = FILE_PATH.split('.')[0] + '_ENCODED' + '.txt'
    file = open(filename)
    text = str(file.read())
    print(text)
    file.close()

    temp = []
    for letter in text:
        temp.append(ord(letter))
    #########
    #temp = [87, 72, 79, 95, 67, 1, 65, 84, 7, 69, 82, 83, 3, 7, 2, 3, 89, 2, 85, 3, 0, 73, 76, 22, 3, 4, 5, 7, 8, 10, 3, 6, 66, 17, 7, 15, 2, 18]

    print('-', end='')
    print(temp)

    out = ''
    for i in range(len(temp)):
        out += refFinder(temp, i, '')

    print(f'\"{out}\"')
    out2 = ''
    for i in out:
        out2 += str(ord(i)) + ' '
    print(out2)

    '''
    out2 = ''
    for i in out:
        if ord(i) >= 41:
            out2 += i
        else:
            out2 += out[ord(i) + 1]
    print(out2)
    '''


def refFinder(temp, i, ch):
    out = ''
    check = False
    for j in range(i):
        if j == int(temp[i]):
            out += refFinder(temp, j, chr(temp[j+1]))
            #print(f'1) {out}')

            if ch == '':
                print(j)
            '''
            if ch != '':
                print(ord(ch))
            '''
            if ch != '':
                print(len(temp))
                if int(ord(ch)) < 41:
                    #ch = temp[i]
                    #ch = str(chr(temp[i]))
                    #ch = str(chr(i))
                    #ch = str(ord(ch))
                    print(ord(ch))
                    ch = str(chr(temp[ord(ch)]))
                    #ch = '*'

            out += ch
            #print(f'2) {out}')
            check = True
            break
    if not check:
        if int(temp[i]) < 41:
            out += str(chr(temp[i]))
        else:
            out += chr(temp[i])
    return out

def main():
    text = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    #text = 'WHO_CHATTERS_TO_YOU_WILL_CHATTER_ABOUT_YOU'
    #LZW_table(text)
    #encode()
    encode2()
    decode()


if __name__ == '__main__':
    main()