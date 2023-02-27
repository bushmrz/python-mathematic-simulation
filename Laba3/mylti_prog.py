import pandas as pd
import matplotlib.pyplot as plt


# метод мультконгр
n = 4
count = 100

a_const = 1357
b_const = 5689
var = a_const

list_var = []
list_prod = []
list_celoye = []
list_ostatok = []
list_random = []

for i in range(count):

    prod = a_const * var
    celoye = prod // b_const
    ostatok = prod % b_const
    if len(str(ostatok)) < n:
        ostatok = int(str(ostatok) + '0' * (n - len(str(ostatok))))

    random = ostatok / (10 ** n)

    list_var.append(var)
    list_prod.append(prod)
    list_celoye.append(celoye)
    list_ostatok.append(ostatok)
    list_random.append(random)

    var = ostatok

data = {'var': list_var, 'prod': list_prod, 'celoye': list_celoye, 'ostatok': list_ostatok, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)

df['random'].hist(bins=100)
title = plt.suptitle('Линейный конгруэнтный метод')
plt.xlim(0.0, 1.0)
plt.show()