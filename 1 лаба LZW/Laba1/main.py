import math as m

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

                if i != 0  and j > 2 and len(str(mas[j][i])) >= 4:
                        print('', end='\t')
                if i != 0  and j > 3 and len(str(mas[j][i])) >= 4:
                        print('', end='\t')

                print(mas[j][i], end='\t\t')
            except:
                print(' ', end='')
        print()
    print('---')


def encoder(text):
    print(f'Исходный текст: {text}')
    n = len(text)
    print(f'Длина текста: {n}')
    esc = '#'
    dictionary = [esc]

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
        #temp = ''
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
        for j in range(len(dictionary) - 1):
            if dictionary[j] == esc + find or dictionary[j] == find:
                num = j
                wordfound = True
        if N == 0:
            table[3].append('')
        else:
            count = m.ceil(m.log2(c - 1))
            if num != 0:
                count -= len(str(bin(c))[2:])
            table[3].append('0' * count)
        if N == 2:
            print(str(bin(num))[2:])
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
        '''
        table[3].append(temp)
        table[4].append(temp)
        '''
        if l != 1:
            l -= 1
        N += l
        #N += 1
        c += 1

    printm2d(table)
    #printm(dictionary)



def main():
    text = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    encoder(text)


if __name__ == '__main__':
    main()