import random
import numpy as np

details = 500
time = 0
time_issues = 0
breakage_interval = np.random.normal(20, 2)
processing_time = 0
count_breakdown = 0
troubleshooting_issues_total_time = 0

time_entrance = [] # время до появления детали
interval_entrance = [] # интервал между поступлением заданий

for i in range(details):
    # экспоненциальное распределение величины интервала между поступлением заданий на станок (в среднем раз в час)
    entrance = random.expovariate(1)
    if i == 0:
        time_entrance.append(entrance)
    else:
        time_entrance.append(entrance + time_entrance[-1])
    interval_entrance.append(entrance)


# print(time_entrance)

# проверка на поломку
def check_breakage(setting_up):
    global time, processing_time
    if breakage_interval <= 0:
        time += setting_up + breakage_interval
        processing_time += setting_up + breakage_interval
        breakdown()
        return True
    else:
        time += setting_up
        processing_time += setting_up
        return False


def breakdown():
    global breakage_interval, time, processing_time, time_issues
    # интервал между поломками с мат.ожиданием 20ч и среднеквадратич. отклонением 2 ч
    breakage_interval = np.random.normal(20, 2)
    # время на устранение поломки
    troubleshooting_issues = np.random.uniform(0.1, 0.5)
    time += troubleshooting_issues
    # время на устранение всех поломок за время работы станка
    time_issues += troubleshooting_issues
    processing_time += troubleshooting_issues


i = 0
# obrabotka = 0

while i != details:
    if i == 0:
        time += time_entrance[0]
    else:
        if time < time_entrance[i]:
            time += time_entrance[i] - time

    print(i + 1)
    # print('Время появления детали:', time_entrance[i])
    # print('Обработка детали.....')
    # наладка станка с равномерно распределенным временем на интервале 0.2-0.5 ч
    setting_up = np.random.uniform(0.2, 0.5)
    breakage_interval -= setting_up

    # print('Наладка станка:', setting_up)
    if check_breakage(setting_up):
        i -= 1
        # print('Поломка')
        count_breakdown += 1
    # время выполнения задания норм. распределено с мат.ожид. 0.5 ч и среднеквадратич. отклонением 0.1 ч
    task_execution = np.random.normal(0.5, 0.1)
    # время до поломки
    breakage_interval -= task_execution

    if check_breakage(task_execution):
        i -= 1
        # print('Поломка')
        count_breakdown += 1

    i += 1
    # print('Время выполнения задания:', task_execution)
    # print('Время обработки детали всего:', processing_time)
    # # obrabotka += processing_time
    # print('Время работы станка:', time)
    # processing_time = 0
    # print("До поломки: ", breakage_interval)
    # print()

print('Итоговое время работы станка:', time)
print('Интервал между поступлением деталей:', sum(interval_entrance) / details)
print('Количество поломок:', count_breakdown)
print('Время, затраченное на исправление поломок', time_issues)
