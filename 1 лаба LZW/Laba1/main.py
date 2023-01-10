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

    table = [0] * 5

    table[0] = list(['Шаг', 0])
    table[1] = list(['Словарь', ''])
    table[2] = list(['Номер слова', '-'])
    table[3] = list(['Кодовые символы', '-'])
    table[4] = list(['Затраты (бит)', '-'])

    c = 1
    N = 0
    dictionary = ['']
    while N < n:
        #print(f'N = {N}')
        table[0].append(c)
        temp = text[N]
        #temp = ''
        l = 1
        while dictionary.__contains__(temp): # Переписать через фор
            if N + l < n:
                temp += text[N+l]
                l += 1
            else:
                break
        dictionary.append(temp)
        table[1].append(temp)
        '''
        table[2].append(temp)
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