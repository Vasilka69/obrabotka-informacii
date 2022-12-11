import math
import random
import sympy


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ost(m, e, n):
    # ищет math.pow(m, e) % n
    temp = m
    for i in range(1, int(e)):
        # print(f'{i+1}) {temp} * {m} = {temp * m} mod {n} ({(temp * m) % n})')
        temp = (temp * m) % n
    return temp


def RSA():
    E_list = []
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    if sympy.isprime(p) and sympy.isprime(q):
        n = q * p
        print("n = {0}".format(n))
        f = (p - 1) * (q - 1)
        print("f = {0}".format(f))
        # e = int(input("Введите e удовлетворяющее условию: 1<e<f : "))
        for e in range(2, f):
            if gcd(f, e) == 1:
                E_list.append(e)
        # print("все возможные e = {0}".format(E_list))
        r_index = random.randint(0, len(E_list))  # находятся все подходящие е и из них выбирается одно рандомное
        e = E_list[r_index]
        print("e = {0}".format(e))
        d = 0.1
        k = 1
        while (float(d).is_integer() == False):
            d = (k * f + 1) / e
            k += 1
        print("d = {0}".format(int(d)))

    else:
        print("p или q не простые числа")

    m = int(input("Введите m: "))
    # c = math.pow(m, e) % n
    c = ost(m, e, n)
    print("c = {0}".format(int(c)))
    # m1 = math.pow(c, d) % n
    m1 = ost(c, d, n)
    print("m1 = {0}".format(int(m1)))


RSA()