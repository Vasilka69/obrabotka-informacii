import math as mat

def A(n: int, m, k, a):
    print()

def main():
    m = 1
    q = 3 # Нечетное    x =2,4,6
    pminus = (2**m)*q # 6  2*x + 1 = p
    p = pminus + 1 # 7 Нечетное простое
    print(f'p = {p}')
    a = int(4) # x^2 = 4

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
    k = int(0)
    print(a**((2**k)*q) % p)
    while a**((2**k)*q) % p != 1:
        k += 1
    K.append(k)

    R = []
    rn = a**((q+1)/2) % p
    R.append(rn)
    for i in range(len(A), 0):
        print(i)
        ri = rn * (b**(2**(m-K[i]-1)))**(-1) % p
        R.append(ri)
        ri = rn
    x0 = R[len(R) - 1]
    print(x0)
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