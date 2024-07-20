# Дополнения к основным материлам занятий

''' 
ОПЕРАТОРЫ BREAK, CONTINUE И PASS В ЦИКЛАХ PYTHON
'''
# https://www.8host.com/blog/operatory-break-continue-i-pass-v-ciklax-python-3/
'''
Оператор break 

В Python оператор break позволяет прервать цикл 
при возникновении внешнего фактора.
'''
number = 0
for number in range(10):
    number = number + 1
if number == 5: 
    print('Error')
    # break # VSCode не позволяет воспользоваться оператором "break"
print('Number is ' + str(number))
print('Out of loop')


''' 
Оператор continue 

Оператор continue позволяет пропустить часть цикла 
при возникновении внешнего фактора и 
перейти к следующей итерации цикла. 
То есть текущая итерация прерывается, после чего 
программа возвращается в начало цикла.
'''
number = 0
for number in range(10):
    number = number + 1
if number == 5:
    print('Error')
    # continue # VSCode не позволяет воспользоваться оператором "continue"
print('Number is ' + str(number))
print('Out of loop')


'''
Оператор pass

При возникновении внешнего фактора оператор pass 
устраняет любое влияние этого фактора на обработку кода. 
Код обрабатывается до тех пор, пока не появится break или другой оператор.
'''
number = 0
for number in range(10):
    number = number + 1
if number == 5:
    pass
print('Number is ' + str(number))
print('Out of loop')