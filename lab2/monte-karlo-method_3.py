import math
import matplotlib.pyplot as plt
import random

# номер варианта и число точек
R = n_var = 11
n_dots = 2000

# размеры квадрата по условию
x_max = 2 * n_var
y_max = 2 * n_var

# точки внутри фигуры
x_inside = []
y_inside = []

# точки вне фигуры
x_outside = []
y_outside = []

# точки окружности
x_dots = []
y_dots = []

x_gen = []
y_gen = []
def f_circle(fi):
    x_circle = -R + R * math.cos(fi)
    y_circle = R + R * math.sin(fi)
    return x_circle, y_circle

i = 0
while i <= 2 * math.pi:
    x1, y1 = f_circle(i)
    x_dots.append(x1)
    y_dots.append(y1)
    i += math.pi / 24

plt.plot(x_dots, y_dots, '-', markersize=2, color='b')


for i in range(0, n_dots):
    x_gen.append(random.uniform(-2 * R, 0))
    y_gen.append(random.uniform(0, 2 * R))

for i in range(0, n_dots):
    if ((x_gen[i] + R) * (x_gen[i] + R)) + ((y_gen[i] - R) * (y_gen[i] - R)) < (R * R):
        x_inside.append(x_gen[i])
        y_inside.append(y_gen[i])
    else:
        x_outside.append(x_gen[i])
        y_outside.append(y_gen[i])

plt.plot(x_inside, y_inside, 'ro', markersize=2, color='g')
plt.plot(x_outside, y_outside, 'ro', markersize=2, color='r')

M = len(x_inside)
PI = round(4 * M / n_dots, 2)

# вывод графика
plt.title('Кол-во точек внутри окружности = ' + str(M) + '\nПолученное значение pi = ' + str(PI))
plt.show()

