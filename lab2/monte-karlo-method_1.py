import matplotlib.pyplot as plt
import random
from scipy import integrate
from matplotlib.widgets import TextBox

arr_y21 = []
arr_y22 = []
arr_x = []

#
x_inside = []
y_inside = []

#
x_outside = []
y_outside = []

n = 11
x_max = 20.9
y_max = 42
M = S = 0
expression = 10000

fig, ax = plt.subplots()


def f(x):
    result_1 = (10 * x) / n
    result_2 = 10 * ((x - 20) / (n - 20)) + 20
    return result_1, result_2


def rand_point(x1, y1, x2, y2):
    x = random.uniform(x1, x2)
    y = random.uniform(y1, y2)
    return x, y


def submit(expression):
    ax.clear()
    draw_graph(arr_x, arr_y21, arr_y22)
    arr_xx = []
    arr_yy = []
    for i in range(int(expression)):
        x,y = rand_point(0,0,21,42)
        arr_xx.append(x)
        arr_yy.append(y)

    draw_points(arr_xx, arr_yy)
    M = len(x_inside)
    print(M)
    S = round((M / int(expression)) * (x_max * y_max), 2)
    print(S)
    S_real = round(y_max / 2 * x_max, 2)
    fig.suptitle("Кол-во точек внутри треугольника = " + str(M) + "\nПлощадь треугольника методом Монте-Карло = " + str(S) + '\n Точная площадь = ' + str(S_real))
    print(expression)
    print("ez")


def draw_points(arr_xx, arr_yy):
    # по условию определяем точки внутри/снаружи фигуры
    for i in range(0, expression):
        f1, f2 = f(arr_xx[i])
        if f1 < arr_yy[i] < f2:
            x_inside.append(arr_xx[i])
            y_inside.append(arr_yy[i])
        else:
            x_outside.append(arr_xx[i])
            y_outside.append(arr_yy[i])

    # строим точки на графике
    ax.scatter(x_inside, y_inside, color='green')
    ax.scatter(x_outside, y_outside, color='red')


def draw_graph(arr_x, arr_y21, arr_y22):
    ax.plot(arr_x, arr_y21, color='blue', label="Exp func")
    ax.plot(arr_x, arr_y22, color='magenta', label="Quadro func")

    ax.plot([0, 0], [0, arr_y22[0]], color='black')
    #ax.plot([0, arr_x[-1]], [0, 0], [0, arr_x[-1]], [arr_y22[0], arr_y22[0]], color='green')


def ex1():
    n = 11
    i = 0

    arr_x.append(i)
    arr_y21.append(10*arr_x[i]/n)
    arr_y22.append(10*(arr_x[i]-20)/(n-20) + 20)

    while abs(arr_y21[i] - arr_y22[i]) > 0.3:
        i += 1
        arr_x.append(i)
        fx21 = 10*arr_x[i]/n
        fx22 = 10*(arr_x[i]-20)/(n-20) + 20
        arr_y21.append(fx21)
        arr_y22.append(fx22)


    # axbox = fig.add_axes([0.1, 0, 0.8, 0.075])
    # text_box = TextBox(axbox, "Кол-во точек", textalignment="center")
    # text_box.on_submit(submit)
    # text_box.set_val(100)
    submit(expression)
    #legend = plt.legend(loc='upper left', shadow=True, fontsize='x-small')
    plt.show()


ex1()

