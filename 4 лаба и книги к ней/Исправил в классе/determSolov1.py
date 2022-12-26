import math

def isPrime(a):
    return all(int(a) % i for i in range(2, int(a)))


# def factorize(n):
#     factors = []
#
#     p = 2
#     while True:
#         while n % p == 0 and n > 0:  # while we can divide by smaller number, do so
#             factors.append(p)
#             n = n / p
#         p += 1  # p is not necessary prime, but n%p == 0 only for prime numbers
#         if p > n / p:
#             break
#     if n > 1:
#         factors.append(n)
#     return factors


# def calculateLegendre(a, p):
#     if a >= p or a < 0:
#         print("_1_")
#         print(calculateLegendre(a % p, p))
#         return calculateLegendre(a % p, p)
#     elif a == 0 or a == 1:
#         print("_2_")
#         print(a)
#         return a
#     elif a == 2:
#         if p % 8 == 1 or p % 8 == 7:
#             print("_3_")
#             print("1")
#             return 1
#         else:
#             print("_4_")
#             print("-1")
#             return -1
#     elif a == p - 1:
#         if p % 4 == 1:
#             print("_5_")
#             print("1")
#             return 1
#         else:
#             print("_6_")
#             print("-1")
#             return -1
#     elif not isPrime(a):
#         factors = factorize(a)
#         product = 1
#         for pi in factors:
#             product *= calculateLegendre(pi, p)
#         print("_7_")
#         print(product)
#         return product
#     else:
#         if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
#             print("_8_")
#             print(calculateLegendre(p, a))
#             return calculateLegendre(p, a)
#         else:
#             print("_9_")
#             print((-1) * calculateLegendre(p, a))
#             return (-1) * calculateLegendre(p, a)

flag1 = False
def calculateLegendre1(a, p):

    for i in range(max(a, p)):
        if a % p == i**2:
            flag1 == True


    if a % p == 0:
        return 0

    if flag == True and a % p != 0:
        return 1

    if flag1 == False:
        return -1


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


flag = False

n = int(input("Введите число : "))

for a in range(1, n):
    if gcd(a, n) == 1:
        # print(a, n)
        if int(math.pow(a, ((n-1)/2)) % n) == int(calculateLegendre1(a, n) % n):
            # print((math.pow(a, ((n-1)/2)) % n))
            # print((calculateLegendre1(a, n) % n))
            # print('сравнение 2 выполняется')
            flag = True
    else:
        flag = False
        break


if flag == False:
    print("N — составное")
else:
    print("N — простое")
