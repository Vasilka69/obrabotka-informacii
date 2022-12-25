
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
    else:
        print(f'Контрольные биты с ошибкой: {errors}')
        # Исправление
        index = sum(errors) - 1
        print(f'Индекс бита с ошибкой: {sum(errors)}')
        output = inp[:index] + str(0) + inp[index + 1:] if inp[index] == '1' else inp[:index + 1] + str(1) + inp[index:]
        print(f'Исправленная последовательность: {output}')

if __name__ == '__main__':
    inp = str('10110111001')
    code = zip(inp)
    print()
    code = str('001001100111001')
    #code = str('001001101111001') # С ошибкой
    code = str('001001100111101')  # С ошибкой
    unzip(code)

