import math
import numpy as np
import matplotlib.pyplot as plt
import numpy.random
import math
import random
from scipy import integrate

# номер варианта и число точек
n_var = 11
n_dots = 2000
# n_dots = 179

# коэффициенты
A = n_var
B = n_var - 10
# A = 3
# B = 7


# функция полярности
def polar(fi):
    p = math.sqrt(abs(A * math.cos(fi) * math.cos(fi) + B * math.sin(fi) * math.sin(fi)))
    return p

def polar_sqrt(fi):
    return abs(A * math.cos(fi) * math.cos(fi) + B * math.sin(fi) * math.sin(fi))

# функция для окружности
def polar_dots(fi):
    x_polar = polar(fi) * math.cos(fi)
    y_polar = polar(fi) * math.sin(fi)
    return x_polar, y_polar


# функция для fi
def fir(x, y):
    if x > 0:
        result = math.atan(y / x)
    elif x < 0:
        result = math.atan(y / x) + math.pi
    elif y > 0:
        result = math.pi / 2
    elif y < 0:
        result = -math.pi / 2
    else:
        result = 0
    return result


# функция для ri
def rif(x, y):
    return math.sqrt(x * x + y * y)


# точки кривой
x_dots = []
y_dots = []
i = 0
i_arr = []
i_arr.append(0)

while i <= 2 * math.pi:
    x1, y1 = polar_dots(i)
    x_dots.append(x1)
    y_dots.append(y1)
    i += math.pi / 24
    i_arr.append(i)

plt.plot(x_dots, y_dots, '-', markersize=2, color='b')

# определили границы
a = 4.3
b = 2.5

# генерируем случайные точки
x_gen = []
y_gen = []
for i in range(0, n_dots):
    x_gen.append(random.uniform(-a, a))
    y_gen.append(random.uniform(-b, b))

# точки внутри фигуры
x_inside = []
y_inside = []

# точки вне фигуры
x_outside = []
y_outside = []

# по условию определяем точки внутри/снаружи фигуры
for i in range(0, n_dots):
    if rif(x_gen[i], y_gen[i]) < polar(fir(x_gen[i], y_gen[i])):
        x_inside.append(x_gen[i])
        y_inside.append(y_gen[i])
    else:
        x_outside.append(x_gen[i])
        y_outside.append(y_gen[i])

# строим точки на графике
plt.plot(x_inside, y_inside, 'ro', markersize=2, color='g')
plt.plot(x_outside, y_outside, 'ro', markersize=2, color='r')

# находим кол-во точек внутри фигуры и площадь
M = len(x_inside)
S = round((M / n_dots) * a * b * 4, 2)
s_real, err = integrate.quad(polar_sqrt, 0, 2*math.pi)
s_real = round(s_real/2,2)
# вывод графика
plt.title('Кол-во точек внутри фигуры = ' + str(M) + '\nПлощадь фигуры = ' + str(S) + '\n Точная площадь = ' + str(s_real))
plt.show()

