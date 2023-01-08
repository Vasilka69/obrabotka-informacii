def printm(mas):
    print('---')
    for i in mas:
        print(i)
    print('---')


def encoder(text):
    print(f'Исходный текст: {text}')
    n = len(text)
    print(f'Длина текста: {n}')
    #c = ['']
    N = 0
    dictionary = ['']
    while N < n:
        print(f'N = {N}')
        temp = text[N]
        l = 1
        while dictionary.__contains__(temp):
            if N + l < n:
                temp += text[N+l]
                l += 1
            else:
                break
        dictionary.append(temp)
        #l = len(temp)
        if l != 1:
            l -= 1
        N += l
        #N += 1
        #c += 1
    printm(dictionary)


def main():
    text = 'IF_WE_CANNOT_DO_AS_WE_WOULD_WE_SHOULD_DO_AS_WE_CAN'
    encoder(text)


if __name__ == '__main__':
    main()