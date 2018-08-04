import math


def euler1(n):
    base = 1
    return (base + 1/n) ** n


def euler2(n):
    base = 1
    return (base/n + base) ** n
# for i in range(n):
    #     base = base


def euler3(n):
    base = 1
    return (base+n) ** (1/n)


def euler4(n):
    summ = 0
    for i in range(n):
        summ += 1/math.factorial(i)
    return summ


def euler5(n):
    base = 1
    for i in range(n):
        base = base + (base * 1/n)
    return base


print(
    euler5(100)
)




































