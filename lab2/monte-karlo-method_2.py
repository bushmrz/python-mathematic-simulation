import math
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import TextBox
from scipy import integrate

n_var = 3
expression = 2000
M=S=0
x_max = 7
y_max = 6
#x_max = 8
x_dots = []
y_dots = []

# точки внутри фигуры
x_inside = []
y_inside = []

# точки вне фигуры
x_outside = []
y_outside = []

v,err = 0, 0
fig, ax = plt.subplots()

x_gen = []
y_gen = []

def f(x):
    #return math.sqrt(7 - 3 * math.sin(x) * math.sin(x))
    return math.sqrt(29-n_var*(math.cos(x)**2))



# for i in range(1,8):
# #for i in range(1, 9):
#     y_max = max(f(i), y_max)

def find_points(expression):
    for i in range(0, int(expression)):
        if y_gen[i] < f(x_gen[i]):
            x_inside.append(x_gen[i])
            y_inside.append(y_gen[i])
        else:
            x_outside.append(x_gen[i])
            y_outside.append(y_gen[i])


def draw_graph():
    ax.plot(x_dots, y_dots, '-', color='b')
    #plt.ylim(0, y_max + 0.5)
    ax.grid()


def submit(expression):
    ax.clear()
    draw_graph()

    for i in range(0, int(expression)):
        x_gen.append(random.uniform(0, x_max))
        y_gen.append(random.uniform(0, y_max))

    find_points(expression)
    ax.scatter(x_inside, y_inside,  color='green')
    ax.scatter(x_outside, y_outside,  color='red')

    M = len(x_inside)
    S = round((M / int(expression)) * (x_max * y_max), 2)

    v, err = integrate.quad(f, 0, x_max)

    fig.suptitle('Кол-во точек внутри = ' + str(M) + '\nПлощадь фигуры методом Монте-Карло = ' + str(S)
              + '\nТочная площадь фигуры = ' + str(v), fontsize=10)

    print(expression)


def ex2():
    x = 0
    while x <= x_max:
        x_dots.append(x)
        x += 0.1

    for dot in x_dots:
        y = f(dot)
        y_dots.append(y)


    submit(expression)
    # axbox = fig.add_axes([0.1, 0, 0.8, 0.075])
    # text_box = TextBox(axbox, "Кол-во точек", textalignment="center")
    # text_box.on_submit(submit)
    # text_box.set_val(expression)

    plt.show()

ex2()