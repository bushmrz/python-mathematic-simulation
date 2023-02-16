import matplotlib.pyplot as plt
import math

# var 11
# x 2 4 6 8 10 12
# y 2.4 2.9 3 3.5 3.6 3.7

x_test = [2, 4, 6, 8, 10, 12]
y_test = [2.4, 2.9, 3, 3.5, 3.6, 3.7]

# x_test = [1, 2, 3, 4, 5, 6]
# y_test = [1, 1.5, 3, 4.5, 7, 8.5]

def linear(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    average_x = 0
    average_y = 0
    while i < size:
        sum_xy += data_x[i] * data_y[i]
        sum_y += data_y[i]

        sum_x += data_x[i]
        sum_sqare_x += data_x[i] * data_x[i]
        i += 1

    average_x = sum_x / size
    average_y = sum_y / size
    return_k = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
    return_b = average_y - average_x * return_k
    print("Linear: \n k = ", round(return_k,2), "b = ", round(return_b,2))
    return return_k, return_b

def step_func(data_x, data_y):
    size = len(data_x)
    ln_x = []
    ln_y = []
    ln_x_sum = ln_y_sum = 0
    ln_sq_x = ln_xy = 0
    a = beta = 0
    delta = delta1 = delta2 = 0
    for i in range(size):
        ln_x.append(math.log(data_x[i]))
        ln_y.append(math.log(data_y[i]))
        ln_x_sum += ln_x[i]
        ln_y_sum += ln_y[i]
        ln_sq_x += ln_x[i]**2
        ln_xy += ln_y[i]*ln_x[i]

    #print("y:", ln_xy, ln_y_sum)
    delta = ln_sq_x*size - ln_x_sum**2
    #print(delta)
    delta1 = ln_xy*size - ln_x_sum*ln_y_sum
    #print(delta1)
    delta2 = ln_sq_x*ln_y_sum - ln_xy*ln_x_sum
    #print(delta2)

    a = delta1/delta
    beta = (math.e)**(delta2/delta)


    print("Step func: \n a = ", round(a,2)," beta = ", round(beta,2))
    return a, beta

def exp_func(data_x, data_y):
    size = len(data_x)
    ln_y = []
    x_sum = ln_y_sum = 0
    sq_x = sum_xy = 0
    a = beta = 0
    for i in range(size):
        ln_y.append(math.log(data_y[i]))
        ln_y_sum += ln_y[i]
        x_sum += data_x[i]
        sq_x += data_x[i]**2
        sum_xy += ln_y[i] * data_x[i]

    a = (sum_xy*size - x_sum*ln_y_sum)/(sq_x*size - x_sum**2)
    beta = (math.e)**((sq_x*ln_y_sum - x_sum*sum_xy)/(sq_x*size - x_sum**2))

    print("Exp func: \n a = ", round(a,2), " beta = ", round(beta,2))
    return a, beta

def quadro_func(data_x, data_y):
    size = len(data_x)

    x_4_sum = x_3_sum = x_2_sum = 0
    quadro_sum = 0
    xy_sum = 0
    x_sum = y_sum = 0
    a = b = c = delta = 0
    for i in range(size):
        x_sum += data_x[i]
        y_sum += data_y[i]
        x_2_sum += data_x[i]**2
        x_3_sum += data_x[i] ** 3
        x_4_sum += data_x[i] ** 4
        xy_sum += data_x[i] * data_y[i]
        quadro_sum += data_x[i]**2 * data_y[i]

    delta = x_4_sum*x_2_sum*size + (x_3_sum*x_sum*x_2_sum)*2 - (x_2_sum**3) - size*x_3_sum**2 - x_4_sum*x_sum**2
    #print(delta)

    a = (quadro_sum*x_2_sum*size + (xy_sum*x_sum*x_2_sum) + (y_sum*x_3_sum*x_sum) - y_sum*(x_2_sum**2) - size*x_3_sum*xy_sum - quadro_sum*x_sum**2)/delta
    b = (x_4_sum*xy_sum*size + (x_3_sum*y_sum*x_2_sum) + (quadro_sum*x_sum*x_2_sum) - xy_sum*(x_2_sum**2) - size*x_3_sum*quadro_sum - x_4_sum*x_sum*y_sum)/delta
    c = (x_4_sum*x_2_sum*y_sum + (x_3_sum*x_sum*quadro_sum) + (x_3_sum*xy_sum*x_2_sum) - quadro_sum*(x_2_sum**2) - y_sum*x_3_sum**2 - x_4_sum*x_sum*xy_sum)/delta

    print("Quadro func: \n a = ", round(a,2), " b = ", round(b,2), " c = ", round(c,2))
    return a, b, c


def mistake(first_y, second_y):
    size = len(first_y)
    m = 0
    for i in range(size):
        d = (first_y[i]-second_y[i])**2
        m += d
        d = 0

    return m

a1, beta1 = step_func(x_test, y_test)
a2, beta2 = exp_func(x_test, y_test)
a_lin, b_lin = linear(x_test, y_test)
a, b, c = quadro_func(x_test, y_test)

linear_y = []
step_y = []
exp_y = []
quadro_y = []
size = len(x_test)

m_lin = m_step = m_exp = m_quadro = 0

for i in range(size):
    linear_y.append(a_lin*x_test[i] + b_lin)
    step_y.append(beta1*(x_test[i]**a1))
    exp_y.append(beta2*(math.e)**(a2*x_test[i]))
    quadro_y.append(a*x_test[i]**2+b*x_test[i]+c)

m_lin = mistake(y_test, linear_y)
m_step = mistake(y_test, step_y)
m_exp = mistake(y_test, exp_y)
m_quadro = mistake(y_test, quadro_y)

print("Линейное отклонение: ", round(m_lin,2), "\n Степенное отклонение: ", round(m_step,2),
      "\n Экспоненциальное отклонение: ", round(m_exp,2), "\n Квадратичное отклонение", round(m_quadro,2))

min_m = min(m_lin, m_step, m_exp, m_quadro)
if min_m == m_lin:
    print("Наименьшее отклонение у линейного: ",  round(m_lin,2))
elif min_m == m_step:
    print("Наименьшее отклонение у степенного: ",  round(m_exp,2))
elif min_m == m_exp:
    print("Наименьшее отклонение у экспоненциального: ",  round(m_exp,2))
elif min_m == m_quadro:
    print("Наименьшее отклонение у квадратичного: ",  round(m_quadro,2))


plt.scatter(x_test, y_test, color = 'black', label = "Main func")
plt.plot(x_test, linear_y, color = 'red', label = "Linear")
plt.plot(x_test, step_y, color = 'green', label = "Step func")
plt.plot(x_test, exp_y, color = 'blue', label = "Exp func")
plt.plot(x_test, quadro_y, color = 'magenta', label = "Quadro func")

plt.scatter(x_test, linear_y, color = 'red')
plt.scatter(x_test, step_y, color = 'green')
plt.scatter(x_test, exp_y, color = 'blue')
plt.scatter(x_test, quadro_y, color = 'magenta')

legend = plt.legend(loc='upper left', shadow=True, fontsize='x-small')
plt.show()



