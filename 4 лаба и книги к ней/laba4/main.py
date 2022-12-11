def A(n: int, m, k, a):
    print()

def main():
    m = 1
    q = 4 # Нечетное
    pminus = (2**m)*q # 12
    p = pminus + 1 # Нечетное простое 13
    print(f'p = {p}')
    Zp = []
    for i in range(p):
        Zp.append(i)
    print(f'Zp = {Zp}')
    a = int(p)
    b = -p
    A = [a]
    K = []
    k = int(-1)
    ipow2 = 2
    i = int(0)
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





if __name__ == '__main__':
    main()