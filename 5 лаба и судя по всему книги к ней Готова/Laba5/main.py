import math as m

def isPrime(N):
    sqr = m.ceil(m.sqrt(N))
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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def getAllDividers(n):
    res = []
    for i in range(n, 1, -1):
        if (n % i == 0):
            res.append(i)
    return res

def determ(N):
    A = [a for a in range(1, N)]
    #print(N, end=') ')
    for a in A:
        check = False
        d = gcd(a, N)
        if d > 1:
            #print('N - составное')
            return
        elif d == 1:
            if a**(N-1) % N != 1:
                #print('N - составное')
                return
            else:
                divs = getAllDividers(N-1)
                for div in divs:
                    if a**((N-1) / div) % N == 1:
                        check = True
                        break
                if check:
                    continue
                #print('N - простое')
                return N
    #print('N - составное')
    return

def Lucas(N):
    for a in range(1, N):
        check = False
        if gcd(a, N) != 1:
            continue
        if a**(N-1) % N != 1:
            continue
        divs = getAllDividers(N-1)
        if len(divs) == 0:
            return True
        for div in divs:
            if a**((N-1)/div) % N == 1:
                check = True
                break
        if check:
            continue
        return True
    return False

def main():
    N = 50
    #isPrime(N) # 1
    #determ(N) # 2
    #Lucas(N) # 3
    primes1 = []
    for i in range(N):
        #print(f'{i}) ', end='')
        if isPrime(i):
            primes1.append(i)
    print(primes1)

    primes2 = []
    for i in range(N):
        res = determ(i)
        if res != None:
            primes2.append(res)
    print(primes2)

    primes3 = []
    for i in range(N):
        if Lucas(i):
            primes3.append(i)
    print(primes3)

main()