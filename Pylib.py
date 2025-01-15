import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

  #NumPy

list_0 = np.linspace(0, 3, 10)                   # 10 чисел от 0 до 3х
print(list_0)
############
list_1 = np.random.randint(-16,89,8)
print(list_1)                                                  #Построение рандомных списков
list_2 = np.random.randint(-46,94,8)                 #с их последующим сложением
print(list_2)
sum_1 = list_1 + list_2
print(sum_1)
############
list_3 = ([2, 4, 6, 8, 10])
list_3 = np.sqrt(list_3)   #Квадратный корень
print(list_3)
list_3 = np.cos(list_3)    #Косинус
print(list_3)
list_3 = np.sin(list_3)    #Синус
print(list_3)
list_3 = np.clongdouble(list_3)    #Два числа с расширенной точностью
print(list_3)
list_3 = np.exp(list_3)    #Экспонента
print(list_3)
#############


   #pandas

df = pd.read_csv("test.txt", sep=" ",encoding='utf-8')
print(df)      #Считываем данные из файла test.txt

data = {'Фамилия': ['Глебов', 'Угальде', 'Сперцян', 'Вендел', 'Батраков'],
        'Команда': ['Ростов', 'Спартак', 'Краснодар', 'Зенит', 'Локомотив'],
        'Номер': [15, 9, 10, 8, 83]}
df = pd.DataFrame(data)                       #Создание фрейма данных
print(df)



  #matplotlib

np.random.seed(19680801)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()



