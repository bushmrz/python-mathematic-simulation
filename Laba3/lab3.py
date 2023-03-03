import matplotlib.pyplot as npt
from shuffle_page import *


def square(x, n):  # квадрат
    li = list()
    for i in range(n):
        x = pow(x, 2)
        x = x // 100
        x = x % 10000
        li.append(x / 10000)
    return (li)


def product(x, y, n):  # произведение
    li = list()
    for i in range(n):
        prod = x * y
        y = prod % 10000
        sl = (prod // 100) % 10000
        li.append(sl / 10000)
    return (li)


def multiplicative(x, l, m, n):  # Метод перемешивания
    li = list()
    x1 = x
    for i in range(n):
        x = (x1 * l) % m
        x1 = x
        li.append(x1 / 10000)
    return (li)


def modification(x, l, u, m, n):  # Линейный конгруэнтный метод
    li = list()
    x1 = x
    for i in range(n):
        x = ((x1 * l) + u) % m
        x1 = x
        li.append(x1 / m)
    return (li)


p1 = (square(7153, 10000))
p2 = (product(5167, 3729, 10000))
#p3 = (multiplicative(1357, 1357, 5689, 100))
p3 = (shuffle_meth())
#p4 = (modification(1357, 1357, 3459, 1113, 100))
p4 = (modification(1220703125,7, 7, (2**31)-1, 10000))

title1 = npt.suptitle('Метод серединных квадратов')
npt.hist(p1)
npt.show()
title2 = npt.suptitle('Метод серединных произведений')
npt.hist(p2)
npt.show()
# title3 = npt.suptitle('Метод перемешивания')
# npt.hist(p3)
# npt.show()
title4 = npt.suptitle('Линейный конгруэнтный метод')
npt.hist(p4)
npt.show()

# npt.bar(range(100), p1)
# npt.show()
# npt.bar(range(100), p2)
# npt.show()
# npt.bar(range(100), p3)
# npt.show()
# npt.bar(range(100), p4)
# npt.show()
