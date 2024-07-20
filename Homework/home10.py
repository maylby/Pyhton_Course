# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# https://gb.ru/lessons/391161/homework

"""
Задача 44: 

В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?

исходный код:
"""
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst) 
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


'''
Решение
'''
import random

lst = (['robot'] + ['human']) * 5
random.shuffle(lst)
# print(*lst) 
a, b = 1, 2
for i in lst:
    if i == 'robot': lst = a
    else: lst = b
    # print(lst, end = " ") 
    res1, res2 = [], []
    for i in range(lst):
        if i % 2 != 0: res1, res2 = 1, 0
        else: res1, res2 = 0, 1

        print(f'robot {res1} human {res2}')


