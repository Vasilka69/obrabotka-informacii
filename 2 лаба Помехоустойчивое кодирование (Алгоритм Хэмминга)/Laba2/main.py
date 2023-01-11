import random

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

    print(f'Выходная последовательность: {output}\n')
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
        print(f'Выходная последовательность: {inp}\n')
        return inp
    else:
        print(f'Контрольные биты с ошибкой: {errors}')
        # Исправление
        index = sum(errors) - 1
        print(f'Индекс бита с ошибкой: {sum(errors)}')
        #output = inp[:index] + str(0) + inp[index + 1:] if inp[index] == '1' else inp[:index + 1] + str(1) + inp[index:]
        output = inp[:index] + str(0) + inp[index + 1:] if inp[index] == '1' else inp[:index] + str(1) + inp[index + 1:]
        print(f'Исправленная последовательность: {output}\n')
        return output


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

def divider(stream, count, side):
    blocks = []
    temp = ''
    for index in range(len(stream)):
        if index % count != 0 or index == 0:
            temp += stream[index]
        else:
            blocks.append(temp)
            temp = stream[index]
    if side == 'right':
        temp += '0' * (count - len(temp))
    else:
        temp = '0' * (count - len(temp)) + temp
    blocks.append(temp)
    return blocks


def zipfile():
    print('---Сохранение файла в коде---')
    # Сохранение файла в коде
    encoded_blocks = ''
    for block in blocks:
        inp = block
        zipped = zip(inp)
        encoded_blocks += zipped
        ZIPPED.append(zipped)
    #print(encoded_blocks)
    bytesarr = divider(encoded_blocks, 8, 'left')
    print(bytesarr)
    text = ''
    for byte in bytesarr:
        text += chr(int(byte, 2))
    print(text)

    file = open(FILE_PATH.split('.')[0] + '_ENCODED.txt', 'w', encoding='utf-8')
    file.write(text)
    file.close()
    print()

def damagefile():
    print('---Сохранение файла в коде с ошибками---')
    # Сохранение файла в коде с ошибками
    damaged_blocks = ''
    indexes = []
    for block in ZIPPED:
        inp = block
        damaged, index = doerror(block)
        damaged_blocks += damaged
        indexes.append(index)
        DAMAGED.append(damaged)
    print(DAMAGED)
    print(indexes)
    bytesarr = divider(damaged_blocks, 8, 'left')
    print(bytesarr)
    text = ''
    for byte in bytesarr:
        text += chr(int(byte, 2))
    print(text)

    file = open(FILE_PATH.split('.')[0] + '_DAMAGED.txt', 'w', encoding='utf-8')
    file.write(text)
    file.close()
    print()

def unzipfile():
    print('---Чтение, исправление и схранение файла---')
    # Чтение, исправление и схранение файла
    unzipped_blocks = ''
    for block in DAMAGED:
        inp = block
        unzipped = unzip(block)
        unzipped_blocks += unzipped
        UNZIPPED.append(unzipped)
    print(unzipped_blocks)
    bytesarr = divider(unzipped_blocks, 8, 'left')
    print(bytesarr)
    text = ''
    for byte in bytesarr:
        text += chr(int(byte, 2))
    print(text)

    file = open(FILE_PATH.split('.')[0] + '_UNZIPPED.txt', 'w', encoding='utf-8')
    file.write(text)
    file.close()
    print()

FILE_PATH = 'example.txt'
ZIPPED = []
DAMAGED = []
UNZIPPED = []

if __name__ == '__main__':
    stream = getbits(FILE_PATH)
    print(f'Битовый поток:\n{stream}')
    # Деление на блоки
    blocks = divider(stream, 11, 'right')
    print(f'Блоки:\n{blocks}\n')

    zipfile()
    damagefile()
    unzipfile()


    '''
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


