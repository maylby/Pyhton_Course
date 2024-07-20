# Результаты Автотеста по ДЗ-07
# https://autotest.gb.ru/problems/83?lesson_id=391158&_ga=2.178040422.236235188.

"""
Задача 1 (ДЗ-07)

print_operation_table


Напишите функцию print_operation_table(operation, num_rows, num_columns), 
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Пример
"""
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:

# 1 2 3
# 2 4 6 
# 3 6 9

"""
Тест 1
Тест не пройден ✗

Формулировка:
* Итоговый код для проверки. Иногда добавляем что-то от себя :)

"""
import warnings
warnings.filterwarnings('ignore')

# Введите ваше решение ниже

#При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x * y, 3, 3)


# Ожидаемый ответ:

# 1 2 3
# 2 4 6
# 3 6 9

# Ошибка:
"""
Traceback (most recent call last):
  File "TEBZXWTYZLXUDQQNGUVG.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)
"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'



"""
Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)
"""
import warnings
warnings.filterwarnings('ignore')


# Введите ваше решение ниже


# При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x + y, 4, 4)


""" 
Ожидаемый ответ: 
"""
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8

"""
Ошибка:

Traceback (most recent call last):
  File "EHYDHWLJAZ3V559B2ZIL.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)
"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'



"""
Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)
"""
import warnings
warnings.filterwarnings('ignore')

# Введите ваше решение ниже


# При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x - y, 5, 5)

"""
Ожидаемый ответ:
"""
# 0 -1 -2 -3 -4
# 1 0 -1 -2 -3
# 2 1 0 -1 -2
# 3 2 1 0 -1
# 4 3 2 1 0
"""
Ошибка:
"""
"""
Traceback (most recent call last):
  File "7IPS5UX9UT3VICKC10Z9.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)

"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'


"""
Тест 4
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)
"""
import warnings
warnings.filterwarnings('ignore')

# Введите ваше решение ниже

#При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x * y, 1, 2)

"""
Ожидаемый ответ:

ОШИБКА! Размерности таблицы должны быть больше 2!

Ошибка:

Traceback (most recent call last):
  File "25TDCA0OYWI6FFL2KV6B.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)
"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'



"""
Тест 5
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)

"""
import warnings
warnings.filterwarnings('ignore')

# Введите ваше решение ниже

#При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x / y, 4, 4)

"""
Ожидаемый ответ:
"""
# 1.0 0.5 0.3333333333333333 0.25
# 2.0 1.0 0.6666666666666666 0.5
# 3.0 1.5 1.0 0.75
# 4.0 2.0 1.3333333333333333 1.0

"""
Ошибка:
Traceback (most recent call last):
  File "LL6YKC1TTCZK2SEAGO0X.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)

"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'



"""
Тест 6
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)
"""
import warnings
warnings.filterwarnings('ignore')

# Введите ваше решение ниже

#При отправке кода на Выполнение раскомментируйте строку ниже, 
# чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - 
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

def print_operation_table(operation, num_rows, num_columns): 
    
    res = []
    if num_rows < 2: 
        print('Error!') 
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                res.append(operation(i, j))

            print(*res) 
            res = []
        
print_operation_table(lambda x, y: x * y)

# print_operation_table(lambda x, y: x * y, num_rows, num_columns) 

print_operation_table(lambda x, y: x * y)

"""
Ожидаемый ответ:
"""
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81

"""
Ошибка:

Traceback (most recent call last):
  File "CZ4EWLSA2ZAU8FDCRP4G.py", line 31, in <module>
"""
    # print_operation_table(lambda x, y: x * y)
"""
TypeError: 
"""
# print_operation_table() missing 2 required positional arguments: 'num_rows' and 'num_columns'
