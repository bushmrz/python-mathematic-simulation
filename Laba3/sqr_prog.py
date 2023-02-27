import pandas as pd
import matplotlib.pyplot as plt

# метод серединных квадратов
count = 100
n = 4
chislo = 7153

list_chislo = []
list_kvadrat = []
list_random = []

start = n // 2
stop = n + n // 2

for i in range(count):
    kvadrat = chislo * chislo
    if len(str(kvadrat)) % 2 == 1:
        kvadrat = '0' + str(kvadrat)

    chislo_srez = int(str(kvadrat)[start:stop])
    random = chislo_srez / (10 ** n)
    list_chislo.append(chislo)
    list_kvadrat.append(kvadrat)
    list_random.append(random)
    chislo = chislo_srez

data = {'chislo': list_chislo, 'kvadrat': list_kvadrat, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)

df['random'].hist(bins=100)
title = plt.suptitle('Метод серединных квадратов')
plt.xlim(0.0, 1.0)
plt.show()
