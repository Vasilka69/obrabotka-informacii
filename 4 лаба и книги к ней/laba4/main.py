import math as mat

def A(n: int, m, k, a):
    print()

def main():
    a = int(9)  # Число, корень которого нужно найти
    print(f'a = {a}')
    m = 1
    q = 3  # Нечетное
    pminus = (2 ** m) * q  # Четное
    while pminus <= a:
        m += 1
        pminus = (2 ** m) * q
    p = pminus + 1 # 7 Нечетное простое
    print(f'p = {p}, m = {m}, q = {q}')

    Zp = []
    for i in range(p):
        Zp.append(i)
    print(f'Zp = {Zp}')
    b = (int(mat.sqrt(p)) + 1) ** 2
    print(f'b = {b}')

    # a = 4
    # k = 0
    # m = 1
    # q = 3
    # pminus = 6
    # p = 7

    A = [a]
    K = []
    # ipow2 = 2
    # i = int(0)
    k = int(-1)
    print(a**((2**k)*q) % p)
    while k != 0:
        k = 0
        ipow2 = 1
        #while a**((2**k)*q) % p != 1:
        while (a ** ((ipow2) * q)) % p != 1:
            print(k)
            # print(f'prepreres = {((ipow2) * q)}')
            # print(f'preres = {(a ** ((ipow2) * q))}')
            # print(f'res = {(a ** ((ipow2) * q)) % p}')
            k += 1
            ipow2 *= 2
        K.append(k)
        if k != 0:
            a = A[len(A) - 1] * b**(2**(m-k)) % p
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