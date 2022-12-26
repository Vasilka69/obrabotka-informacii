import math
import math as mat
import random


def A(n: int, m, k, a):
    print()


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def getAllPrimes(n):
    N = []
    for i in range(2, n + 1):
        if IsPrime(i):
            N.append(i)
    return N


def MillerRabinTest(num, k=40):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    s = 0
    t = num - 1
    while t % 2 == 0:
        s += 1
        t //= 2

    for _ in range(k):
        a = random.randint(2, num - 1)
        x = pow(a, t, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == 1:
                return False
            if x == num - 1:
                break
    return True


def getAllDividers(n):
    res = []
    for i in range(n, 1, -1):
        if (n % i == 0):
            res.append(i)
    return res


def is_prime(N): # Методом пробных делений
    sqr = mat.ceil(mat.sqrt(N))
    if N == 0 or N == 1:
        return
    elif N <= 2:
        #print(f'Число {N} является простым')
        return True
    for i in range(2, sqr + 1):
        if N % i == 0:
            #print(f'Число {N} не является простым')
            return False
    #print(f'Число {N} является простым')
    return True


def main():
    n = int(3)
    B = 5
    # Шаг 1
    min = 10 ** (n - 1)
    max = (10 ** (n)) - 1
    print(f'min = {min}')
    print(f'max = {max}')
    x = random.randint(min, max - 1)
    #t = random.randint(1, max - min)
    #t = random.randint(1, int((max - min) * 0.001))
    #t = random.randint(1, int((max - min) * 0.1 ** (n-3)))
    t = random.randint(1, math.ceil(mat.sqrt(max - min)))
    while x + t > max:
        t = random.randint(1, max - min)
    print(f'x = {x}')
    print(f't = {t}')
    print(f'x+t = {x + t}')
    # Шаг 2
    Otrezok = list(range(x, x + t + 1))  # Вроде правильная длина
    primes = getAllPrimes(B)
    print(f'Простые числа <= B{primes}')
    for num in Otrezok:
        for prime in primes:
            if (num % prime == 0):
                Otrezok.remove(num)
                print(f'1 Удалено) {num}')
                break
    # Шаг 3
    print('Шаг 3')
    for num in Otrezok:
        if (not MillerRabinTest(num, k=100)):
            Otrezok.remove(num)
            print(f'2 Удалено) {num}')
    # Шаг 4
    for num in Otrezok:
        if (is_prime(num)):
            print(f'Простое число найдено: {num}')
            #break


if __name__ == '__main__':
    main()
