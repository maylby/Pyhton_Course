# Знакомство с языком Python (семинары)
# Урок 9. Работа с табличными данными
# https://gb.ru/lessons/391160/homework

""""
Для решения данного домашнего задания вам необходимо 
воспользоваться сервисом автоматической проверки написанного кода.
Для того, чтобы успешно выполнить задание, необходимо 
перейти по каждой из представленных ссылок и решить все предложенные задачи. 
Будьте внимательны, количество попыток отправки кода на проверку ограничено! 
Вам дано 5 попыток на каждую задачу.

Прикреплять полученные решения не требуется. 
Итоговая оценка домашнего задания появится автоматически на платформе 
после решения всех задач. Полученная оценка не повлияет на получение 
итогового документа об обучении.


Задача 1
"""
# https://autotest.gb.ru/problems/113?lesson_id=391160&_ga=2.108864450.1926430629.1706850067-1736153193.1704617193
"""
Определить среднюю стоимость дома

Дан файл california_housing_train.csv. Определить среднюю стоимость дома, 
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg. 
Используйте модуль pandas.
 
Без библиотек "pandas", код в VSCode работать не будет.


Решение (автотест)
"""

import pandas as pd # Сообщение VSCode: "не удалось импортировать «pandas»"
df = pd.read_csv('california_housing_train.csv')

avg = df[(df['population'] >= 0) & (df['population'] <= 500)] ['median_house_value'].mean()
print(avg) 



"""
Задача 2
"""
# https://autotest.gb.ru/problems/114?lesson_id=391160&_ga=2.4481907.1926430629.1706850067-1736153193.1704617193
"""
Максимальная households

Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" 
в зоне минимального значения переменной min_population 
и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas

Решение для автотеста, 
без библиотек "pandas" в VSCode работать не будет


Решение (Александр Верзун, 01_(С-10))
"""

import pandas as pd # Сообщение VSCode: "не удалось импортировать «pandas»"
df = pd.read_csv('california_housing_train.csv')
# x = 30
min_population = df['population'].min()

max_households_in_min_population = df[df['population'] <= min_population] ['households'].max()
print(max_households_in_min_population)



'''
Запрос 'head(10)'
'''
import pandas as pd # Сообщение VSCode: 
                    # "не удалось импортировать «pandas»"
df = pd.read_csv('california_housing_train.csv')
df.head(10)
print(df.head(10))

# выдача на сервисе "goole panda":
# 0 -114.31 34.19   15.0    5612.0  1283.0  1015.0 472.0    1.4936  66900.0


''' 
запрос 'tail' 
'''
import pandas as pd
df = pd.read_csv('california_housing_train.csv')
df.tail()
print(df.tail())


''' 
запрос 'dtypes' 
'''
import pandas as pd
df = pd.read_csv('california_housing_train.csv')
df.tail()
print(df.dtypes)


''' 
запрос 'shape' 
'''
import pandas as pd
df = pd.read_csv('california_housing_train.csv')
df.tail()
print(df.shape)

# Вывод автотеста по 'shape':
# (30, 9)
