def RAlg():
    Input = ['503', '087', '512', '061', '908', '170', '897', '275',
             '653', '426', '154', '509', '612', '677', '765', '703']
    maxradix = int(len(max(Input)))
    for radix in range(maxradix):
        currRadixList = []
        for i in Input:
            currRadixList.append(i[len(i) - radix - 1])
        maxCurrRadix = int(max(currRadixList))

        stackArr = [[]  for _ in range(maxCurrRadix + 1)]
        for i in Input:
            stackArr[int(i[len(i) - radix - 1])].append(i)
        Input = [j for i in stackArr for j in i]
    print(Input)

def SAlg():
    R = [13, 32, 23, 53, 15, 345, 435, 12, 24]
    K = 15
    for i in R:
        if i == K:
            print(f'Элемент с ключом K = {K} найден')
            return True
    print(f'Элемент не найден')
    return False


def DopSort():
    inp = [5, 4, 3, 2]
    temp = []
    for i in range(0, len(inp), 2):
        if inp[i] > inp[i+1]:
            temp.append([inp[i+1], inp[i]])
        else:
            temp.append([inp[i], inp[i+1]])
    print(temp)

def main():
    #RAlg()
    #SAlg()
    DopSort()

if __name__ == '__main__':
    main()
