import math as mat
import random


def A(n: int, m, k, a):
    print()

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

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
    pminus = (2 ** m) * q  # 20 Четное
    p = pminus + 1 # 21 7 Нечетное простое
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
    # a = int(0)
    a = int(16)
    while (calculateLegendre(a, p) != 1 and gcd(a, p) != 1):
        print(f'Число a подобрано неправильно')
        a = a
        #a = random.randint(1, p)
    print(f'Число a подобрано правильно')
    print(f'a = {a}')

    #b = int(0)
    b = 12
    while (calculateLegendre(b, p) != -1):
        return
        b = random.randint(0, p)
    print(f'Число b подобрано правильно')
    print(f'b = {b}')

    A = [a]
    K = []
    k = int(-1)
    while k != 0:
        a = A[len(A) - 1]
        k = 0
        #while a**((2**k)*q) % p != 1:
        #while (a ** ((ipow2) * q)) % p != 1:
        #while (a % p)** (ipow2 * q) != 1:
        #res = pow(a,2**k * q, p) # a^(b mod c - 1) mod c
        #res = a ** (2**k * q % (p - 1)) % p
        res = int()
        while res != 1:
            #print(k)
            #res = pow(a,2**k * q, p)
            #res = a ** ( 2**k * q % (p - 1)) % p
            res = a**((2**k)*q) % p
            print(res)
            k += 1
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