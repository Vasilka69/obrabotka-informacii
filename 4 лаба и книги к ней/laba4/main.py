import math as mat
import random


def A(n: int, m, k, a):
    print()


def calculateLegendre(a, p):
    a1 = a % p
    if a1 == 0:
        return 0
    else:
        for i in range(1, p-1):
            if i**2 % p == a1:
                return 1
        return -1

def main():
    m = 2
    q = 5  # Нечетное
    pminus = (2 ** m) * q  # Четное
    p = pminus + 1 # 7 Нечетное простое
    print(f'p = {p}, m = {m}, q = {q}')

    Zp = []
    for i in range(p):
        Zp.append(i)
    print(f'Zp = {Zp}')
    '''
    a = int(9)  # Число, корень которого нужно найти
    print(f'a = {a}')
    if (calculateLegendre(a, p) == 1):
        print(f'Число a подобрано правильно')
    else:
        return
    '''
    a = int(0)
    while (calculateLegendre(a, p) != 1):
        a = random.randint(10, p)
    print(f'Число b подобрано правильно')
    print(f'a = {a}')

    b = int(0)
    while (calculateLegendre(b, p) != -1):
        b = random.randint(0, p)
    print(f'Число b подобрано правильно')
    print(f'b = {b}')

    A = [a]
    K = []
    k = int(-1)
    while k != 0:
        k = 0
        #ipow2 = 1
        #while a**((2**k)*q) % p != 1:
        #while (a ** ((ipow2) * q)) % p != 1:
        while pow(a,(2**k * q), p) != 1:
        #while (a % p)** (ipow2 * q) != 1:
            print(k)
            k += 1
            #ipow2 *= 2
        K.append(k)
        if k != 0:
            a = A[len(A) - 1] * b**(2**(m-k)) % p
        A.append(a)
        print(f'k = {k}')
    #print(K)
    R = []
    rn = A[len(A) - 1] ** ((q + 1) / 2) % p
    R.append(rn)
    for i in range(len(A), 0):
        print(i)
        ri = rn * (b**(2**(m-K[i]-1)))**(-1) % p
        R.append(ri)
        rn = ri
    x0 = R[len(R) - 1]
    print(f'Корень из a = {x0}')
    '''
    while k != 0:
        print(i)
        ipow2 *= 2
        if (a**(ipow2 * q)) % p == 1:
            k = i
            K.append(k)
            print('ki = ', i)
        print('ki = ', i)
        i += 1
    print(f'\nk = {K}\n')
    '''
    #print(f' = {}')


if __name__ == '__main__':
    main()