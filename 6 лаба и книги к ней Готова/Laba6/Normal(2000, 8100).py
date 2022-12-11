import math as m

nu = 2000
sigma2 = 8100

def N(t):#, nu, sigma):
    # nu - мат. ожидание
    # sigma - дисперсия (насколько в среднем отклоняется)
    # sqrt(sigma) - среднее квадратич отклонение
    return (m.exp(((t - nu)**2) / (- 2 * sigma2))) / (m.sqrt(sigma2 * 2 * m.pi))

def f(x):
    return N(x)#, nu, sigma)

def integral(left, right, h):
    sum = float()
    i = float(left)
    while(i <= right):
        sum += f(i) * h
        i += h
    return sum

def Mf(x):
    return x*f(x)

def M():
    left = 0
    right = 10000
    h = 0.1
    sum = float()
    i = float(left)
    while(i <= right):
        sum += Mf(i) * h
        i += h
    return sum

def Df(x):
    return x**2 * f(x)
    #return ((x - Mf(x)) ** 2) * f(x)

def D():
    left = 0
    right = 10000
    h = 0.01
    sum = float()
    i = float(left)
    while(i <= right):
        sum += Df(i) * h
        i += h
    return sum - M()**2

def main():
    #print(N(2000, 8100))
    '''
    a = 1
    b = 2
    n = 50
    width = float(m.fabs(a-b) / n)
    print(integral(a, b, width))
    print(f(2000))
    '''
    print(f'Вероятность распределения = {integral(-1000, 2000, 0.01)}')
    delta = 100
    #print(f'Плотность распределения = {integral(0, 10000, 0.01)}')
    print(f'Плотность распределения = {integral(nu - delta, nu + delta, 0.01)}')
    print(f'M = {M()}')
    Disp = D()
    print(f'D = {Disp}')
    sigm = m.sqrt(Disp)
    print(f'Sigma = {sigm}')



main()