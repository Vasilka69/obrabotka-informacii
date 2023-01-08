import math

def len_number(x):
    if x == 0:
        return 1
    len_ = 0
    while x:
        x //= 10
        len_  += 1
    return (len_)

def ss2(n): #двоичная сс
    b = ''
    while n > 0:
        b += str(n % 2)
        n = n // 2
    return(b[::-1]) 

def mon(number): #монотонный код
    unar = ''
    l = len(ss2(number))
    b = ss2(number)
    b = b[1:]
    for i in range(l-1):
        unar += str(1)
    unar += str(0)
    mon = str(unar) + str(b) 
    return(mon) 

def code(d,w,l): #кодовая последовательность
    second = ss2(d)
    second_l = math.ceil(math.log2(w))
    if len(second) < second_l:
        while len(second) != second_l:
            second = '0' + second
            
    code = '1' + second + mon(l)
    return(code)

def find_max_l(input_str, search_str):# (строка, найти)
    l1 = [] #массив с индексами повторов
    max_n = 0
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str[0], index)
        if i == -1:
            return l1
        n = 0  # длина повтора
        while (n < len(input_str) - i) and (n < len(search_str)) and (search_str[n] == input_str[i + n]):
            n += 1
        if n >= max_n:
            max_n = n
            l1.append(i)
        index = i + 1
    return l1


def makeLZ77(dictionary, buf):
    r = find_max_l(dictionary, buf) # номер совпадающего символа в словаре с конца
    # первый символ буфера в словаре не найден
    if (len(r) == 0):
        flag = 0
        n = 0  # длина подстроки
        Code = "0bin(" + str(buf[0]) + ")"
        byte = 9
        return [flag, buf[0] ,'-','-',n, Code, byte]# flag,text, d,w,l, code, byte
    # первый символ буфера в словаре найден смещение - i
    else:
        flag = 1
        n = 0  # длина подстроки
        text = ''
        while (n < len(dictionary) - r[-1]) and (n < len(buf)) and (buf[n] == dictionary[r[-1] + n]):
            text += buf[n]
            n += 1
            #print('d = {0} '.format(len(dictionary) - r[-1] - 1))
            #print('w = {0} '.format(len(dictionary)))
            #print('l = {0} '.format(n))
            Code = code(len(dictionary) - r[-1] - 1, len(dictionary), n) # код в lz77 (d=len(dictionary) - r - 1,w=len(dictionary),l=n)
            byte = len(Code)
        return (flag, text, len(dictionary) - r[-1] - 1 ,len(dictionary), n, Code, byte) # flag, text, d,w,l, code, byte
    # сдвиг курсора код и размер кода

def vivod(text):
    ld = len(text)
    lb = len(text)
    dictionary = ''
    buf = text
    shag = 0
    sum_byte = 0
    print('=={0}==={1}==={2}==={3}==={4}==={5}==={6}==={7}==={8}==={9}=='.format(''.ljust(len(text), '='),''.ljust(len(text), '='),''.ljust(3, '='),''.ljust(4, '='),''.ljust(10, '='),''.ljust(3, '='),''.ljust(3, '='),''.ljust(3, '='),''.ljust(15, '='),''.ljust(4, '=')))
    print('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |'.format('словарь'.center(len(text)), 'буфер'.center(len(text)), 'шаг'.center(3), 'флаг'.center(4), 'текст'.center(10), 'd'.center(3), 'w'.center(3), 'l'.center(3), 'код'.center(15), 'биты'.center(4)))
    print('|-{0}-|-{1}-|-{2}-|-{3}-|-{4}-|-{5}-|-{6}-|-{7}-|-{8}-|-{9}-|'.format(''.ljust(len(text), '-'),''.ljust(len(text), '-'),''.ljust(3, '-'),''.ljust(4, '-'),''.ljust(10, '-'),''.ljust(3, '-'),''.ljust(3, '-'),''.ljust(3, '-'),''.ljust(15, '-'),''.ljust(4, '-')))
    while buf != '':
        lz = makeLZ77(dictionary, buf)
        if lz[0] == 0:
            sum_byte += lz[6]
            print('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |'.format(dictionary.ljust(len(text), '·'), buf.ljust(len(text), '·'), str(shag).center(3), str(lz[0]).center(4), lz[1].center(10), str(lz[2]).center(3), str(lz[3]).center(3), str(lz[4]).center(3), lz[5].center(15), str(lz[6]).center(4)))
            dictionary += buf[0]
            buf = buf[1:]
            shag += 1
        else:
            sum_byte += lz[6]
            print('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |'.format(dictionary.ljust(len(text), '·'), buf.ljust(len(text), '·'), str(shag).center(3), str(lz[0]).center(4), lz[1].center(10), str(lz[2]).center(3), str(lz[3]).center(3), str(lz[4]).center(3), lz[5].center(15), str(lz[6]).center(4)))
            dictionary += buf[:lz[4]]
            buf = buf[lz[4]:]
            shag += 1
    print('=={0}==={1}==={2}==={3}==={4}==={5}==={6}==={7}==={8}==={9}=='.format(''.ljust(len(text), '='),''.ljust(len(text), '='),''.ljust(3, '='),''.ljust(4, '='),''.ljust(10, '='),''.ljust(3, '='),''.ljust(3, '='),''.ljust(3, '='),''.ljust(15, '='),''.ljust(4, '=')))
         
    print('итого  {0}  бит'.format(sum_byte))
# -*- Main -*-
#who_chatters_to_you_will_chatter_about_you
#if_we_cannot_do_as_we_would_we_should_do_as_we_can
vivod("who_chatters_to_you_will_chatter_about_you")