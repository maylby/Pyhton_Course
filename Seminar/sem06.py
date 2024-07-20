# Знакомство с языком Python (семинары)
# Урок 6. Повторение списков
# https://gb.ru/lessons/391157


# 00:12:35
"""
Разбор решения задач ДЗ-05

Задача 1 (26): 
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
"""
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
""""
Решение
"""
# a = int(input('Input base: '))
# b = int(input('Input exp: '))

# def power(a, b):
#     if b == 0: return 1
#     return (a * power(a, b - 1))

# print(f'{a} ** {b} = {power(a, b)}')


"""
Задача 28: 
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""
# 2 2
# 4

"""
Решение
""" 
# a = int(input('Input A: '))
# b = int(input('Input B: '))

# def sum(a, b):
#     if a < b: a, b = b, a # аналог записи "temp" (передача значений)
# 	# temp = a 
# 	# a = b
# 	# b = temp 
#     if b == 0: return a
#     return sum(a + 1, b - 1) # вариант записи

# print(f'sum: {sum(a, b)}')


# 00:26:40
"""
Задача про холодильники 
(чат семинара)

Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

Формат входных данных
В первой строке подаётся число 'n'.
'n' – количество холодильников. 
В последующих n-строках вводятся строки, 
содержащие латинские строчные буквы и цифры, 
в каждой строке от 5 до 100 символов.

Сердюк: "Два способа решения через списки и через условие (?)"

(см. решение в видео семинара 7)
"""


# Sample Input 1: 6

# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# Sample Output 1:
# 1 2 3


# Sample Input 2: 9

# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton

# Sample Output 2: 
# 1 2 7 8



# 00:27:30

"""
Определить дружественная рекурсия или нет

Дружественные функции - это функции, которые не являются членами класса, 
однако имеют доступ к его закрытым членам - переменным и функциям,

Решение (см. семинар 7)
"""


# 00:28:10
"""
Сергей Сердюк 1. 
Напишите функцию, которая принимает одно число и проверяет, 
является ли оно простым

* Напоминание: 
Простое число - это число, которое 
имеет два делителя: 1 и n (само число) *

Три вывода:
    - Простое число
    - Составное число
    - Рекурсия 
"""

# 00:52:00 (разбор решения)
"""
Решение
"""
# n = int(input('Input N: '))

# def function(n, d = 2): # 'd = 2' - именованный аргумент с заданным значением (2)
#                         # алгоритм поиска простого числа начинается с деления на 2,
#                         # задаём значение 2, чтобы постоянно не вводить его
#                         # при определении простого и составного числа
#     if d * d > n: return True # если квадрат делителя (d * d) больше делимого (n),
#                               # то возврат 'True'.
#     elif n % d == 0: return False # Иначе, если 'n' кратно 'd', возврат 'False'.
#     return function(n, d + 1) # При невыполнении всех условий, 
#                               # возврат 'function(n, d + 1)', где 'd' увеличено на 1
# print(function(n, d = 2))



# 00:28:30 (появление условия в чате семинара)
# 01:11:50 (разбор решений)

"""
Определить рекурсией является слово (число) палиндромом. 

Три вывода:
    - Палиндром
    - Не палиндром
    - Рекурсия

Не обязательно брать слова-палиндромы 
(шалаш, казак, колок, тот, оно),
можно использовать набор чисел (1 2 3 3 2 1)


Решение

Вариант 1 (while)
"""
# st = '1234321'
# st = 'казаки'

# def polyndrome(st):
# 	if len(st) > 1: 
# 		mid = len(st) // 2
# 		left = st[:mid]
# 		right = st[mid:]
# 		# polyndrome(left)
# 		# polyndrome(right) 
# 		i = j = mid
# 		while i < len(left) and j < len(right): 
# 			if left[i] != right[j]: return 'Not polyndromes'
# 			else: 
# 				i += 1
# 				j += 1
# 	return 'Polyndrome'

# print(f'{st} -> {polyndrome(st)}')



"""		
Вариант 2 (рекурсия)
"""

# s = '1234321'
# s = 'казак'

# def pol(s, i = 1): # 'i = 1' - именованная переменная
# 	               # значение неизменное, его можно указать сразу
# 	if len(s) <= 1: return 'Polyndrome' # возврат: 'Polyndrome',
#                                         # если длина меньше или равна 1.
# 	elif s[0] == s[-1]: # Иначе, если первый и последний элемент равны, то
# 		return pol(s[i:-i]) # переходим к сравнению следующих,
#                             # второго и предпоследнего, ... и т.д.
# 	return 'Not polyndromes' # Возврат: 'Not polyndromes' 
#                              # в случае невыполнения равенства (s[0] == s[-1])
# p = pol(s, i = 1)
# print(f'{s} -> {p}')



# 01:17:00
'''
Задача №45. 
(Решение в группах)

Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) 
равна числу m и наоборот. 

Например, 220 и 284 – дружественные числа, т.к. сумма делителей 
числа 284 равна 220, а сумма делителей числа 220 равна 284.

Сумма делителей числа: 
'''
# 284 = 1 + 2 + 4 + 142 + 71
# 220 = 1 + 2 + 4 + 110 + 55 + 44 + 22 + 11 + 10
'''
По данному числу k выведите все пары дружественных чисел, 
каждое из которых не превосходит k. 

На входе - одно натуральное число k, не превосходящее 10**5. 
Программа должна вывести все пары дружественных чисел, 
каждое из которых не превосходит k. 

Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз 
(перестановка чисел новую пару не дает).
'''
# Ввод: 
# 300  

# Вывод:
# 220 284

'''
Решение:

Вариант 1 (while)
'''
# k = 300
# dict01 = {1: 1}
# for i in range(k):
# 	x = i - 1
# 	sum = 0
# 	while x >= 1: 
# 		if i % x == 0: 
# 			sum += x
# 		x -= 1
# 	dict01[i] = sum

# print(dict01)


'''
Вариант 2 (for)
'''
# n = 300
# dict01 = {1: 1}
# for i in range(n):
# 	x = i - 1
# 	sum = 0
# 	for j in range(1, i // 2 + 1): 	# перебор до середины значения,
# 					                # чтобы избежать повторов 
# 		                            # ({1: 299, ..., 299: 1})
# 		if i % j == 0:
# 			sum += j
# 	dict01[i] = sum

# print(dict01)


# 01:48:45
'''
Задачи ДЗ-06 (разбор решений см. семинар 7)
'''