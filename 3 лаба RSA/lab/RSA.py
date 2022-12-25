import math
import random
import sympy

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ost(m, e, n):
    #ищет math.pow(m, e) % n
    temp = m
    for i in range(1, int(e)):
        # print(f'{i+1}) {temp} * {m} = {temp * m} mod {n} ({(temp * m) % n})')
        temp = (temp * m) % n
    return temp

    
def RSA():
    E_list = []
    #p = int(input("Введите p: "))
    #q = int(input("Введите q: "))
    p = int(7)
    q = int(11)
    if (sympy.isprime(p) and sympy.isprime(q)) == False:
        print("p или q не простые числа")
        return

    n = q * p # n - Модуль
    print(f"n = {n}")
    f = (p - 1)*(q - 1) # Функция Эйлера
    print(f"f = {f}")
    for e in range(2, f):
        if gcd(f, e) == 1:
            E_list.append(e) # Все взаимнопростые со значением функции Эйлера
    # print("все возможные e = {0}".format(E_list))
    r_index = random.randint(0, len(E_list))
    e = E_list[r_index]
    print(f"e = {e}") #  e - Открытая экспонента - случайное из списка взаимнопростых
    d = 0.1
    k = 1
    while (float(d).is_integer() == False):
        d = (k * f + 1) / e
        k += 1
    print(f"d = {int(d)}") # d - Мультипликативное обратное к числу e (закрытая экспонента)

    m = int(input("Введите m (сообщение для шифрования): ")) # Сообщение для шифрования
    c = ost(m, e, n)
    print(f"c (зашифрованное сообщение) = {int(c)}")
    d = int(input("Введите d (закрытый ключ получателя): "))

    # (e, n) - Открытый ключ
    # (d, n) - Закрытый ключ
    #print(f"c = {int(c)}")
    # m1 = math.pow(c, d) % n
    m1 = ost(c, d, n)
    print(f"Расшифрованное сообщение: {int(m1)}")
    if (m == m1):
        print('Расшифрование выполнено успешно')
    else:
        print('Расшифрование выполнено некорректно')

RSA()