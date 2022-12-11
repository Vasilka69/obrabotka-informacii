
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Eulersfunc(n: int):
    nums = []
    for i in range(2, n):
        if float(n / i) % 1 != 0:
            nums.append(i)
            print(i)
    return nums

def spisok():
    m = int(27)
    e = int(13)
    n = int(33)
    temp = int(m)
    for i in range(1, e):
        print(f'{i + 1}) {temp} * {m} = {temp * m} mod {n} ({(temp * m) % n})')
        temp = (temp * m) % n

def main():
    nums = Eulersfunc(10)
    print(nums)


if __name__ == '__main__':
    main()