''' 
Создание таблиц
'''
# https://metanit.com/python/tkinter/4.2.php
'''
Для отображения данных в виде таблицы параметру show 
предпочтительно передать значение "headings" (если надо отображать заголовки), 
либо " " (для таблицы без заголовков). 
Определим небольшую таблицу с тремя столбцами:
'''

from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
 
# определяем данные для отображения
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
 
# определяем столбцы
columns = ("name", "age", "email")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.heading("email", text="Email")
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)
 
root.mainloop()

'''
Здесь данные, которые будут отображаться в таблице, 
определены в виде списка people, который хранит набор кортежей. 
Каждый кортеж состоит из трех элементов. Условно будем считать, 
что первый элемент кортежа представляет имя пользователя, 
второй - возраст, а третий - электронный адрес. 
И эти данные нам надо отобразить в таблице:
'''
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]

'''
Для отображения этих данных определяем три столбца: 
name, age и email в виде кортежа и передаем их параметру columns:
'''
columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")

'''
Далее нам надо настроить заголовки столбца 
с помощью метода heading() класса Treeview 
(по умолчанию столбцы не имеют никаких заголовков). 
Данный метод принимает ряд параметров:
'''
tree.heading("name", text="Имя")

'''
Первый параметр указывает на имя столбца. 
В примере выше определяем также параметр text, определящий текст заголовка
И последний момент - добавляем сами данные в таблицу 
с помощью метода insert() класса Treeview
'''
tree.insert("", END, values=person)
'''
Первый параметр - пустая строка "" указывает, что 
элемент добавляется как элемент верхнего уровня, 
то есть у него нет родительского элемента. 
Значение END указывает, что элемент добавляется в конец набора. 
И параметр values в качестве добавляемых данных устанавливает кортеж person.

В итоге мы получим следующую таблицу:

Имя | Возраст | email
Tom     38      tom@
Bob     42      bob@
Sam     28      sam@


Создание таблицы с помощью Treeview в Tkinter и python

Настройка столбца

Вполне возможно, что изначальные настройки столбцов нас не устроят. 
Например, текст заголовка располагается по умолчанию по центру, 
а данные столбца выравниваются по левому краю. 
Кроме того, каждый столбец имеет некоторую начальную ширину, 
в следствие чего ширина виджета может оказаться больше ширины окна. 
Либо мы захотим как-то иначе настроить вид столбца.

Прежде всего мы можем настроить заголовки столбца с помощью метода heading():

'''
def heading(column, text, image, anchor, command):
    column 
# Параметр 'def' вставлен для подсветки метода "heading()"
# Двоеточие и переменная 'column' введены, чтобы 
# VSCode не определял строку, как написанную с ошибкой 
 

'''
Параметры метода:

* column: имя настраиваемого столбца
* text: текст заголовка
* image: картинка для заголовка
* anchor: устанавливает выравнивание заголовка по определенному краю. 
          Может принимать значения n, e, s, w, ne, nw, se, sw, c
* command: функция, выполняемая при нажатии на заголовок


Для настройки столбца в целом применяется метод column():

'''
def column(column, width, minwidth, stretch, anchor):
    column 
# Параметр 'def' вставлен для подсветки метода
# Двоеточие и переменная 'column' введены, чтобы 
# VSCode не определял строку, как написанную с ошибкой 

'''
Параметры метода:

column: индекс настраиваемого столбца в формате "# номер_столбца"
width: ширина столбца
minwidth: минимальная ширина
anchor: устанавливает выравнивание заголовка по определенному краю. 
        Может принимать значения n, e, s, w, ne, nw, se, sw, c
stretch: указывает, будет ли столбец растягиваться при растяжении контейнера. 
        Если будет, то значение True, иначе значение False

        
Применим некоторые из этих параметров:
'''
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
 
# определяем данные для отображения
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
 
# определяем столбцы
columns = ("name", "age", "email")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки с выпавниваем по левому краю
tree.heading("name", text="Имя", anchor=W)
tree.heading("age", text="Возраст", anchor=W)
tree.heading("email", text="Email", anchor=W)
 
# настраиваем столбцы
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=60)
tree.column("#3", stretch=NO, width=100)
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)
 
root.mainloop()
'''
В данном случае для заголовков устанавливаем выравнивание по левому краю. 
Для столбцов запрещаем растяжение и устанавливаем ширину.

URL картинки: 
'''
# https://metanit.com/python/tkinter/pics/2.88.png
'''
Текст картинки: 
"настройка столбцов в таблице в виджете Treeview в Tkinter и Python"



При добавлении изображения оно помещается в правой части. 
Например, установка изображения для третьего столбца:
'''
# предполагается, что в папке приложения располагается файл email_icon_micro.png
email_icon = PhotoImage(file="./email_icon_micro.png")
tree.heading("email", text="Email", anchor=W, image=email_icon)

'''
# URL картинки: 
'''
# https://metanit.com/python/tkinter/pics/2.89.png
'''
Текст картинки:
"картинка в заголовке столбца в таблице в виджете Treeview в Tkinter и Python"



Добавление к Treeview прокрутки
'''
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)
 
# определяем данные для отображения
people = [
    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ]
 
# определяем столбцы
columns = ("name", "age", "email")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.grid(row=0, column=0, sticky="nsew")
 
# определяем заголовки
tree.heading("name", text="Имя", anchor=W)
tree.heading("age", text="Возраст", anchor=W)
tree.heading("email", text="Email", anchor=W)
 
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=60)
tree.column("#3", stretch=NO, width=100)
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)
 
# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
 
root.mainloop()

'''
URL картинки:
'''
# https://metanit.com/python/tkinter/pics/2.90.png
'''
Текст картинки:
Прокрутка таблицы в Treeview в Tkinter и python
'''