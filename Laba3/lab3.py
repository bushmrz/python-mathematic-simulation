import matplotlib.pyplot as npt
from shuffle_page import *
import pandas as pd

n = 100
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


p1 = (square(7153, n))
p2 = (product(5167, 3729, n))
p3 = (shuffle_meth())
p4 = (modification(1220703125,7, 7, (2**31)-1, n))


npt.xlim(0.0, 1.0)

df1 = pd.DataFrame(p1)
df2 = pd.DataFrame(p2)
df4 = pd.DataFrame(p4)




title1 = npt.suptitle('Метод серединных квадратов')
#df1['random'].hist(bins=10)
npt.hist(p1, bins=10)
#npt.hist(p1)
npt.show()
title2 = npt.suptitle('Метод серединных произведений')
npt.hist(p2, bins=10)
#npt.hist(p2)
npt.show()

title4 = npt.suptitle('Линейный конгруэнтный метод')
npt.hist(p4, bins=10)
#npt.hist(p4)
npt.show()

#p3 = (multiplicative(1357, 1357, 5689, 100))
#p4 = (modification(1357, 1357, 3459, 1113, 100))
# title3 = npt.suptitle('Метод перемешивания')
# npt.hist(p3)
# npt.show()
#npt.bar(range(100), p1)
# npt.show()
# npt.bar(range(100), p2)
# npt.show()
# npt.bar(range(100), p3)
# npt.show()
# npt.bar(range(100), p4)
# npt.show()
