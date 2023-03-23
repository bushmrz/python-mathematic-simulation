from math import exp
import matplotlib.pyplot as plt


def f1(t):
    return 4 * exp(-t) - exp(2 * t)  # точное решение задачи Коши
    # return exp(2 * t) + 1


def g1(t):
    return exp(-t) - exp(2 * t)  # точное решение задачи Коши
    # return 2*exp(2*t)


def f2( x, y):
    return -2 * x + 4 * y  # производная
    # return y


def g2(x, y):
    return -x + 3 * y  # производная
    # return 2*y


# метод Рунге-Кутта 4-го порядка
def runge_kutta_4(a, b, n, h, x0, y0, f, g):
    x, y = [0] * (n + 1), [0] * (n + 1)
    x[0], y[0] = x0, y0
    for i in range(1, n + 1):
        k1 = h*f(x[i - 1], y[i - 1])
        L1 = h*g(x[i - 1], y[i - 1])
        k2 = h*f(x[i - 1] + h * 0.5, y[i - 1] + k1 / 2)
        L2 = h*g(x[i - 1] + h * 0.5, y[i - 1] + L1 / 2)
        k3 = h*f(x[i - 1] + h * 0.5, y[i - 1] + k2 / 2)
        L3 = h*g(x[i - 1] + h * 0.5, y[i - 1] + L2 / 2)
        k4 = h*f(x[i - 1] + h, y[i - 1] + k3)
        L4 = h*g(x[i - 1] + h, y[i - 1] + L3)
        x[i] = x[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y[i] = y[i - 1] + (L1 + 2 * L2 + 2 * L3 + L4) / 6
    return x, y


a, b = 0, 3
n = 10
h = (b - a) / n
x0, y0 = 3, 0  # начальное условие

t1, x1, y1 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(n + 1):
    t1[i] = a + i * h
    x1[i] = f1(t1[i])
    y1[i] = g1(t1[i])

x2, y2 = runge_kutta_4(a, b, n, h, x0, y0, f2, g2)

plt.title('Приближённые решения задачи Коши и точные решения этой задачи')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
# plt.xlim(-100, 10)
# plt.ylim(-100, 10)
# plt.plot(t1, x1, label='Точное решение 1')
# plt.plot(t1, y1, label='Точное решение 2')
# plt.plot(t2, x2, '--', label='Приближённое решение 1')
# plt.plot(t2, y2, '--', label='Приближённое решение 2')
plt.plot(x2, y2, '--', label='Приближённое решение')
plt.plot(x1, y1, label='Точное решение', alpha = 0.5)

plt.legend()
plt.show()
