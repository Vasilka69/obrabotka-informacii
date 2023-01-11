import math
import random
import struct


def zip(inp):
    print(f'---Кодер---')
    print(f'Входная последовательность: {inp}')
    print(f'Длина последовательности: {len(inp)}')
    powers = []
    pow = 0
    while 2 ** pow <= len(inp):
        powers.append(2 ** pow)
        pow += 1
    print(f'Степени: {powers}')

    output = ''
    index = 0
    for i in range(len(inp) + len(powers)):
        if powers.__contains__(i + 1):
            output += '0'
        else:
            output += inp[index]
            index += 1

    for i in powers:
        index = i - 1
        counter = 0
        while index < len(output):
            for j in range(index, index + i):
                if j < len(output):
                    counter += int(output[j])
                else:
                    break
            index += i * 2
        output = output[:i - 1] + str(counter % 2) + output[i:]

    print(f'Выходная последовательность: {output}')
    return output

def unzip(inp):
    print(f'---Декодер---')
    print(f'Входная последовательность: {inp}')
    powers = []
    pow = 0
    while 2 ** pow <= len(inp):
        powers.append(2 ** pow)
        pow += 1
    print(f'Степени: {powers}')

    errors = []
    for power in powers:
        #print(f'Power = {power}')
        ctrlBit = int(inp[power-1])
        summ = int(0)
        bit = int(power - 1)
        while bit <= (len(inp) - power):
            for i in range(power):
                summ += int(inp[bit])
                bit += 1
            bit += power
        summ %= 2
        if summ != ctrlBit:
            errors.append(power)
    if len(errors) == 0:
        print('Ошибок не найдено')
        '''
        for power in powers:
            power -= 1
        output = ''
        for i in range(len(inp)):
            if not i in powers:
                output += inp[i]
        print(f'Выходная последовательность: {output}')
        '''
        print(f'Выходная последовательность: {inp}')
    else:
        print(f'Контрольные биты с ошибкой: {errors}')
        # Исправление
        index = sum(errors) - 1
        print(f'Индекс бита с ошибкой: {sum(errors)}')
        #output = inp[:index] + str(0) + inp[index + 1:] if inp[index] == '1' else inp[:index + 1] + str(1) + inp[index:]
        output = inp[:index] + str(0) + inp[index + 1:] if inp[index] == '1' else inp[:index] + str(1) + inp[index + 1:]
        print(f'Исправленная последовательность: {output}')


def doerror(code: str):
    index = random.randint(0, len(code))
    output = ''
    for i in range(len(code)):
        if i == index:
            if code[i] == '0':
                output += '1'
            else:
                output += '0'
        else:
            output += code[i]
    return output, index

def getbits(file_path):
    file = open(file_path, 'r')
    inp = file.read()
    file.close()

    code = ''.join(str(format(ord(byte), '08b') + ',') for byte in inp)[:-1]
    #print(code)

    '''
    code = ''
    for letter in inp:
        code += str("{0:b}".format(letter))
    print(code)
    '''
    bitsarr = code.split(',')
    #print(bitsarr)

    bytesarr = []
    for byte in bitsarr:
        bytesarr.append(int(byte, 2))
    #print(bytesarr)

    text = ''
    for char in bytesarr:
        text += (chr(char))
    #print(text)

    stream = ''
    for byte in bitsarr:
        temp = ''
        for bit in byte:
            temp += bit
        stream += temp
    #print(stream)
    return stream

if __name__ == '__main__':
    file_path = 'example.txt'

    stream = getbits(file_path)
    # Деление на блоки
    blocks = []
    '''
    for block in range(math.ceil(len(stream) / 11)):
        temp = ''
        for i in range(11):
            if block < len(stream):
                temp += stream[block * 11 - 1 + i]
            else:
                temp += '0'
        blocks.append(temp)
    '''
    temp = ''
    for index in range(len(stream)):
        if index % 11 != 0 or index == 0:
            temp += stream[index]
        else:
            blocks.append(temp)
            temp = stream[index]
    temp += '0' * (11 - len(temp))
    blocks.append(temp)
    print(f'Блоки:\n{blocks}\n')



    '''
    file = open(file_path.split('.')[0] + '_DAMAGED.txt', 'w')
    file.write(text)
    file.close()
    #file = open()
    '''
    # Сохранение файла в коде
    for block in blocks:
        inp = block
        code = zip(inp)
    '''
    for block in blocks:
        #inp = str('10110111001')
        inp = block
        code = zip(inp)
        print()
        code, i = doerror(code)  # С ошибкой
        pr = '001001100111001'
        print(f'Код с ошибкой в {i+1} бите: {pr}')
        print(f'Код с ошибкой в {i+1} бите: {code}')
        unzip(code)
    '''


