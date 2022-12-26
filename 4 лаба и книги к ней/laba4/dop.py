import math as mat
import random


def A(n: int, m, k, a):
    print()

def gcd(a, b):
    while b:
        a, b = b, a%b
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

def MillerRabinTest(num, k = 40):
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

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    n = int(5)
    B = 5
    # Шаг 1
    min = 10 ** (n - 1)
    max = (10 ** (n)) - 1
    print(f'min = {min}')
    print(f'max = {max}')
    x = random.randint(min, max - 1)
    t = random.randint(1, max - min)
    while x + t > max:
        t = random.randint(1, max - min)
    print(f'x = {x}')
    print(f't = {t}')
    print(f'x+t = {x+t}')
    # Шаг 2
    Otrezok = list(range(x, x+t+1)) # Правильная ли длина
    primes = getAllPrimes(B)
    print(primes)
    for num in Otrezok:
        for prime in primes:
            if (num % prime == 0):
                Otrezok.remove(num)
                print(f'1 Удалено) {num}')
                break
    # Шаг 3
    print('Шаг 3')
    for num in Otrezok:
        if (not MillerRabinTest(num, k = 100)):
            Otrezok.remove(num)
            print(f'2 Удалено) {num}')
    # Шаг 4



if __name__ == '__main__':
    main()