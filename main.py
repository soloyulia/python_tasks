import argparse
import copy
import datetime
import itertools
import math
import stringprep
import time

# import turtle
# t = turtle.Pen()
# window = turtle.Screen()
# # window.mainloop() нужно ставить  конце
#
# t.width(7)
# t.color('red')
# # t.fillcolor('green')
# # t.begin_fill()
# t.width(2)
#
# # for i in range(1,3):
# #     t.left(90)
# #     t.forward(50)
# #     t.right(90)
# #     t.forward(50)
# len1 = 10
# step = 0
# while step<20:
#     t.forward(len1)
#     t.left(72)
#     len1 +=10
#     step +=1
#
# t.up()
# t.home()
# window.mainloop()

# КОРТЕЖИ

# data = 244,7,7,5,78,98888, True,'Hello'
# print(data[0:7])
# print(data.count(7))
# print(len(data))
# for el in data:
#     print(el)
# num = [34,56,87]
# new_data = tuple(num)
# print(new_data)

# word = 'Hello World!'
# print(word)
# new_word = tuple(word)
# print(new_word)

# СПИСКИ

# nums = [3,45,True,'45',2,89,56,23]
# nums[0] ='by'
# print(nums[-1][1])
# print('Длина списка = ',len(nums))
# for el in nums:
#     print(el)
# nums.insert(1,True)
# b = [5,50,500]
# nums.extend(b)
# nums.sort()
# nums.pop(-1)
# nums.remove(3)
# for el in nums:
#         print(el)

# n = int(input('Укажите длину списка '))
# user = []
# el = 0
# while el < n:
#     a = 'Введите значение %s списка ' % el
#     user.append(input(a))
#     el +=1
#
# print(user)

# СЛОВАРИ

# country = {'kode':'RU','name':'Russian','popul':144}
# country = dict(code='RU',name='Russian',popul=144)
# print(country.items())
# for key,value in country.items():
#     print('Ключ ', key,': значение ',value)

# print(country.get('name'))
# country.pop('name')
# country.popitem()
# country.keys()
# print(country.keys())
# country['ves']=123
# print(country)

# person = {
#     'user1': {
#         'first_name':'Jonn',
#         'last_name':'Marli',
#         'age':45,
#         'adress': ('г.Москва', 'ул Заслонова', 3),
#         'grades': {'math':5, 'phizika':4}
#     },
#     'user2': {
#         'first_name': 'Mark',
#         'last_name': 'Ivanov',
#         'age': 50,
#         'adress': ('г.Москва', 'ул Ленина', 3),
#         'grades': {'math': 5, 'phizika': 4}
#
#     }

# print(person)

# МНОЖЕСТВА (set, frozenset)

# data = set('hello')
# data = {5,6,3,6,3,8,0}
# data.add(67)
# data.update([99,'by'])
# data.remove(5)
# data.clear()
# new_data = frozenset([5,6,3,6,3,8,0,5,6,3,6,3,8,0])
# print(new_data)

# ФУНКЦИИ (def)

# def test_fun():
#     print('hello world', end='')
#     print('!')
#
# test_fun()

# def test_fun(word):
#     print(word)

# test_fun(9)

# def summa(a,b):
#     sum = a + b
#     return sum
#
# rez = summa(34,67)
# rez2 = summa(678,34)
# print(rez)
# print(rez2)

# # поиск минимального элемента в списке
# def minima(spis):
#     min_num = spis[0]
#     for i in spis:
#         if i< min_num:
#             min_num = i
#             return min_num
#
# # поиск максимального элемента в списке
# def maxima(spis):
#     max_num = spis[0]
#     for i in spis:
#         if i > max_num:
#             max_num = i
#     return max_num
#
# # функция сложения максимума и минимума
# def sum12(rez_max, rez_min):
#     s12 = rez_max+rez_min
#     return s12
#
# nums1 = [5,64,37,7,4,55]
# rez_min = minima(nums1)
# rez_max = maxima(nums1)
# rez_sum = sum12(rez_max,rez_min)
#
# print('Минимальное число ', rez_min)
# print('Максимальное число', rez_max)
# print('Сумма минимального и максимального чисел ', rez_sum)

# lambda функция

# функция по подсчету индекса массы тела
# def imt(ves,rost):
#     rez = ves/((rost/100)**2)
#     if rez<16.5:
#         print('Крайний недостаток веса !')
#     if 16.5< rez< 18.4:
#         print('Недостаток веса')
#     if 18.5< rez < 24.9:
#         print('Нормальный вес ')
#     if 25 < rez < 29.9:
#         print('Чрезмерная масса тела ')
#     else:
#         print('Избыток массы тела!')
#
#     return rez
#
# ves = int(input('Введите массу тела в кг '))
# rost = int(input('Введите рост в см '))
# rez = imt(ves,rost)
# print('Ваш индекс массы тела = ', round(rez,2))

# функция по переводу градусов с Фаренгейта по Цельсию
# def convert(far):
#     far = 5/9*(far-32)
#     return far
#
# n = int(input('Введите градус по Фаренгейту '))
# frr = convert(n)
# print(round(frr,2))

# def privet():
#     print('Prosto! ')
#     print('obichnay! ')
#     print('hello ')
#
# privet()

# среднее арифметическое 3-х чисел
# def sred3(a,b,c):
#     rez = (a + b + c)/3
#     return rez
#
# a = int(input('Введите 1 число '))
# b = int(input('Введите 2 число '))
# c = int(input('Введите 3 число '))
#
# sum = sred3(a,b,c)
# print('Среднее арифметическое 3-х чисел = ', round(sum,2))
# def summa(x,y):
#     return x + y
# def func(f,a,b):
#     return f(a,b)
# # v = func(summa,10,4)
# # print(v)
# func(23,45)

# a= input('Kak teba zovut? ')
# print('Privet, ', a)
s = 'Я люблю писать программы!'
# print(len(s)-1)
# print(s[1:])
# print('My'+ s[1:])

# программа проверяет ввели число или строку,потом на четность
# def chet(a):
#     if a.isdigit() == True and isinstance(a,int):
#         if int(a) % 2 ==0:
#             print('Число четное ')
#         else:
#             print('Нечетное число ')
#     else:
#         print('Не число')
#
# a=input('Введите число ')
# (chet(a))

from math import sqrt
# import sys
# print(sys.path)

# ************************************
# РАБОТА С ФАЙЛАМИ

# data = input('введите текст')
# file = open('data/text.txt', 'w')
# file.write(data + '\n')
# file.close()

# file = open('data/text.txt','r')
# # print(file.read(3))
# for line in file:5

#     print(line, end='')
#  file.close()
# ********************************************
# ОБРАБОТЧИК ИСКЛЮЧЕНИЙ
# try:
#     x = int(input('Введите число '))
#     x+=5
#     print(x)
# except ValueError:
#     print('введите лучше число')

# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число '))
#         x+=5
#         print(x)
#     except ValueError:
#         print('введите лучше число')
#
# try:
#     x = 5/1
#     x=input()
# except ZeroDivisionError:
#     print('деление на нолль')
# except ValueError:
#     print('ввели что то не то')
# finally:
#     print('end')
# **************************************************88
# Дано число, введенное с клавиатуры. Определите сумму
# квадратов нечетных цифр  в числе.
# n = int(input('Введи число: '))
# n = str(n)
# for i in range(0,len(n)):
#     print(n[i])
#     s = 0
#     if int(n[i]) % 2 !=0:
#         s = n[i]**2
#         print(s)

# n = 123
#
# new = str(n)
# print(new)
# x = int(new[0])%2
# y = int(new[1])%2
# z = int(new[2])%2
# print(int(new[1])**2+int(new[2])**2)

# import time
# print(time.asctime())
# outer = [1, 2, 3, 4]
# inner = [9, 8, 7, 6]
# for i in outer:
#     for j in inner:
#         print('i = ', i,'j = ', j)
# *******************************************************8
import random

# outer = 3
# inner = 2
# spis = []*outer
#
# for i in range(outer):
#     # n = random.randint(1, 10)
#     spis.append([random.randint(1,10)]*inner)
# print(spis)
# outer = 3
# inner = 2
# spis = []*inner
# for i in range(outer):
#     for j in range(inner):
#         spis[i][j] = random.randint(0,10)
# print(spis)

# *****************************************************************8
# ДВУМЕРНЫЕ МАССИВЫ


# c = 'hello'
# num = list(c)
# for el in b:
#     print(el)

# i = 0
# while i<len(b):
#     print(b[i])
#     i +=1

# c =[8,2,3,5]
# if a == c :
#     print('=')
# else:
#     print('!=')
# a = [8,2,3,5]
# b = ['Tom','Goin','Mark','Yulia']
# b = b.append('Qwe')
# a.append(45)
# people1 =['Moskow','Pariz','Orel','Barcelona','Orel','Sankt']
# people2 = people1.copy()
# people2.append('Sew')
# b = ['Tom','Goin','Mark','Yulia']
# # sorted_people = sorted(people, key=str.upper)
# people3 = b + people1
# print(people3)

# people.insert(2,'Tom')
# people.append('Mark')
# c = ['New York','Sankt','aq']
# people.remove('Orel')
# people.reverse()
# z = max(people)
# if 'Orel' in people:
#     print('yes')

# people = [['Tom', 29], ['Mark', 31], ['Bob', 54], [23, 45]]

# общее количество элементов в списке
# mylist =[[1],[1,2],[2,3,4],[5,5,6,4],[]]
# total =0
# for el in mylist:
#     total = total+len(el)
#     print('длина = ', len(el))
#     print('количество = ',total)
# *************************************
# множества
# users = {'Tom','Mark','Bill','Bob','Tom'}
# user ='Tom'
# if user in users:
#     users.remove(user)
# print(users)
# список из случайных чисел
# import random
# new_num =[random.randint(1,9) for n in range(0,10) ]
# print(new_num)

# x = 47865
# a = x//1000
# q = x//1000//10
# b = x//1000%10
# c = x//100%10
# d = x//10%10
# r = x%10
# print(q, b,c,d,r)
import math
# print(math.trunc(-34.500987654567))
# print(int(-36.544463454353))
# сколько слов в строке
# s = 'у лукоморья дуб зеленый, златая цепь на нем висит'
# s1 = len(s.split(' '))
# print(s1)
# *********************************************
# ИГРА УГАДАЙ ЧИСЛО
# import random
# print('Я задумал число от 1 до 100. Угадай!')
# secret = random.randint(1, 100)
# print(secret)
# attemp =0
# case = 0
# while case != secret:
#     print('Введи число')
#     case = int(input())
#     attemp += 1
#     if case > secret:
#         print('Слишком большое')
#     if case< secret:
#         print('Слишком маленькое')
#     if case == secret:
#         print('Правильно! Угадал с %s попытки '% attemp)
#     if case == 0:
#         print('Загаданное число: ',secret)
#         print('Всего было %s попыток: ' %attemp)
#         break
# *******************************************************
# ИГРА ИГРАЛЬНЫЕ КУБИКИ
# import random
#
# print('Давай бросим кубики ')
# attemp = 0
# myNum = 0
# yourNum = 0
# while attemp < 5:
#     attemp +=1
#     print('Раунд: %s' % attemp)
#     print('Твой бросок: ')
#     shoot1 = random.randint(1,6)
#     time.sleep(2)
#     print(shoot1)
#     print('Мой бросок: ')
#     shoot2 = random.randint(1,6)
#     time.sleep(2)
#     print(shoot2)
#     if shoot1 > shoot2:
#         yourNum +=1
#     if shoot1 < shoot2:
#         myNum += 1
#     print('Счет: '+ str(yourNum) +'  '+ str(myNum))
#     time.sleep(2)
#
# if yourNum > myNum:
#     print('Ты выиграл!')
# elif  yourNum < myNum:
#     print('Я выиграл!')
# else :
#     print('Ничья')
# ******************************************************8
# ВЫВЕСТИ ВСЕ ЧЕТНЫЕ И НЕЧЕТНЫЕ ЧИСЛА ОТ 1 ДО 100
# for i in range(0,100,2):
#     print(i, end=" ")
# print()
# for i in range(1,100,2):
#     print(i, end=" ")
# ***********************************************************8
# week = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
# for day in week:
#     print(day,end=" ")
# *************************************************************
# ИГРА ВЫИГРАЛ В ЛОТЕРЕЮ, ЧЕРЕЗ СКОЛЬКО ЛЕТ ЗАРАБОТАЕШЬ МИЛЛИОН
# import random, math
# capital = int(input('Мой начальный капитал: '))
# print('Ты можешь вложить деньги в банк и заработать еще больше!')
# percent = float(input('Введи процентную ставку: '))
# term = int(input('На какой срок ты вкладываешь деньги: '))
#
#
# for value in range(term):
#     fee = capital*percent/100
#     capital = capital+fee
#
#
# print('Ты заработаешь %s рублей ' % math.floor(capital))
# **********************************************************888
# ПАЛИНДРОМ
# print('text')
# text1 = input()
# text2 =''
# ch = len(text1)
# for i in range(0,ch):
#     text2 +=text1[ch-i-1]
#     print(text2)
# print(text2)
# if text1 == text2:
#     print('Палиндром')
# ***************************************************************888
# import random
#
# a1 = random.randint(10,99)
# a2 = random.randint(10,99)
# symv =['*','+','/','-']
# symv_ran = random.choice(symv)
# if symv_ran == '*':
#     rez = a1*a2
# elif symv_ran == '+':
#     rez = a1+a2
# elif symv_ran == '/':
#     rez = a1/a2
# elif symv_ran == '-':
#     rez =a1 - a2
# print('Первое случайное число: ', a1)
# print('Второе случайное число: ',a2)
# print('Случайный сиxмвол: ' ,symv_ran)
# print('Результат: ', rez)
# *********************************************************
# ты задумывал число, а  компьютер пытался угадывать его.
# Указывая «меньше» или «больше»
import math

# x = 1
# y = 100
# secret = 34
# i = 1
# while True:
#     z = (x + y) // 2
#     print('Ваше число %s ?' % z, 'Напишите: да, больше, меньше')
#     otvet = input()
#
#     if otvet == 'да':
#         print('Я угадал за %s ходов' % i)
#         break
#     elif otvet == 'меньше':
#         y = z
#     elif otvet == 'больше':
#         x = z
#     else:
#         print('Ответ нераспознан')
#         continue
#     i +=1
#     print('Диапозон: ', x, y)
#     z =(y - x) // 2 + x
#     print(z)
#
# *******************************************************************8
# Функция, которая возвращает словарь, содержащий статистику встречаемости элементов
# в последовательности
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c]= d[c]+1
#     return d
#
# s = 'у лукоморья дуб зеленый'
# his = histogram(s)
# print(his)
# **************************************************************
# def total(initial=5,*numbers,**keywords):
#     count = initial
#     for num in  numbers:
#         count = count + num
#     for key in keywords:
#         count = count + keywords[key]
#     return count
# print((total(10,1,2,3,vegetables=50,fruits=100)))

# try:
#     with open ('text.txt', 'r',encoding='utf-8') as file:
#         file.read()
#
# except FileNotFoundError:
#     print('Файл не найден!')

# ****************************************************************
# from mymodule import add_three_numbers as add
# print(add(23,23,0))
#
# import cowsay
# cowsay.cow('hello')
# ****************************************************
# import monsterlab
#
# Frank = monsterlab.Monster('Френки','необычный')
# Frank.show()
#
# Albert = monsterlab.GMonster('Альберт','задумчивый')
# Albert.show()
# Sigmund = monsterlab.SMonster('Зигмунд','веселый')
# Sigmund.show()
# __________________________________________________
# class Address():
#     name = ''
#     line1 = ''
#     line2 = ''
#     city = ''
#     state = ''
#     zip = ''
#
# homeAddress = Address()
# homeAddress.name = 'Ivanov Ivan'
# homeAddress.line1 = '701 N.C.Street'
# homeAddress.line2 = 'Carver Science Building'
# homeAddress.city = 'Indiana'
# homeAddress.state = 'IA'
# homeAddress.zip = '50125'
#
# vacationHomeAddress = Address()
# vacationHomeAddress.name = 'Ivanov Ivan'
# vacationHomeAddress.line1 = '1122 Main Street'
# vacationHomeAddress.line2 = ''
# vacationHomeAddress.city = 'Panama City Beach'
# vacationHomeAddress.state = 'FL'
# vacationHomeAddress.zip = '32407'
#
# def printAddress(address):
#     print(address.name)
#     if (len(address.line1)>0):
#         print(address.line1)
#     if (len(address.line2)>0):
#         print(address.line2)
#     print(address.city+' '+address.state+' '+address.zip)

# printAddress(homeAddress)
# print()
# printAddress(vacationHomeAddress)

# class Dog():
#     age = 0
#     name = ''
#     weight = 0
#     def __init__(self,newname):
#         self.name=newname
#         # print('родилась новая собака!')
#     def setname(self,newname):
#         self.name=newname
#     def getname(self):
#         return self.name
#     def bark(self):
#         print(self.name, 'говорит гав')
# myDog =Dog('Spotik')
# # myDog.name = 'Spot'
# # myDog.weight = 20
# # myDog.age = 1
# print(myDog.getname())
# myDog.setname('Sharik')
# # myDog.bark()
# print(myDog.getname())
#
# **************************************************
#
# class Dog():
#     age =0
#     name = ''
#     weight = 0
#     def __init__(self,newname):
#         self.name = newname
#         # print('new dog!')
#     def setname(self,newname):
#         self.name=newname
#     def getname(self):
#         return self.name
#     def bark(self):
#         print(self.name, 'govorit gav!')
#
# myDog = Dog('Spot')
# # myDog.age =3
# # myDog.name ='Spoti'
# # myDog.weight =20
# #
# # myDog.bark()
# print(myDog.name)
# print(myDog.getname())
# myDog.setname('Sharik')
# print(myDog.getname())

# class Animal():
#     name = ''
#     def __init__(self,newname):
#         self.name=newname
#         print('Родилось животное ',self.name)
#
#     def setname(self,newname):
#         self.name = newname
#     def getname(self):
#         return self.name
#     def makeNoise(self):
#         print(self.name, 'говорит Грррр')
#     def eat(self):
#         print(self.name, 'Ням-ням!')
#
# myAnimal = Animal('Dino')
# myAnimal.getname()
# print(myAnimal.getname())
# myAnimal.setname('Dinozavr')
# print(myAnimal.getname())
#
# myAnimal.eat()
# myAnimal.makeNoise()


# class Cat():
#     name = ''
#     color = ''
#     weight =0
#     def meow(self):
#         print(self.name, 'говорит Мяу')
#
# myCat = Cat()
# myCat.name = 'Kisa'
# myCat.color = 'orange'
# myCat.weight = 5
#
# myCat.meow()
# ********************************************************88
# class Monster():
#     def __init__(self,name,character):
#         self.name = name
#         self.character = character
#     def type(self):
#         return 'Monstr'
#
#     def show(self):
#         print('Имя: ',self.name)
#         print('Характер: ',self.character)
#         print('Тип: ', self.type())
#
# Frank = Monster('Frenki','neobichn')
# Frank.show()
#
# Frank2 = Monster('Сэмш','обычный')
# Frank2.show()
#
# class GMonster(Monster):
#     def type(self):
#         return 'Сын монстра'
#
# class SMonster(Monster):
#     def type(self):
#         return 'Сын монстра'
#
# Albert = Monster('Альберт','задумчивый')
# Albert.show()
# Zigmund = Monster('Зигмунд','веселый')
# Zigmund.show()
#
# class StringVar():
#     def __init__(self,stroka):
#         self.str = stroka
#     def setstr(self,newstr):
#         self.str = newstr
#         self.strdl = len(newstr)
#         print('Длина строки: ',self.strdl)
#
#     def getstr(self):
#         print(self.str)
#
# myVar = StringVar('у лукоморья')
# print(myVar.str)
# print()
# myVar.setstr('Дуб зеленый златая цепь на дубе том')
# myVar.getstr()
#
# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def addxy(self):
#         print('Сумма: ', self.x + self.y)
#
#     def printAddxy(self):
#         print(self.z)
#
# MYxy = Point(120,130)
# MYxy.addxy()

#
# class Parrot:
#     species = 'птица '
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     def singl(self,song):
#         return "{} поет {}".format(self.__name, song)
#     def setnewname(self,newname):
#         self.__name = newname
#     def getname(self):
#         return self.__name
#     def dance(self):
#         return 'танцует'
#
# Kesha = Parrot('Кеша',10)
# # print(Kesha.singl('pop'))
# # # Kesha.name = 'Test'
# # Kesha.setnewname('Питон')
# # print(Kesha.getname())
#
# class Pingvin(Parrot):
#     def __init__(self,name, age):
#         super().__init__(name, age)
#         print('Пингвин родился')
#     def dance(self):
#         print('Пингвины танцуют')
#
# peggy = Pingvin('Peggy',12)
# peggy.dance()
# print(peggy.singl('kino'))
# print(peggy.getname())
# peggy.setnewname('Pink')
# print(peggy.getname())
# class Bird:
#     def __init__(self):
#         print('Птица готова')
#     def whoisThis(self):
#         print('Птица')
#     def swim(self):
#         print('Плывет быстрее')
#
# class Pengvin(Bird):
#     def __init__(self):
#         super().__init__()
#         print('Пингвин готов')
#     def whoisThis(self):
#         print('Пингвин')
#     def run(self):
#         print('Бежит быстрее')
#
# peggy = Pengvin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
# **********************************************************
# for i in range(5):
#     print(i, end=' ')
#     for j in range(5):
#         print(j,end=' ')
#     print('*')
# *******************************************************
# x=5
# y=12
# print('Значение х = {} , у = {}'.format(x,y))
# print('Значение х = %s , у = %s'%(x,y))
# print('Я люблю  {0}, {1}'.format('хлеб','масло'))
#
# num = eval(input('Введите число '))
# print(num+'qwe')

# def outer_function():
#     global a
#     a = 20
#
#     def inner_function():
#         global a
#         a = 30
#         print("inner, a = ", a)
#
#     inner_function()
#     print('outer , a = ', a)
#
# a = 10
# outer_function()
# print('Global a = ',a)

# for i in 'stroka':
#     # print('начало цикла ', i)
#     if i == 'o':
#         continue
#     print('конец цикла ', i)
#
# def greet(*names):
#     """Эта функция приветствует человека"""
#
#     for i in names:
#         print('Привет,',i)
# greet(12,67,87)
#
# x ='global'
# def foo():
#     global x
#     x=x*2
#     print('x внутри функции ',x)
#
# print('х вне функции ',x)
# foo()

# def outer():
#     x = 200
#
#     def inner():
#         nonlocal x
#         x = 10
#         x = x*2
#         print('вложенная функция ',x)
#
#     inner()
#     print(x)
# outer()

# LAMBDA ФУНКЦИИ

# double = lambda x,y:(x+y)*2
# print(double(5,3))

# mylist = [2,5,3,7,8,9,3,5,7,6,9]
# # newlist = list(filter(lambda x:x%2==0,mylist))
# # newlist1 = list(filter(lambda x:x%2!=0,mylist))
# # print(newlist)
# # print(newlist1)
# newlist2 =list(map(lambda a:a*2,mylist))
# print(newlist2)

# x = 1
# def foo():
#     x = 20
#
#     def bar():
#         # global x
#         x = 25
#         print(x)
#
#     print('до вызова bar ',x)
#     bar()
#     print('после вызова bar ',x)
#
# foo()
# print('х в глобальной области ',x)

# print(1.1+2.2)
# import decimal
# print(0.1)
# print(decimal.Decimal(0.1))

# import fractions
# print(fractions.Fraction(1.5))
# print(fractions.Fraction(5))
# print(fractions.Fraction(1,3))

# s = 'дуб зеленый'
# for i in range(len(s)):
#     print('Элемент %s строки: ' %i, s[i])
# count=0
# for el in s:
#     if el == 'е':
#         count +=1
# print(count)
# print('д' in s)
# s = 'дуб зеленый'
# for el in enumerate(s):
#     print(el, end=' ')
# s1 = list(enumerate(s))
# print(s1[4r])

# s = 'у лукоморья дуб зеленый и большой'
# s1 = s.split(' ')
# s1[0]='Опа'
# s = s.replace('дуб','ива')
# s = s.replace('у','В')
# print(s)

# l = ['мама','мыла','раму']
# s = ' '
# s1 = s.join(l)
# s1 = s1.replace('мама','Маша')
# print(s1)
# print(l)
# s = 'у лукоморья дуб зеленый'
# s1 = s.split(' ')
# s = s.replace('у','*Вон*')
# print('это строка: ', s)
# print(s)
# s1 = s.index('лук')
# print(s1)
# print('''He said, "What's there?"''')
# print("He said, \"What's there?\"")
# print('Это вообще \nочень \nхороший \nпример')
# defa = '{a},{b},{c}'.format(b='Ваня',a='Петя',c='Катя')
# print(defa)
# n = [8,3,6,8,5]
# n[0]=9
# n[2:4]=1,7
# n.append(56)
# n.extend(23,34)
# m = [6,5,4,3,5,6]
# del m[3:]
# print(m)
# s = ['hello', 'car', 'people',12,23]
# s.pop()
# print(s)
# pow = [2**x for x in range(10) if x%2==0]
# print(pow)
#
# pow2=[]
# for x in range(10):
#     if x%2==0:
#         pow2.append(2**x)
# print(pow2)

# l = [12,45,23,'car','cat']
# a = 'car' in l
# print(a)

# l = ['яблоко','вишня','арбуз','груша']
# for el in range(len(l)):
#     print('%s -й элемент ' %el, l[el])

# СЛОВАРИ
# myDict = {}
# myDict = {1:'apple',2:'bananas',3:'mango',4:'ananas',5:[2,3,4]}
# myDict[6]='kat'
# myDict.pop[5]
# print(myDict.popitem())
# print(myDict)
# for el in myDict.items():
#     print(el)
# print(list(sorted(myDict.keys())))

# squares = {x: x*x for x in range(10) if x%2==0}
# print(squares)
# squares = {}
# for x in range(10):
# #     if x%2==0:
#         squares[x] = x*x
# print(squares)
# print(36 in squares)
# squ = {1:1,4:56,5:67,7:90,9:67}
# for i in squ:
#     print(squ[i], end=' ')

# print(len(squ))
# print(all(squ))
# l ={}
# for el in range(10):
#     if el%2 == 0:
#         l[el] = el*el
# print(l)
#
# print()
# l1 = {x:x*x for x in range (6)}
# print(l1)

# КОРТЕЖИ
# my_tuple = 3, 4.6, 'dog'
# print(my_tuple)
#
# a,b,c = my_tuple
# print(a)
# print(b)
# print(c)
# my1 =(99,88,77)
# print(my1)
# a,b,c = my1
# print(a)
# print(b)
# print(c)
# my_tupl = ('hello')
# print(type(my_tupl))
# my_tupl2 = 'hello',
# print(type(my_tupl2))
# l = ('hello','car','cat',(12,34),[99,88])
# l1 = l[4]
# l1[0]='Dima'
# print(l1)
# l = (1,2,3)
# print(l)
# l = (1,2,3)
# l1 = (4,)
# c = l + l1
# print(c)
# print(l*2)
# del l1
# print(l1)
# l = ('hello','car','cat',(12,34),[99,88])
# print(l.count([99,88]))
# print(l.index([99,88]))
# my_tupl = ('h','e','l','l','o')
# print('h' in my_tupl)
# count =0
# for el in range(len(l)):
#     print('Это %s элемент кортежа: ' %el, l[el] )
#     count += 1
# print('Всего элементов в кортеже: ', count)
# МНОЖЕСТВА
# my_set = set({2,4,6,8})
# print(my_set)
# my_set1 ={'hello', 45,'bob',45,'bob'}
# my_set1.add('yulia')
# my_set1.update({3,46,78})
# my_set1.discard('bob')
# my_set1.discard(3)
# my_set1.remove(45)
# my_set1.discard(33)
# print(my_set1)

# my_set =set('Приветмир!')
# my_set1 =set('здравствуйте')
# s1 =set({1,2,3})
# s2 =set({3,5,6})
# # print(my_set)
# print(type(my_set))
# print(s1.union(s2))
# print(my_set&my_set1)
# print(my_set.difference(my_set1))
# print(s2.difference(s1))
# a = {1, 2, 3, 4, 5, 5, 1, 2}
# b = {4, 5, 6, 7, 8}
# a.add(999)
# b.clear()
# print(a)
# print(a.difference_update(b))
# print(2 in a)
# for i in a:
#     print(i, end=' ')
# for i in enumerate(a):
#     print(i)
# print(sorted(a))

# favorite_lang = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
#     }
# for name in sorted(favorite_lang.keys()):
#     print(f"{name.title()}")

# for language in favorite_lang.values():
#     print(language.title())
# alien0 ={'color':'green','points':5}
# alien1 ={'color':'red','points':10}
# alien2 ={'color':'yellow','points':15}
# aliens=[alien0,alien1,alien2]
# for al in aliens:
#     print(al)
# aliens =[]
# for i in range(30):
#     new_alien ={'color':'red','points':10,'speed':'slow'}
#     aliens.append(new_alien)
#
# for i in aliens[0:3]:
#     if i['color']=='green':
#         i['color'] ='yellow'
#         i['points']=10
#         i['speed']='medium'
#     elif i['color']=='yellow':
#         i['color']='red'
#         i['points'] = 15
#         i['speed'] = 'fast'
#
# print('Количество созданных пришельцев:', len(aliens))

# l =['edward','join','bob','phill']
# for i in sorted(l):
#     print(i.title())
# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese'],
#     'ingriduints':['bekon','grib','salo','ananas']
#     }
#
#
# for el in pizza['toppings']:
#     print(el)
# print()
# for i in pizza['ingriduints']:
#     print(i)

# favorite_lang = {
#     'jen':['python','c++'],
#     'sarah':['c'],
#     'edward':['ruby','python'],
#     'phil':['python','go','haskell']
#     }
# for i in favorite_lang['phil']:
#     print(i)
# import this
# s = ['yulia','bob','smit','python']

# magicians = ['alice','david','rim','polia']
# for i in magicians:
#     print(f"Дорогая {i.title()},вы были приглашены на обед \n" )
# pizza = ['peperoni','chizz','moreprodukti']
# for i in pizza:
#     print(f"I like {i.title()} ")

# numbers = list(range(1,10,2))
# numbers1 = list(range(0,10,2))
# print(numbers)
# print(numbers1)

# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# squares =[x**2 for x in range(1,11)]
# print(squares)
# for x in range(1,1000001):
#     print(x)

# million = [x for x in range(1,1000001)]
# sum_million = sum(million)
# print(sum_million)

# nechet =[x for x in range(1,21,2)]
# print(nechet)
# print()
# nec = []
# for x in range(1,21,2):
#     nec.append(x)
# print(nec)

# three = []
# for x in range(3,30,3):
#     three.append(x)
# print(three)
# kub = [x**3 for x in range(1,10)]
# print(kub)
# print()
#
# kub1 = []
# for x in range(1,10):
#     kub1.append(x**3)
# print(kub1)
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# for i in players[:3]:
#     print(i.title())
# igrok =[23,45,67,49,78]
# igrok.sort()
# print(igrok)
# print('вывести первые 3 минимальных элемента: ',igrok[:3],end=' ')
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# my_players = players
# players.append('tim')
# my_players.append('rim')
# for i in players:
#     print(i)
# print()
# print(my_players)

# dimens = (200,50)
# print('Original:')
# for i in dimens:
#     print(i)
# dimens = (400,100)
# print('Modify:')
# for i in dimens:
#     print(i)
# menu = ('шашлык','торт', 'салат', 'бутерброды', 'вино')
# for i in menu:
#     print(i.title())
# menu = ('шашлык','торт', 'салат')
# print(menu)

# cars = ['audi','bmw','subaru','hendai','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# age =45
# if age <= 4:
#     price =0
# elif age <= 18:
#     price = 100
# elif age > 65:
#     price = 250
# else:
#     price = 500
# print('Ваш билет %s рублей' %price)
# req = ['peperoni','chees','mush']
# if 'peperoni' in req:
#     print('peperoni')
# if 'chees' in req:
#     print('chees')
# if 'mus'in req:
#     print('mush')
# print('finised pizza!')
# alien_color = ['green','yellow','blue','red']
# a ='yellow'
# if a in alien_color:
#     ball=5
# elif 'yellow' in alien_color:
#     ball =10
# elif 'red' in alien_color:
#     ball =15
# print('Вы заработали %s баллов!' %ball)
# age = 82
# if age<2:
#     print('младенец')
# elif age <=4:
#     print('малыш')
# elif age <=13:
#     print('ребенок')
# elif age <=20:
#     print('подросток')
# elif age <=65:
#     print('взрослый')
# else:
#     print('пожилой')
# fruits = ['bananas','mango','orange','avokado']
# a ='orange'
# if a in fruits:
#     print('Я люблю ', a)

# requast_topping =['mushrooms','green peppers','exstra chees']
# for i in requast_topping:
#     if i=='green peppers':
#         print('Извитните нет')
#     else:
#         print('Добавлен ', i)
# print('Пицца готова')

# req_toppings =['mushrooms']
# if req_toppings:
#     for i in req_toppings:
#         print('add')
#     print('finised pizza!')
# else:
#     print('baz pizza?')
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Add {requested_topping}')
#     else:
#         print('Sorri!')
# print('Finised pizza')

# clients =['yulia','dima', 'admin','yana']
# if clients:
#     for client in clients:
#         if client == 'admin':
#             print('Привет %s, когда обновишь статусы?'%client)
#         else:
#             print('Здравствуйте, %s уважаемый ' %client)
# else:
#     print('Тут нет пользователей! Где все?')
# current_users = ['YULIA','Dima', 'Admin','yana']
# current_users_copy = current_users[:]
# current_users_copy.extend(['yulia','dima'])
#
# for i in current_users_copy:
#     print(i.lower())
#
# print(current_users_copy)
# new_users = ['yulia','dima','boba','aleks']
#
# for new_user in new_users:
#     if new_user in current_users_copy:
#         print('Выберите новое имя!',new_user)
#     else:
#         print('Имя доступно', new_user)
# byte =[x for x in range(1,10)]
# print(byte)
# for i in byte:
#     if i == 1:
#         print(f"{i}st")
#     elif i == 2:
#         print(f"{i}nd")
#     elif i == 3:
#         print(f"{i}rd")
#     else:
#         print(f"{i}th")
# client = ['Yuila','DIMA','BOB','JoIn','BoRIc','MAKs']
# client1 =[]
# for i in client:
#     client1.append(i.lower())
# print('New list ', client1)
# print('List ', client)
#
# men = 'Boric'
# if men.lower() in client1:
#     print('Это имя занято!')
# else:
#     print('Имя свободно!')
# alien_0={'color':'green', 'points':5}
# new_points =alien_0['points']
# print(f"Вы заработали {new_points} баллов!")
# alien_0['x position']=0
# alien_0['y position']=25
# print(alien_0)
# alien ={}
# alien['color']='red'
# alien['points']=5
# alien['speed']='medium'
# print(alien)
# alien['color']='blue'
# print(alien)

# alien_0 ={'color':'green', 'points':5,'x position':0,'y position':25,'speed':'medium'}
# if alien_0['speed'] == 'slow':
#     x_increment =1
# elif alien_0['speed'] == 'medium':
#     x_increment =2
# else:
#     x_increment =3
# alien_0['x position']=alien_0['x position']+x_increment
# print(f"New position {alien_0['x position']}")
# alien_0['speed']='fast'
# del alien_0['color']
# print(alien_0)

# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phill':'python'}
# language = favorite_language['sarah']
# print(f"Любимый язык программирования Сары {language.title()}")

# for k in favorite_language.keys():
#     print(f'Участвовали в опросе: {k.title()}')
# friends = ['phill','sarah']
# for name in favorite_language.keys():
#     # print(name.title())
#     if name in friends:
#         lan = favorite_language[name].title()
#         print(name.title(), 'I see you love ',lan)
# if 'jen' in favorite_language.keys():
#     print('I am here')
#
# clients = ['Yuila','DIMA','BOB','JoIn','BoRIc','MAKs']
# new_client = 'dima'
# new_client_lowered = new_client.lower()
# for client in clients:
#     print(client)
#     if new_client_lowered == client.lower():
#         print('Такой пользователь уже есть')
#         break

# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phill':'python'}
# # for i in sorted(favorite_language.keys()):
# #     print(i.title())
# for i in set(favorite_language.values()):
#     print(i)
# men = {
#     'first_name':'yulia',
#     'last_name':'solovjeva',
#     'age':38,
#     'city':'Almetevsk',
#     'ulisa':'Zaslonova',}
# print(f" Здравствуйте, меня зовут {men['first_name'].title()} {men['last_name'].title()}.\n Мне {men['age']} год")
# for key,value in men.items():
#     print(f" \nКлюч {key}: значение {value}")
# ******************************************************************
# river_country = {
#     'nile': 'egypt',
#     'Bosphorus':'turkey',
#     'volga':'russia',
#     'amazon':'brazil',
# }
# for river, country in river_country.items():
#     print(f"Река - {river.title()}: страна - {country.title()}")
# for river in river_country.keys():
#     print(river.title())
# print()
# for country in river_country.values():
#     print(country.title())
# ********************************************************************
# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phill':'python',
#     'ilya':'pascal',
#     'nil':'basic',
#     'yana':'c'
# }
# print('Список людей: ')
# for peopl in favorite_language.keys():
#     print(peopl.title())
#
# peopl_opros = ['natali','yana','ilya','svetlana']
#
# favorite_peopl =[]
# for peopl in favorite_language.keys():
#     favorite_peopl.append(peopl)
# print(favorite_peopl)
#
# for peopl in peopl_opros:
#     if peopl in favorite_peopl:
#         print(peopl.title(), 'Вы прошли опрос!')
#     else:
#         print(peopl.title(),'Пройдите опрос')
# *******************************************************************
# alien0={'color':'green', 'points':5}
# alien1={'color':'yellow', 'points':10}
# alien2={'color':'red', 'points':15}
# # aliens =[alien0,alien1,alien2]
# aliens = []
# for alien in range(1,31):
#     new_alien = {'color':'green', 'points':5}
#     aliens.append(new_alien)
# print(aliens[:3])
# print(len(aliens))
#
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color']='yellow'
#         alien['points']=10
#         alien['speed']='medium'
# print(aliens)

# pizza = {'crust':'thick',
#          'toppings':['mushrooms','exstra cheese']}
# for top in pizza['toppings']:
#     print(top)
# ****************************************************
# favorite_language = {'jen':['python','c'],
#                      'sarah':['c'],
#                      'edward':['ruby','pascal','go'],
#                      'bob':['python'],
#                      'edik':['ruby','go'], }
#
# for name,languages in favorite_language.items():
#     print('Name - ',name.title())
#     for language in languages:
#         print(language)
#
#     print('Количество ЯП: ', len(languages))
#     if len(languages) == 1:
#         print('Один любимый язык')
#     print()
# ***********************************************************************
# users = {
#         'aienstein': {
#             'first':'albert',
#             'last':'enstein',
#             'location':'turkey',},
#         'mcurei':{
#             'first':'marle',
#             'last':'curei',
#             'location':'brazil',
#         },
# }
# for user,value in users.items():
#     print(f"\nUserName: {user.title()}")
#     full_name = f"Full_name: {value['first'].title()} {value['last'].title()}"
#     loc = f"Location: {value['location'].title()}"
#     print(f"\t {full_name}")
#     print(f"\t {loc}")
# dog = {'name':'Sharik','age':5,'vladeles':'Tim'}
# cat = {'name':'KisaMeow','age':2,'vladeles':'Tim'}
# popugai ={'name':'Kesha','age':10,'vladeles':'Rimma'}
#
# pets =[dog,cat,popugai]
#
# for pet in pets:
#     print(pet.items())
# print(f"{pet['name']}, {pet['age']}, {pet['vladeles']}")
# ******************************************************************
# alien1 = {'color':'green','points':5}
# alien2 = {'color':'red','points':10}
# del alien2['color']
# print(alien2)
# # p=alien1['points']+alien2['points']
# # print('Я заработал %s очков' %p)
# if alien1['color'] == 'green':
#     print('Это старое значение',alien1['points'])
#     alien1['points'] = alien1['points']+5
#
# print('Это новое значение = ',alien1['points'])
# user = { 'first_name':'sergei',
#          'last_name':'pushkin',
#          'job':'poet',
#          'city':'mockow'}
# user['last_name']='zverev'
# full_name = f"Полное имя: {user['first_name'].title()} {user['last_name'].title()}"
# location = f"\nАдрес: {user['city'].title()} "
# print(full_name,location)
# **************************************************************************************
# users = {'bob':[12,45,23],
#          'natali':[45,11,12,56,33],
#          'yana':[5,],
#          'ilya':[2,1] }
# for name,value in users.items():
#     print(name.title(),' :',value)
#     count =0
#     for i in value:
#         count +=1
#     print('Количество любимых чисел: ',count)
#     print('Сумма чисел: ',sum(value))
#     print('Максимальное: ',max(value))
#     print('Минимальное: ',min(value))
#     if max(value) == min(value):
#         print('max == min ')
#     print()
# **********************************************************************************
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phill': 'python',}
#
# friends =['phill','sarah']
#
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(favorite_languages[name])
#         language = favorite_languages[name].title()
#         print(name.title(), 'Твой любимый язык программирования - ',language)

# ************************************************************************88
# участвовал ли конкретный человек в опросе. если не участвовал в опросе составить
# новый список людей
# favorite_languages = {
#      'jen': 'python',
#      'sarah': 'c',
#      'edward': 'ruby',
#      'phill': 'python',}
#
# friends =['boric','phill','sarah','yana','bob']
# new_friends = []
# for name in sorted(friends):
#     if name in favorite_languages.keys():
#         print(name.title(), 'Прошел опрос!')
#     else:
#         new_friends.append(name.title())
#         print(name.title(),'Пройдите опрос!')
# print('Список людей для опроса: ',new_friends)
# ***********************************************************************
# car = input('Какую машину хотите взять напрокат?')
#
# avto  = ['subaru','bmw','toyota','nissan','vaz']
# if car in avto:
#     print('Скоро привезем вам машину')
# else:
#     print('К сожалению эта машина недоступна! ')
# *********************************************************************88
# table = [2,3,4,6,8,10]
# a =int(input('На сколько мест хотите забронировать стол?'))
# if a > 8:
#     print('Придется подождать')
# else:
#     print('Ok')

# n=int(input('Введите число '))
# if n % 10 ==0:
#     print('Кратно 10')
# else:
#     print('Обычное число')

# num = 0
# while num <= 5:
#     print(num)
#     num +=1


# ***********************************************************************************
# new_user = {}
# for i in range(3):
#     new_user[i] = {'name':'nikoly','age':45,'city':'moskow'}
# print(new_user)
# ******************************************************************************888
# promt ='Введите сообщение или quit для выхода из программы'
# message =''
# while message!='quit':
#     message=input(promt)
#
#     if message!='quit':
#         print(message)
# active =True
# while active:
#     message =input(promt)
#     if message == 'quit':
#         active=False
#     else:
#         print(message)
# promt ='Введите ваш любимы город или введите quit для выхода из программы'
#
# while True:
#     city = input(promt)
#     if city == 'quit':
#         break
#     else:
#         print(f'I love go to {city.title()}')

# num = 0
# while num <10:
#     num +=1
#     if num %2 == 0:
#         continue
#     print(num)

# top = 'Введите топпинг для пиццы или quit для выхода'
# active = True
# while active:
#     mes = input(top)
#     if mes == 'quit':
#         active=False
#     else:
#         print(mes)
#         print('Это дополнение включено в заказ!')

# *************************************************************************

# price = 0
# while True:
#     age = int(input('Введите ваш возраст'))
#     if age <3:
#         price =0
#         print('Бесплатно')
#
#     elif age <12:
#         price = 10
#         print('Ваш билет %s долларов ' %price)
#
#     else:
#         price = 15
#         print('Ваш билет %s долларов ' % price)
#         break

# age = int(input('Введите ваш возраст'))
# price = 0
# message = "долларов билет"
#
# while age !=0:
#     if age < 3:
#         price = 0
#         print('Бесплатно')
#         age = 0
#     elif age <12:
#         price = 10
#         print(price,message)
#         age = 0
#     else:
#         price = 15
#         print(price, message)
#         age = 0

# unconfirmed_users = ['alice','brian','caandace','bob']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print(current_users)
#     confirmed_users.append(current_users)
# print()
# for user in confirmed_users:
#     print(user.title())

# import time
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#
# for i in range(0, 200000):
#     pets.append('cat')
#
# start_time = time.time()
# while 'cat' in pets:
#     pets.remove('cat')


# while True:
#     try:
#         i = pets.index('cat')
#         pets.pop(i)
#     except ValueError:
#         break

# print( pets )
#
# print("--- %s seconds ---" % (time.time() - start_time))
# ***********************************************************
# import random

# pets = []
# i=0
# while i <10:
#     ran = random.randint(10, 90)
#     pets.append(ran)
#     i +=1
#
# print(pets)
# m=max(pets)
# print(m)
# pets.remove(m)
# print(pets)
# ****************************************************************
# responses = {}
# hobbi = {}
# polling_active = True
# while polling_active:
#     name = input('Введите имя ')
#     response = input('На какую гору ты хотел бы подняться?')
#     country = input('Какую страну хотел бы посетить?')
#     more = input('На каком море хотел бы поплавать?')
#     responses[name.title()] =hobbi
#     hobbi['gora'] = response
#     hobbi['coutry'] = country.title()
#     hobbi['more'] = more
#     repeat = input('Продолжаем опрос? yes/no ?')
#     if repeat == 'no':
#         polling_active=False
# print(responses)
# ***********************************************************************88

# promt = "Здесь представлен очень преочень длинный текст чтобы показать" \
#         "как можно делить строку на две "
# print(promt)

# users = ['alice','yana','ilya','mark','boric']
# new_users =[]
# while users:
#     user = users.pop()
#     if user == 'ilya' or user == 'mark':
#         continue
#     new_users.append(user.title())
# print(sorted(new_users))

# users = ['Mark','alice','yana','ilya','MARK','boric','mARk']
# for name in users:
#     if name.lower() == 'mark':
#         users.remove(name)
# print(users)

# while 'mark' in users:
#     users.remove('mark')
# print(users)

# **********************************************8

# sandwich_orders =['ostri','pastrami','vegan','pastrami','postni','bekon','pastrami']
# finised_sandwich =[]
# while sandwich_orders:
#     san =sandwich_orders.pop()
#     finised_sandwich.append(san)
#     print(san, 'Сэндвич добавлен в заказ')
# print('Ваш заказ собран! ',finised_sandwich)
# sandwich_orders =['ostri','pastrami','vegan','pastrami','postni','bekon','pastrami']
# print(sandwich_orders.count('pastrami'))
# finised_sandwich =[]
# print('pastrami закончился!')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
# ****************************************************************
# ОТПУСК МЕЧТЫ
# otpusk ={}
# location = {}
# active = True
# while active:
#     name = input('Как вас зовут?')
#     local = input('Где вы хотели бы провести отпуск?')
#     today = int(input('На сколько дней хотите взять отпуск?'))
#     child = input('Сколько у вас детей?')
#     ret = input('Какой отдых интересует:активный или расслабленный?')
#     repeat =input('Хотите продолжить ? yes/no')
#     otpusk[name] = location
#     location['local']=local
#     location['today']=today
#     location['child']=child
#     location['ret']=ret
#     if repeat == 'no':
#         active=False
# print(otpusk)
# ****************************************************************888
# def person(first,last,age=0):
#     user = {'first':first.title(), 'last':last.title()}
#     if age:
#         user['age']=age
#     return user
#
# name = person('yulia','solovjeva')
# print(name)
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# while True:
#     f_name =input('First name')
#     if f_name=='q':
#         break
#     l_name = input('Last name')
#     if l_name == 'q':
#         break
#     name = get_formatted_name(f_name,l_name)
#     print(name)

# def city_country(country,city):
#     cc = {'country':country.title(),'city':city.title()}
#     return cc
# city = city_country('turkey','alanya')
# print(city)
# while True:
#     country = input('vvedi strany')
#     if country == 'q':
#         break
#     city = input('vvedi gorod')
#     if city == 'q':
#         break
#     m =city_country(country,city)
#     print(m)

# users = ['alice','yana','mark','anatoly']
#
# def name_users(users):
#     for name in users:
#         print('Приветствую тебя мой дорогой друг %s! ' % name.title())
#
# name_users(users)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# def pechat(unprinted_designs,completed_models):
#     while unprinted_designs:
#         design = unprinted_designs.pop()
#         completed_models.append(design)
#     print('New list: ',completed_models)
#
# def vivod(completed_models):
#     for i in completed_models:
#         print(i)
#
# pechat(unprinted_designs[:],completed_models)
# vivod(completed_models)
# print(unprinted_designs)
# # *********************************************************************
# messages = ['Как дела?','Что делаешь?','Что нового?','Как поживаешь?','Че почем?']
# def show_message(messages):
#     while messages:
#         message = [messages.pop()]
#         print(message)
#
# show_message(messages)
# ************************************************************************
# messages = ['Как дела?','Что делаешь?','Что нового?','Как поживаешь?','Че почем?']
# send_messages = []
# def send_message(messages):
#     while messages:
#         message = messages.pop()
#         send_messages.append(message)
#     print(send_messages)
#
# send_message(messages[:])
# print(messages)
# def build_profile(first,last,**user_info):
#     user_info['first_name']=first
#     user_info['las_name'] =last
#     return user_info
# user_profile = build_profile('albert','einstein',location='riceton',field='physics')
# print(user_profile)

# sandwich=['vegan','peperoni','ostri']
#
# def sadw(*toppings):
#     print(toppings)
#
# sadw('qw','er',3)
# ************************************************************************
# КЛАССЫ

# class Dog():
#     def __init__(self,name,age):
#         self.name =name
#         self.age =age
#     def sit(self):
#         print(f' Собака {self.name} садится по команде')
#     def roll_over(self):
#         print(f' Собака {self.name} перекатывается по команде')
#
# my_dog =Dog('willie',5)
# print(my_dog.name, my_dog.age)
# my_dog.sit()
# my_dog.roll_over()
#
# your_dog =Dog('lucy',12)
# print(your_dog.name, your_dog.age)
# your_dog.sit()
# your_dog.roll_over()
# ********************************************************************************88
# class Restaurant():
#     def __init__(self,restoran_name,cuisine_type):
#         self.restoran_name =restoran_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#     def describe_restoran(self):
#         print('Название ресторана: ',self.restoran_name)
#         print('Тип национальной кухни: ', self.cuisine_type)
#     def open_restoran(self):
#         print(f"Наш рестрован {self.restoran_name} открыт" )
#     def set_number_served(self, new_number_value):
#         if new_number_value < 0:
#             raise ValueError('Новое значение не может быть меньше 0')
#         self.number_served = new_number_value
#     def  increment_number_served(self,new_incr_value):
#         if (new_incr_value + self.number_served) < 0:
#             raise ValueError('Результат меньше 0')
#         self.number_served += new_incr_value
#
# class IceCreamStand(Restaurant):
#     def __init__(self,restoran_name,cuisine_type):
#         super().__init__(restoran_name,cuisine_type)
#         self.flavors  = ['vanil','shokolate','plombir']
#     def get_flavors(self):
#         print('Список сортов мороженого:')
#         for i in self.flavors:
#             print(i)
#
# my_icecream = IceCreamStand('Ice Cream Solovjeva','cream')
# my_icecream.get_flavors()
#
# restauran = Restaurant('Solovjeva','грузинская')
# # restauran.number_served=4
# # restauran.set_number_served(5)
# # restauran.increment_number_served(-6)
# print(restauran.number_served)
# restauran.describe_restoran()
# restauran.open_restoran()

# **********************************************************************************
# class User():
#     def __init__(self,first,last,age,email,login):
#         self.first =first
#         self.last =last
#         self.age =age
#         self.email =email
#         self.login = login
#     def describe_user(self):
#         full_name=f"Имя пользователя: {self.first} {self.last}"
#         print(full_name.title())
#         print(f"Возраст: {self.age}")
#         print(f"Email: {self.email}")
#     def greet_user(self):
#         print(f"Приветствую, уважаемый {self.first} {self.last}")
#     def increment_login_attempts(self):
#         self.login +=1
#     def reset_login_attempts(self):
#         self.login = 0
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить']
#
#     def show_privileges(self):
#         print('Набор привилегий администратора:')
#         for i in self.privileges:
#             print(i)
#
#
# class Admin(User):
#     def __init__(self,privileges):
#         # super().__init__(first,last,age,email,login)
#         self.privileges = Privileges()
#
# my_admin = Admin('admin')
# my_admin.privileges.show_privileges()
# my_user = User('yulia','solovjeva',38,'solovjevayulia1985@dmail.com',0)
# my_user.describe_user()
# my_user.greet_user()
# my_user.increment_login_attempts()
# my_user.reset_login_attempts()
# print(my_user.login)

# **************************************************************************
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometr_reading =0
#     def get_descriptive_name(self):
#         """возвращает отформатированное описание"""
#         long_name=f" {self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odometr(self):
#         """выводит пробег машины"""
#         print(f"Пробег машины: {self.odometr_reading} км")
#     def update_odometr(self,mileage):
#         """устанавливает на одометре заданное значение
#         при попытке обратной прокрутки изменение отклоняется"""
#         if mileage >= self.odometr_reading:
#             self.odometr_reading = mileage
#         else:
#             print('Нельзя откатывать одометр!')
#     def incremetn_odometr(self,km):
#         self.odometr_reading +=km

# my_car = Car('audi','a4',2019)
# print(my_car.get_descriptive_name())
# my_car.update_odometr(10)
# # my_car.incremetn_odometr(34)
# my_car.update_odometr(9)
# my_car.read_odometr()
# print()

# class Battery():
#     def __init__(self,battery_size=100):
#         self.battery_size =battery_size
#     def describe_battery(self):
#         print(f"Мощность аккумулятора {self.battery_size} kmh")
#
#     def get_range(self):
#         """выводит приблизительный запах хода аккумулятора"""
#         if self.battery_size == 75:
#             zapac_hod = 260
#
#         elif self.battery_size == 100:
#             zapac_hod = 315
#         print(f'Запах хода аккумулятоа {zapac_hod} км\ч')
#     def uprade_battery(self):
#         if self.battery_size == 75:
#             zapac_hod = zapac_hod+100
#
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
#
# my_tesla = ElectricCar('tesla', 'model s',2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.uprade_battery()
# my_tesla.battery.get_range()
# *************************************************************
# RANDOM
# from random import randint
# print(randint(1,9))
# from random import choice
# play = ['alice','yana','ilya','ivan','natali']
# c = choice(play)
# print(c)
# *************************************************
# from random import randint
# class Die():
#     """ игра кубики, sides - количество граней кубика"""
#
#     def __init__(self,sides):
#         self.sides = sides
#     def roll_die(self):
#         play = randint(1,self.sides)
#         return play
#
# my_kubik = Die(10)
# for i in range(1,11):
#     print('Бросок %s: ' %i, my_kubik.roll_die())
# ********************************************************************
# ЛОТЕРЕЯ
# import random
# loterei = ['a',12,'d',34,'l',4,5,9,'t',56,43,67,'r',2,77]
# priz =[]
# while len(priz) <= 4:
#         priz.append(random.choice(loterei))
# print('Выигрышная комбинация: ', priz)
#
# my_iter=0
# while True:
#     ticket = []
#     while len(ticket) != len(priz):
#         ticket.append(random.choice(loterei))
#     if priz == ticket:
#         print('Через сколько комбинаций выпал выигрыш:',my_iter)
#         break
#     else:
#         my_iter += 1
# *************************************************************************
# with open('pi.txt.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# my_file = 'C:/Users/Юля/Desktop/testik.txt'
# with open(my_file) as file_object:
#     contents =file_object.read()
# print(contents)
# *************************************************************
# встречается ли в числе пи мой день рождения?
# filename ='pi.txt.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string +=line.rstrip()
# print(pi_string)
# print('Длина числа Пи: ',len(pi_string))
# # birthday = input('Введи свой день рождения ддммгг')
# # if birthday in pi_string:
# #     print('Твой день рождения есть в числе Пи')
# # else:
# #     print('Твоего дня рождения нет в числе Пи')
# c = pi_string.count('3')
# print(p)
# ******************************************************
# filename ='text.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     # contents = file_object.read()
# for line in lines:
#     if 'Python' in line:
#         line = line.replace('Python','C')
#     print(line)
# ***********************************************************
# filename = 'zapis.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("New text\n")
#     file_object.write("I love creating apps that can run a browser.\n")
# **********************************************************
# ГОСТЬ
# name = input('Введите ваше имя: ')
#
# with open('guest.txt','a') as file_object:
#     file_object.write(name)
#     file_object.write('\n')
# # ********************************************************
# with open('guest.book.txt','w') as file_object:
#     line = 0
#     while line<5:
#         name = input('Введите ваше имя: ')
#         file_object.write('Welcome  '+ name.title())
#         file_object.write('\n')
#         line +=1
# *******************************************************
# with open('otvet.txt','w') as file_object:
#     active = True
#     while active:
#         otvet = input('Почему вам нравится программировать? ')
#         file_object.write(otvet)
#         file_object.write('\n')
#         if otvet == 'q':
#             active =False
# ***************************************************************88
# play = [3,4,34,2,43,4,54,3,4,23,44,40]
# print('Сколько чисел с цифрой 4 встречается в списке,'
#       'вывести колво и список')
# four = []
# count = 0
# for i in play:
#     z = i // 10
#     r = i % 10
#     if i == 4 or z == 4 or r == 4:
#         count +=1
#         four.append(i)
#
# print('Количество: ',count)
# print('Список: ',four)
# *******************************************************************
# n = int(input())
# power = 1
# i = 0
# while i<= n:
#     print(str(i) + ' ' + str(power))
#     power = 2*power
#     i +=1
#
# n1 = int(input('Введите число: '))
# i1 = 0
# while i1 <= n1:
#     print('2 в степени',i1, ' = ',2**i1)
#     i1 +=1
# ***********************************************************
# name = {'solojeva':'yulia','ivanov':'sergei'}
# last ={'petrov':'petr'}
# l = list(name.items())
# print(type(l))
# word = 'hello'
# letter_counts = {letter:word.count(letter) for letter in word}
# print(letter_counts)
# def commentary(color):
#     if color == 'red':
#         return 'It ic tomato'
#     elif color == 'green':
#         return 'It is green pepper'
#     elif color == 'bee purple':
#         return 'i dont know'
#     else :
#         return 'never of the color '+color
#
# c = commentary('gree')

# try:
#     print(5/1)
# except ZeroDivisionError:
#     print('Делить на ноль нельзя!')
#
# while True:
#     first_number = input('\n Введите первое число ')
#     if first_number =='q':
#         break
#     last_number = input('\n Введите второе число ')
#     if last_number == 'q':
#         break
#     try:
#         rez = int(first_number)/int(last_number)
#     except ZeroDivisionError:
#         print('Деление на ноль!')
#     else:
#         print(rez)
# ***************************************************888
# def count_words(filename):
#     '''подсчет приблизительных слов в текстовом файле'''
#     try:
#         with open (filename, encoding='utf-8') as f:
#             contens =f.read()
#     except FileNotFoundError:
#         # print('Файл не найден')
#         pass
#     else:
#         words = contens.split()
#         num_words = len(words)
#         print(num_words)
#         # print(words)
#
# filename = ['atom.txt','pobed.txt','mobi_dick.txt']
# for name in filename:
#     count_words(name)

# **********************************************************
# title = 'Alice in wonderland'
# print(title.split())
# *******************************************************
# упражнение 10.6

# while True:
#     first = input('Введи первое число ')
#     if first == 'q':
#         break
#     last = input('Введи второе число ')
#     if last == 'q':
#         break
#     try:
#         rezult = int(first) + int(last)
#
#     except ValueError:
#         print('Нужно ввести ЧИСЛО!')
#     else:
#         print(rezult)
# **********************************************************
#  Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt.
#  Напишите программу, которая пытается #  прочитать эти файлы и выводит
#  их содержимое на экран. Заключите свой код в блок try-except для перехвата исключения
#  FileNotFoundError и вывода понятного сообщения об отсутствии файла
#
#
# with open('cats.txt','w') as f:
#     i=0
#     while i<=4:
#         cat = input('Введи имя кошки')
#         contens = f.write(cat+'\n')
#         i +=1
# with open('dogs.txt','w') as f:
#     i=0
#     while i<=4:
#         cat = input('Введи имя собаки ')
#         contens = f.write(cat.title()+'\n')
#         i +=1
#
# def cats_dogs(filename):
#     try:
#         with open(filename,encoding='utf-8') as f:
#             contens = f.read()
#
#     except FileNotFoundError:
#         print('Файл не найден!')
#     else:
#         return contens
#
# filename = ['dogs.txt','cats.txt']
# for name in filename:
#     print(cats_dogs(name))
# ****************************************************************
# упр 10.10 подсчет кол-ва вхождений слова в тексте из файла
# def file_count(filename,name):
#     try:
#         with open(filename,encoding='utf-8') as f:
#             contens = f.read()
#     except FileNotFoundError:
#         print('Файл не найден!')
#     else:
#         word_count = contens.lower().count(name)
#         print(word_count)
#
# filename =['genrik.txt','cats.txt']
# name = 'уильям'
# for n in filename:
#     file_count(n,name)
# *******************************************************************
# ФУНКЦИЯ JSON.DUMP

# import json
# numbers =[2, 3, 6, 8, 11, 45]
# filename ='numbers.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)
# filename ='numbers.json'
# with open(filename) as f:
#     numbres = json.load(f)
#     print(numbres)

# import json
# name = ['alice','nataly','boric','timofei','mark']
# filename ='name_j.json'
# with open(filename,'w') as f:
#     json.dump(name,f)
# filename ='name_j.json'
# with open(filename) as f:
#     nam =json.load(f)
#     print(nam)

# import json
# username = input('What is your name?')
# filename = 'username.json'
# with open(filename,'w') as f:
#     json.dump(username,f)
#     print(f"We'll remember you when you come back {username}")

# import json
# filename = 'username.json'
# with open(filename) as f:
#     name = json.load(f)
#     print(f"Доброе пожаловать {name}!")
# программа запрашивает у пользователя имя при первом
# запуске программы и «вспоминает» его при повторных запусках.

# import json
# def get_stored_username():
#     '''получает хранимое имя пользователя'''
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def new_username():
#     '''запрашивает новое имя пользователя'''
#     username = input('What is your name?')
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username
# def greet_user():
#     username = get_stored_username()
#     if username:
#         print(f'Welcome {username}')
#     else:
#         username = new_username()
#
# greet_user()
# **********************************************************************
# прежде чем выводить приветствие спросить правильно ли определено имя
# import json
# def my_name():
#     filename ='my_number.json'
#     user = input('Введите ваше имя ')
#     with open(filename,'w') as f:
#         json.dump(user.title(),f)
#         print('Запомнили имя')
#
# def get_my_number():
#     filename ='my_number.json'
#     try:
#         with open(filename) as f:
#             user = json.load(f)
#     except FileNotFoundError:
#         print('Файл не найден!')
#     else:
#         vopros = input(f'Ваше имя {user}? yes/no')
#         if vopros == 'yes':
#             print(f"Добро пожаловать {user}")
#         else:
#             print('Перезапишем:')
#             my_name()
# my_name()
# get_my_number()
# ************************************************************************

# def get_formatted_name(first,last):
#     full_name = f"{first} {last}"
# #     return full_name.title()
# x1 =8
# y1 =8
# x2=1
# y2=8
# if ((x1+1==x2) and (y1==y2)) or ((x1-1==x2) and (y1==y2))\
#         or ((x1==x2) and(y1-1==y2)) or ((x1==x2)and(y1+1==y2))\
#         or ((x1+7==x2)and(y1==y2)) or ((y1+7==y2)and(x1==x2))\
#         or ((x1-7==x2)and(y1==y2)) or ((y1-7==y2)and(x1==x2)):
#     print('yes')
# else:
#     print('no')
# c=0
# maxx=0
# active=True
# while active:
#     n = int(input())
#     if maxx < n:
#         maxx = n
#         c+=1
#
#     if n == 0:
#         active=False
#
# print(maxx)
# n=10
# f1=f2=1
# if n == 0:
#     print(0)
# else:
#     for i in range(2,n):
#         f1,f2=f2,f1+f2
#
#     print(f2,end=' ')
# m1=0
# m2=0
# c=0
# active=True
# while active:
#     n = int(input())
#     m1=n
#     if m2 == m1:
#         m2 = n
#         c+=1
#
#     if n == 0:
#         active=False
# print(c)
# поиск второго минимума
# 3 4 6 2
# n = int(input())
# m1 = n
# m2 = 0
# while n > 0:
#
#     if n < m1:
#         m2 = m1
#         m1=n
#
#     elif n>m1 and n<m2:
#         m2 = n
#
#     n = int(input())
#
# n=int(input('Введите количество элементов в списке '))
# s=[]
# for i in range(n):
#     new_s = int(input())
#     s.append(new_s)
# print(s)
# for i in range(n):
#     if i%2==0:
#         print(s)

# a = [0] * int(input())
# for i in range(len(a)):
#     a[i] = int(input())
# print(a[i],end=' ')

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i<5:
#         print(a[i],end=' ')
# l='Kто и шутя и скоро пожелаетъ ПИ узнать число — ужъ знаетъ'
# l1=l.split()
# print(l1)
# p =3,1415926536
# for i in l1:
#     print(len(i),end=' ')
# print (int('3') * str(3+4))

# a =35
# c='14.8'
# print(a+int(c))
# # lst = 'I,like,to,sort'
# print(lst)
# s=lst.split(',')
# print(s)
# a= list(lst)
# a[0]='Me'
# print(a, end=' ')
# print()
# z=' '.join(a)
# print(z)
# sorted_lst=sorted(lst.split())
# print(' '.join(sorted_lst))

# a.pop()
#
# lst=[1, 5, [3, 1], 2, 1, [[1], 2] ]
# del lst
# print(lst)
# print(str(1 + 2))
# print(int('1' + '2'))

# for i in a:
#     if i%2==0:
#         print(a, end=' ')
# print()
# for i in range(len(a)):
#     print(f"{i}элемент списка=",i,a[i])
# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)
# z= '12345'
# a=s.find('1')
# print(a)
# s =input()
# a = s.split()
# print(a)
# a = ['green','red','blue']
# print(' '.join(a))
# b =[1,2,3]
# print(' '.join(i for i in b))
# n=10
# # k=3
# a=[]
# for i in range(n):
#     a.append('I')
# # a=''.join(a)
# print(a)
#
# b= [[3,6],[2,5],[8,10]]
# for j in b:
#     n1,n2 = j
#     for i in range(n1,n2+1):
#         a[i-1]='.'
# print(''.join(a))
# import requests
# req = requests.get('https://pythonist.ru')
# req.status_code
#
# import math
# a='0 0 1 1'
# a = a.split()
#
# print(a)
# def distanseXY(x1,y1,x2,y2):
#     s=math.sqrt((x1-x2)**2+(y1-y2)**2)
#     return s
#
# d= distanseXY(x1=int(a[0]),y1=int(a[1]),x2=int(a[2]),y2=int(a[3]))
# print(d)


# def capitalize(s):
#     return s.title()
# z=capitalize(s)
# print(z)
# def capitalize(word):
#     first_letter_small = word[0]
#     first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
#     return first_letter_big + word[1:]
# word = 'not a hero unless you die'
# source = input().split()
# res = []
# for word in source:
#     res.append(capitalize(word))
# print(' '.join(res))

# small =word[0]
# big =chr(ord(small))-ord('a')+ord('A')
# print(big)
# word = 'not a hero unless you die'
# def emphasise(txt):
#     return ' '.join(w[0].upper()+w[1:].lower() for w in txt.split())
# a = emphasise(word)
# print(a)

# print(word)
# word_list=word.split()
# print(word_list)
# for i in word_list:
#     print(i.capitalize())


# def power(a,n):
#     if n==1:
#         return a
#     elif n==0:
#         return 1
#     elif n%2==0:
#         rezult = power(a,n//2)
#         return rezult * rezult
#     elif n%2!=0:
#         rezult = power(a,n//2)
#         return rezult * rezult * a
#
# a=2
# n=0
# z=power(a,n)
# print(z)
# stek=[]
# for i in range(1,11):
#     stek.append(i)
#     print(f'{i} -ый элемент добавлен')
# print(stek)
#
# for i in range(len(stek)):
#     stek.pop()
#     print(f'{i} -ый элемент удален')
# print(stek)

# s = 'harry potter'
# l=len(s)
# for i in range(len(s)):
#     print(s[:-i])
# def greeyings(s):
#     print(s)
#     if len(s)==0:
#         return
#     else:
#         greeyings(s[:-1])
# greeyings(s)

# def faktorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# a=faktorial(5)
# print(a)
# def faktorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# a=faktorial(5)
# print(a)
# def faktorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*faktorial(n-1)
# s='*'
# s1=' '
# print(s)
# for i in range(20,1,-1):
#     print(s*i)
# oge= [['9А',
#        [45,90,78,89,57,100,100,89,97,80,76,68,90,99,98,97,95],
#        [66,78,98,56,78,90,87,67,98,95,97,87,98,98,87,98,98,87,68,89,100]],
#       ['9Б',[98,88,78,90,87,67,98,95,97,60,98,98,87,98,98,70,68,89,100],
#        [98,87,67,98,95,76,87,98,98,87,94,98,70,68,89,100]],
#       ['9В',[98,56,78,90,87,67,98,76,97,87,56,98,87,98,98,87,68,89,100,76],
#        [98,56,67,98,95,75,87,98,98,87,98,98,87,68,89,100]]]
# for class_9 in oge:
#     for i in (1,2):
#         average_mask = round(((sum(class_9[i]))/(len(class_9))),2)
#         if i==1:
#             math=average_mask
#         else:
#             rus=average_mask
#     print(f"{class_9[0]} класс, средний балл по математике {math},русскому {rus}")

# for j in 1,2:
#     for i in 'a','b':
#         print(i, end='')
#         print(j, end='')

# for letter in 'Мама мыла 4 рамы, а Мила ела 3 Баунти ':
#     if letter.isdigit():
#         print(letter, end=' ')
#
# for i in range(8):
#     if i>3:
#         break
# print(i)
# for i in 'СЛОВО':
#     if i=='О':
#         pass
#     print(i, end=('*'))

# def treg(x,y,z):
#     pass
#
#
# x=12
# y=33
# z=67
# rez =treg(x,y,z)
# print(rez)
# print([1,2,3] == [1,2,3], [5,7,4] > [5,7,3,7], [2,3,4] != [4,3,2])
#
# for i in [0, 1, 2, 3]:
#     print(i)
# print()
# for i in range(0, 4,1):
#     print(i)
# print()
# for i in range(0, 3,1):
#     print(i)
# print()
# for i in range(0, 4):
#     print(i)

# for i in range(1, 6):
# #     print('Python')
# lst1 = [1, 2, 3]
# lst2 = [4, 5]
# x
# lst1[3:]= lst2
# print(lst1)
# x = 475
# h = 1
# m = 55
# m1 = (x % 60+m)%60
# h1 = x // 60 + h + (x % 60 + m) // 60
#
# # if m1>60:
# #     m2=m1//60
# #     print(m1//60)
# print(h1)
# print(m1)
# g=2003
# if 1900<=g<=3000:
#     if g%4==0 and g%100!=0 or g%400==0:
#         print('Високосный')
#     else:
#         print('Обычный')
# import math
# a=3
# b=4
# c=5
# p = (a+b+c)/2
# s=math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)
# import random
# z=['*','+','-','/','//','%','**']

# n=int('090234')
# a=n%10+n%100//10+n%1000//100
# b=n%10000//1000+n//1000//100+n//1000//10%10
# if a==b:
#     print('Счастливый')
# else:
#     print('Обычный')

# s=0
# while True:
#     i = int(input())
#     s=s+i
#     if i==0:
#         break
# print(s)
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)
# a1=[]
# b1=[]
# while i<=9:
#    s=a*i
#    s1=b*i
#    a1.append(s)
#    b1.append(s1)
#    # print(f"{a}x{i}={s}")
#    i+=1
#
#
# print(a1)
# print(b1)
# for i in a1:
#     for j in b1:
#         if i==j:
#             print(i,end=' ')

# while True:
#     x=int(input())
#     if x <10:
#         continue
#     if x>100:
#         break
#     print(x)
# ТАБЛИЦА УМНОЖЕНИЯ
# a=7
# b=10
# c=5
# d=6
#
# for j in range(c, d + 1):
#     print(f"\t{j}", end=' ')
# print()
#
# for i in range(a,b+1):
#
#     print(i, end="")
#
#     for j in range(c,d+1):
#         print(f"\t{i*j}",end=' ')
#     print()
# ********************************************************
# a=-5
# b=12
# s=0
# con=0
# for i in range(a,b+1):
#     if i%3==0:
#         s=s+i
#         con+=1
# print(s/con, end=' ')
# ***********************************************************
# s='acGgtGttat'.lower()
#
# print(s)
# c=s.count('g')
# g=s.count('c')
#
# print(((c+g)/len(s))*100)
# ***************************************************************
# s='aaaa'
# c=0
# for i in range(1,len(s)):
#     if s[i-1]==s[i]:
#         c+=1
#
#
#     else:
#         c=1
#     print(f"{s[i]}{c}",end=' ')
# print(s[i-1]+str(i+1), end=' ')
# **********************************************************
# c=0
# s = 'aaaabbсaa'
# for i in range(len(s)):
#     if s[i-1]==s[i]:
#         c+=1
#         # print(f"{s[i]}{c}",end=' ')
#     else:
#         print(f"{s[i-1]}{c}", end=' ')
#
#         c=1
# print(s[i-c]+str(c),end=' ')
# *******************************************************************
# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
# *********************************************************
# a = '4 -1 9 3'.split()
# s=0
# for i in a:
#    s+=int(i)
# print(s)
# ********************************************************8888
# a= '1 3 5 6 10'.split()
#
# # print(a)
# b=[]
# if len(a)==1:
#     print(' '.join(a))
# else:
#     for i in range(0,len(a)-1):
#         b.append(int(a[i-1])+int(a[i+1]))
#     b.append(int(a[-2])+int(a[0]))
#
#     print(*b,sep=' ')
# **************************************************************************88
# a='1 1 1 1 1 2 2 2'.split()
# b = []
# c=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             c+=1
#             if c>=1:
#                 b.append(a[i])
#                 c=0
#
# b.sort()
# print(*b, sep=' ')
# a='1 1 1 1 1 2 2 2'.split()
#
# for i in a:
#     z=a.count(i)
#
#     if z!=1:
#         b.append(i)
#     elif b.count(i)>1:
#         b.pop(i)
# print(b)
# *********************************************************
# n= 0
# s=0
# kv=0
# while True:
#     n=int(input())
#     s+=n
#     kv=kv+n**2
#     if s==0:
#         print(kv)
#         break
# ********************************************************************
# если элемент в списке встреччается более одного раза
# a='4 8 0 3 4 2 0 3'.split()
# # a = input().split()
# print(a)
# b=[]
# for i in range(len(a)):
#     c=a.count(a[i])
#     if c>1:
#         if a[i] not in b:
#             b.append(a[i])
#
# b.sort()
# print(*b, sep=' ')
# *************************************************************************
# Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов
# последовательности должна отобразить программа. На выходе ожидается последовательность
# чисел, записанных через пробел в одну строку.
# # Например, если n = 7, то программа должна вывести 1 2 2 3 3 3
# n=1
# z=0
# x=0
# v=0
# total=0
# if n == 1:
#     print(1)
# for i in range(1, n):
#     print(i)
#     if i < (n-total):
#         k = i
#     else:
#         k=n-total
#     q=((str(i)+' ')*k)
#     if total<=n:
#         print(q, end='')
#         total+=i
#     else:
#         break


# *********************************************************************
# a = [int(s) for s in '5 8 2 7 8 8 2 4'.split()]
# b=9
# for i in range(len(a)):
#     if b==a[i]:
#         print(i,end=' ')
# if b not in a:
#     print('Отсутствует')
# ********************************************************************
# def fib(n):
#     if n<3:
#         return 1
#     return fib(n-1)+fib(n-2)
# rezult = fib(4)
# print(rezult)

# def nod(x,y):
#     for i in range(x,0,-1):
#         if x%i==0 and y%i==0:
#             return i
# n=3
# m=2
# n1=n//nod(n,m)
# m1=m//nod(n,n)
# print( n1,m1)

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# # for i in a:
# #     for j in i:
# #         print(j,end=' ')
# #     print()
#
# for row in a:
#     print(' '.join([str(elem) for elem in row ]))

# a=[[3,4],[0,3,2,4],[2,3,5,5],[5,1,2,3]]
# maxx=0
#
# for i in a:
#     for j in i:
#         # if a[i][j]>maxx:
#         #     maxx=a[i][j]
#         if j==3:
#             print(j*3,end=' ')
#     print()

# ***************************************************************
# a='1 2 3'.split()
# b='4 3 2'.split()
# print(len(set(input().split()).intersection(set(input().split()))))
# *********************************************
# a='82 54 91 100 70 33 88 14 52 48 56 20 63 16 22 23 30 8 84 75 45 95 51 98 4 86 78 24 5 77 76 18 97 10 17 66 2 43 61 53 21 69 19 39 7 11 72 40 79 57 68 96 80 71 67 13 99 83 35 27 28 73 36 6 25 55'.split()
# b='c 6 87 36 64 49 19 72 62 29 22 82 7 17 1 73 54 30 9 66 61 95 55 28 86 39 3 42 74 60 93 2 52 78 34 51 32 94 11 37 26 23 69 58 35 14 84'.split()
# x = [int(i) for i in '82 54 91 100 70 33 88 14 52 48 56 20 63 16 22 23 30 8 84 75 45 95 51 98 4 86 78 24 5 77 76 18 97 10'.split()]
# y = [int(i) for i in '10 2 77 90 43 75 25 24 5 21 4 70 83 68 8 92 81 57 27 67 48'.split()]
# x1=set(x)
# y1=set(y)
# z=sorted(x1.intersection(y1))
# print(*z,sep=' ')
# c1=sorted(c)
# print(c1.sort())
# *************************************************************************************8
# встречалось ли число ранее в последлвательности
# a = [int(s) for s in '1 2 3 2 3 4'.split()]
# print(a)
# before = set()
# for num in a:
#     if num in before:
#         print('YES')
#     else:
#         print('NO')
#         before.add(num)
# ******************************************************************
# nm=[int(s) for s in input().split()]
# a=set()
# b=set()
# for i in range(nm[0]):
#     x=int(input())
#     a.add(x)
# for j in range(nm[1]):
#     y=int(input())
#     b.add(y)
# c =a.intersection(b)
# print(len(c))
# print(*c,sep=' ')
#
#
# z=a.difference(b)
# print(len(z))
# print(*z,sep=' ')
#
# v=b.difference(a)
# print(len(v))
# print(*v,sep=' ')
# *******************************************************
# def f(x):
#     if x<=2:
#         return 1-(x+2)**2
#     elif -2<x<=2:
#         return -x/2
#     elif x>2:
#         return (x-2)**2+1
#
# x=float(input())
# n=f(x)
# print(n)
# *****************************************************
# n=int(input())
# l1=int(input())
# s1=set()
# s2=set()
# s3=set()
# for i in range(l1):
#     x1=input()
#     s1.add(x1)
# l2=int(input())
# for j in range(l2):
#     x2=input()
#     s2.add(x2)
# l3=int(input())
# for i in range(l1):
#     x3=input()
#     s3.add(x3)

# s1= {'Russian','English','Japanese'}
# s2={'Russian','English'}
# s3={'English'}
#
# rez1=s1.intersection(s2)
# rez2=rez1.intersection(s3)
# print(len(rez2))
# print(*rez2,sep=' ')
# ************************************************
# def modify_list(l):
# l1=[]
# for elem in range(len(lst)):
#
#     if lst[elem]%2!=0:
#         print('el1=',elem)
#         lst.remove(elem)
#     # else:
#         # print('el2=', elem)
#         # l1.append(elem//2)
# *****************************************************************
#       0   1  2  3  4
# lst = [2, 3, 4, 45, 36]
#
# for i in range(len(lst)-1,-1,-1):
#     if lst[i]%2!=0:
#         lst.pop(i)
#     else:
#         lst[i]=lst[i]//2
#
#
# print(lst)

# **********************************************************
# КОЛИЧЕСТВО СЛОВ В ТЕКСТЕ
# n=int(input())
# text=[]
# for i in range(n):
#     s=input().split()
#     text+=s
#
# text_set=set(text)
# txt_len=len(text_set)
# print(text)
# print(txt_len)
# ************************************************************************
# n=5
# a=[]
# for i in range(n):
#     a.append(i)
# print(a)
#
# b=list(range(1,n))
# print(b)
# def f(x):
#     return x+3
#
# def g(function,x):
#     return function(x)*function(x)
# print(g(f,7))

# for i in range(5,10):
#     if i%2==0:
#         i=i*2
#     else:
#         i+=1
#     print(i,end=' ')
# print()
# a=[x*2 if x%2==0 else x+1 for x in range(5,10)]
# print(a)
# b1 = [i for i in range(1,11)]
# print(b1)
# b=[i*2 if i%2!=0 else i+10 for i in range(1,11)]
# print(b)
# c = list(map(lambda x,y:x**2 + y**2,b1,b))
#
# print(c)

# a= [i for i in range(1,15)]
# print(a)
# # b=[i+100 for i in a ]
# # print(b)
# def f(x):
#     return  x+100
# a1 = map(f,a)
# for i in range(1,15):
#     print(next(a1))

# a = list(map(lambda s:s*10,'hello'))
# print(a)
# b=lambda x:x+10
# print(b(10))
# import random
# a = list(random.randint(1,10) for i in range(1,11))
# b = [random.randint(20,30) for i in range(1,11)]
# c = list(map(lambda x,y:x+y, a,b))
# print(a)
# print(b)
# print(c)
# def f(x,y):
#     return x//2+y*2
# c1= list(map(f,a,b))
# print(c1)
# a=[]
# n=3
# for i in range(n):
#     n=int(input())
#     a.append(n)
# print(a)
#
# c=list(map(lambda x:x*100,a))
# print(c)
# c1 =[int(input()) for x in range(4)]
# print(c1)
# n=10
# m=3
# z=lambda x,y: x-ylist_of_tuples = [('Player 1', 32),
#    ('Player 2', 27),
#    ('Player 3', 48),
#    ('Player 4', 15)]
# print(z(n,m))
# z1=lambda x:x**2
# print(z1(4))

# list_of_tuples= [('Player 1', 32,2),('Player 2', 27,1),('Player 3', 48,3),('Player 4', 15,4)]
# sorted_tup =sorted(list_of_tuples,key=lambda x:x[2])
# print(sorted_tup)
#
# x= lambda a,b:a if a>b else b
# print(x(23,6))
# y = lambda a,b,c:a+b+c if a>0 else a+b-c
# print(y(-4,6,5))

# weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri']
# days=filter(lambda day: day if len(day)==3 else '', weekdays)
# for d in days:
#     print(d)
# lst = [4, 67, 43, 2, 90, 11, 100, 7, 500]
# l=list(filter(lambda item: item if item>100 else '',lst))
# print(l)

# lst = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
# # l=list(filter(str.isdigit,lst))
# # print(l)

# numb = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# a=list(map(lambda x:x+100,numb))
# print(a)

# n1 = [i for i in range(1,11)]
# n2 = [j for j in range(11,21)]
# # print(n1)
# print(n2)
# c= map(lambda x:x if x%5==0 else '' ,n2)
# for i in c:
#     print(i)

# p='phone'
# a=[]
# for i in p:
#     a.append(i)
# print(a)
# b=[x for x in p]
# print(b)
# phone_list = ["apple", "samsung", "sony", "nokia", "lg", "huawei"]
# new_list=list()
# for elem in phone_list:
#     if 'e' in elem:
#         new_list.append(elem)
# print(new_list)
# new_list=list(elem for elem in phone_list if 'e' in elem)
# print(new_list)
# new2=list(elem for elem in phone_list if len(elem)>5)
# print(new2)
# new3=list(elem.title() for elem in phone_list )
# print(new3)
#
# a= [i+100 if i%2==0 else i+1 for i in range(5,10)]
# print(a)
# b = [i+10 for i in range(5,10)]
# print(b)
# c=list(map(lambda x,y:x+y,a,b))
# print(c)
# import math
# c=list(map(lambda x:math.log(x),a))
# print(c)
# import random
# a=[random.randint(1,10) for i in range(10) ]
# print(a)
# l1 = [i for i in range(1,6)]
# print(l1)
# l2=[1,7,3,9,5]
# print(l2)
# l3=[]
# # for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(i)
# print(l3)
#
# for j in l1:
#     [l3.append(i) for i in l2 if i==j in l2]
# print(l3)
# l_new=[]
# for j in l2:
#     l3=list(filter(lambda x: x==j ,l1))
#     print(l3)
#     l_new=l_new+l3

# password=input('vvedi parol')
# i=0
# while i<len(password):
#     if password[i] in ('@','*') or (len(password)>8):
#         password=input('no')
#         i+=0
#     else:
#         i+=1
# print('ok')
# print(password)
# text='''Недавно мы сообщали, что у нас появились \
# на свет трое пингвинят.\
# Спустя несколько недель \
# нас осчастливили еще двое пингвинят.\
# Мама Умка и папа Нокс \
# – молодая пара, у них \
# впервые появились птенцы.\
# Первый вылупился 12 марта, \
# второй – 14-го.\
# Сейчас с птенцами все хорошо, \
# они отлично себя чувствуют.\
# Оба весят уже больше 3 килограммов, \
# - говорится в сообщении.'''
# l=text.split()
# print(l)
# l_max=len(l[0])
# i=0
# count=0
# while i<len(l):
#
#     if len(l[i]) > l_max:
#         l_max=len(l[i])
#         count=i
#     i+=1
# print('Длинное слово= ',l[count])
# print('Индекс= ',count)
# print('Длина слова= ',l_max)
# s = 0
# m = 123
# while m > 0:
#     d = m % 10
#     print(d)
#     s = s + d
#     print(s)
#     m = m // 10
#     print(m)
#
# print(123//10)
# line =1
# while line<=5:
#     while pos<line:
#         print(((' ')*(4-pos)),('*')*(pos+1))
#         pos+=1
#     line+=1
# *************************************
# В единственной строке записан текст. Для каждого слова из данного
# текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# l='one two one tho three'.split()
# d={}
# ret = []
# for key in l:
#     if key not in d:
#         d[key]=0
#     else:
#         d[key]+=1
#     ret.append(d[key])
# print(*ret,sep=' ')

# **************************************************************
# определить синоним
# c=[]
# n=int(input())
# for i in range(n):
#     v=input().split()
#     c=c+v
#
# d= {c[i]:c[i+1] for i in range(0,len(c),2)}
# print(d)
# l=input()
# if l in d.values():
#     for key,values in d.items():
#         if l==values:
#             print(key)
# else:
#     if l in d.keys():
#         print(d.get(l))
# **********************************************************
# n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input()])
# ***************************************************
# ЗАДАЧА ПРО ВЫБОРЫ США
# n=int(input())
# d={}
# for i in range(n):
#     kand,golos=input().split()
#     if kand not in d:
#         d[kand]=golos
#     else:
#         d[kand]=int(d.get(kand))+int(golos)
# for k,v in sorted(d.items()):
#     print(k,v )
# **********************************************************
# n=int(input())
# d={}
# col=1
# for i in range(n):
#     l=input().split()
# for word in l:
#     if word not in d:
#         d[word]=col
#     else:
#         d[word]+=1
# b=[]
# for k,v in d.items():
#     b.append(v)
#     m=max(b)
# if m == v:
#     print(k)


# ************************************************************
# d={2:[9]}
# key=4
# value=6
# if key in d:
#     d[key].append(value)
# else:
#     if 2*key not in d:
#         d[2*key]=[value]
#     else:
#         d[2*key].append(value)
# print(d)
# ***********************************************************
# l = 'a aa abC aa ac abc bcd a'.lower().split()
# print(l)
# d={}
# for key in l:
#     col=l.count(key)
#     if key not in d:
#         d[key]=col
# for k,v in d.items():
#     print(k,v)
# *********************************************************************
# def f(x):
#     return x+10
# d={}
# n=int(input())
# for i in range(n):
#     x=int(input())
#     if x not in d:
#         d[x]=f(x)
#     print(d[x])
# *****************************************************************
# n=1
# d={}
# col=1
# for i in range(n):
#     l='apple orange banana banana orange'.split()
# for word in l:
#     if word not in d:
#         d[word]=col
#     else:
#         d[word]+=1
# b=[]
#
# for k,v in d.items():
#     b.append(v)
#
# m=max(b)
# c=[]
# for k,v in d.items():
#     if m == v:
#         c.append(k)
# for elem in c:
#     if ord()
# print(c)
# *******************************************************************************
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

# n=int(input())
# d={}
# for i in range(n):
#     v=input().split()
#     key=v[0]
#     for i in range(1,len(v)):
#         if key not in d:
#             d[key]=[v[i]]
#         else:
#             d[key].append(v[i])
# for i in range(int(input())):
#     gorod=input()
#     for k_g,v_g in d.items():
#         for i in range(len(v_g)):
#             if gorod == v_g[i]:
#                 print(k_g)

# **************************************************
# n=2
# d={}
# l=input().split()
# while len(l)==3:
#     fio = l[0]
#     tovar=l[1]
#     kol=int(l[2])
#     if fio not in d:
#         d[fio]={}
#     if tovar not in d[fio]:
#         d[fio][tovar]=kol
#     else:
#         d[fio][tovar]+=kol
#     l = input().split()
# print(d)
# spisok=sorted(d.keys())
# for fio in spisok:
#     print(f'{fio}:')
#     spis_tov=sorted(d[fio].keys())
#     print(spis_tov)
# ***********************************************************************************
# with open('data.txt') as f_data:
#     line = f_data.read()
#
# line_new=[]
# s1=''
# num=''
# for char in line:
#     if char.isalpha():
#
#         if s1!='' and int(num)>0:
#             line_new.append(s1 * int(num))
#         s1=char
#
#         num=''
#
#     elif char.isdigit():
#         num=num+char
# if s1!='' and int(num)>0:
#     line_new.append(s1 * int(num))
#
#
# with open('otvet.txt','w') as f_data:
#     f_data.write(''.join(line_new))
# ******************************************************************888
# вывести список чисел, входящих в строку
# l='c16F6Z19W5h4T17j7f2i16b15Z5V14r19w8k3L13A8R3H6t19k5e13f15S19s17Z16l'
# l_new=[]
# num=''
# for char in l:
#     if char.isalpha():
#         if num!='' and int(num)>0:
#             l_new.append(num)
#         num=''
#     else:
#         num=num+char
# print(l_new)
# *****************************************************************
# with open('dataset_1.txt') as f_data:
#     line=[]
#     line_str=''
#     for l in f_data.readlines():
#         line=l.lower().split()+line
#         # line.append(line_str)
#
#     print(line)
# line_new=[]
# dict_word={}
# for word in line:
#     word_count=line.count(word)
#     dict_word[word]=word_count
# with open('otvet1.txt','w') as f_data:
#     for key,value in dict_word.items():
#         print(key,value)
#         f_data.write(key+'\n')
#         f_data.write(str(value))

# with open('d1.txt') as f_data:
#     line=[]
#     line_str=''
#     rezult={}
#     for line in f_data:
#         words=line.strip().lower().split()
#         for w in words:
#             rezult[w]=rezult.get(w,0)+1
# with open('otvet1.txt','w') as f_data:
#     maxx=[]
#     for v in sorted(rezult.values()):
#         maxx.append(v)
#     print(max(maxx))
#     for k,v in rezult.items():
#         if max(maxx)==v:
#             # print(k)
#             f_data.write(k+'\t'+str(v)+'\n')
#             # f_data.write(str(v)+'\n')
# *******************************************************************
# with open('students.txt') as file:
#     # line_count = sum(1 for line in file)
#     # print(line_count)
#     student={}
#     itog=[]
#     m=0
#     c=0
#     p=0
#     r=0
#     for line in file:
#
#         words=line.strip().split(';')
#         fio=words[0]
#         matem=words[1]
#         phizik=words[2]
#         rus=words[3]
#
#         sr_ball=(int(matem)+int(phizik)+int(rus))/3
#         student[fio]=sr_ball
#
#         m=int(matem)+m
#         p=int(phizik)+p
#         r=int(rus)+r
#         c+=1
#     itog=str(m/c)+' '+str(p/c)+' '+str(r/c)
#     print(itog)
#
# with open('otvet3.txt','w') as f:
#     for v in student.values():
#         f.write(str(v)+' '+'\n')
#
#     f.write(itog+' \t')
# ********************************************************************************
# n=2
# lines = [
#     'helloworld.exe R X',
#     'pinglog W R',
#     'nya R',
#     'goodluck X W R',
# ]
# file_sys={}
# operations = {
#     'read': 'R',
#     'write': 'W',
#     'execute': 'X'
# }
# for j in range(0, len(lines) ):
#     s = lines[j].split()
#     oper = []
#     file_sys[s[0]] = 0
#     for i in range(1, len(s)):
#         oper.append(s[i])
#         file_sys[s[0]] = oper
#
#
# print(file_sys)
#
# def allow(operWide, fileName):
#     operShort = operations[operWide]
#     if operShort in file_sys[fileName]:
#         return 'OK'
#     else:
#         return 'Access denied'
# m=5
# for h in range(m):
#     l=input().split()
#     op=l[0]
#     fil=l[1]
#     print ( allow(op,fil))
# ********************************************************************
# # АНГЛО-ЛАТИНСКИЙ СЛОВАРЬ
# n=3
# a=[]
# b=[]
# # slovar={}
# # for word in range(n):
# #     l=input().split()
# #     a=[]
# #     for j in range(2,len(l)):
# #         a.append(l[j])
# #         b.append(l[j])
# #         key=l[0]
# #         if key not in slovar:
# #             slovar[key]=a
# slovar = {'apple': ['malum', 'pomum', 'popula'],
#         'fruit': ['baca', 'bacca', 'popum'],
#         'punishment': ['malum', 'multa']}
#
# b={'baca', 'bacca', 'malum', 'multa', 'pomum', 'popula', 'popum'}
# print(sorted(b))
# count=[]
# for elem in sorted(b):
#     count=[]
#     for key,value in slovar.items():
#
#         if elem in value:
#             count.append(key)
#             print(elem, *count, sep=', ')
# *******************************************************************************88
# # САМОЕ ЧАСТОЕ СЛОВО. НУЖНО ДОДЕЛАТЬ!
# n=int(input())
# d={}
# col=1
# for i in range(n):
#     l=input().split()
# for word in l:
#     if word not in d:
#         d[word]=col
#     else:
#         d[word]+=1
# b=[]
# for k,v in d.items():
#     b.append(v)
# m=max(b)
# itog=[]
# for k,v in d.items():
#     if m == v:
#         itog.append(k)
# print(itog)
# print(min(itog))
# *************************************************************
# ЧАСТОТНЫЙ АНАЛИЗ
# n=int(input())
# s=[]
# for i in range(n):
#     l=input().split()
#     s=s+l
# print(s)
# # s=['hi', 'hi', 'what', 'is', 'your', 'name', 'my', 'name', 'is', 'bond',
# #    'james', 'bond', 'my', 'name', 'is', 'damme', 'van', 'damme', 'claude',
# #    'van', 'damme', 'jean', 'claude', 'van', 'damme']
# s_set=set(s)
# # print(s_set)
# d={}
# for word in s:
#     word_count=s.count(word)
#     if word not in d:
#         d[word]=word_count
#     else:
#         d[word]+=1
# # print(d)
# spis=[]
# a1 = tuple()
# for key,value in d.items():
#     a1=(-value,key)
#     spis.append(a1)
# # print(spis)
# a2=tuple(sorted(spis,reverse=True))
#
# # a2=((7, 'damme'), (5, 'van'), (5, 'name'), (5, 'is'), (3, 'my'), (3, 'hi'),
# #     (3, 'claude'), (3, 'bond'), (1, 'your'), (1, 'what'), (1, 'jean'), (1, 'james'))
# print(a2)
# # print(a2[0][1])
# dd=[]
# for i in (range(len(a2))):
#     for j in range(1,len(a2[i])):
#
#         print(a2[i][j])
# print(dd)
# *****************************************************************88
# ЧАСЫ -1
# ch1=6
# m1=54
# s1=4
#
# ch2=14
# m2=18
# s2=42
# ch1,m1,s1,ch2,m2,s2=int(input())
# r1=ch2-ch1
# r2=m2-m1
# r3=s2-s1
#
# print('часы=',r1,'минуты= ',r2,'секунды= ',r3)
# print(r3+r2*60+r1*60*60)
# ************************************************************
# МАКСИМАЛЬНОЕ ЧИСЛО ИДУЩИХ ПОДРЯД РАВНЫХ ЭЛЕМЕНТОВ
# n = int(input())
# new_n = 0
# count = 1
# a=[1]
# while n != 0:
#     if new_n != n:
#         new_n = n
#         count=1
#     else:
#         count += 1
#         a.append(count)
#     n = int(input())
# print(max(a))
#
# n = int(input())
# new_n = 0
# count = 1
# maxx=1
# while n != 0:
#     if new_n != n:
#         new_n = n
#         count=1
#
#     else:
#         count += 1
#         if count>maxx:
#             maxx=count
#     n = int(input())
# print(maxx)
# ************************************************************8
# СТАНДАРТНОЕ ОТКЛОНЕНИЕ
# import math
# a=0
# s = 0
# count = 0
# while True:
#     n = int(input())
#     count += 1
#     s = (s + n)/count
#     if n == 0:
#
#         a = math.sqrt(((n-s)**2)/(count-1))+a
#         print(a)
#         break
# ****************************************************************
# КАКИМ ПО СЧЕТУ ЧИСЛОМ ЯВЛЯЕТСЯ ЧИСЛО ФИБАНАЧЧИ
# n=int(input())
# f1=f2=1
# count=2
# if n == 0:
#     print(0)
# else:
#     for i in range(2,n):
#         if f2==n:
#             print(count)
#             break
#         f1,f2=f2,f1+f2
#         count+=1
#     else:
#         print(-1)
# ********************************************************************
# ВЫВЕСТИ СРЕДНИЙ РОСТ ПО КЛАССАМ
# with open('rost1.txt') as file:
#     students={}
#     count=0
#     r=[]
#     for line in file:
#         count+=1
#         word=line.split()
#         klas=int(word[0])
#         fio=word[1]
#         rost=int(word[2])
#
#         if klas not in students:
#             students[klas]=[rost]
#         else:
#             students[klas].append(rost)
# c=0
# sred=0
# new_stud={}
# for k,v in students.items():
#     sred=0
#
#     for j in v:
#         c=len(v)
#         sred=sred+j
#         new_stud[k]=sred/c
# with open('otvet_rost.txt','w') as f:
#     for k,v in sorted(new_stud.items()):
#         f.write(str(k)+' '+str(v)+'\n')
# **********************************************************
# ПРОВЕРКА ОРФОГРАФИИ
# n=4
# # word=set()
# # for i in range(4):
# #     l=input().lower()
# #     word.add(l)
# word={'champions','we','are','stepik'}
# print(word)
# # m=3
# # prov_slov=[]
# # for j in range(m):
# #     l1=input().lower().split()
# #     prov_slov=prov_slov+l1
#
# prov_slov=['we', 'are', 'the', 'champignons',
#            'we', 'are', 'the', 'champions', 'stepic']
# prov_set=set(prov_slov)
# print(prov_set)
# for elem in prov_set:
#     if elem not in word:
#         print(elem)
# ***************************************************
# ШИФРОВКА И ДЕШИФРОВКА
# l1=input()
# l2=input()
# l3=input()
# l4=input()
# d={}
# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
# d2={}
# for i in range(len(l1)):
#     d2[l2[i]]=l1[i]
# r2=[]
# for char in l3:
#     if char in d.keys():
#         r2.append(d[char])
# s2=[]
# print(''.join(r2))
# for char in l4:
#     if char in d2.keys():
#         s2.append(d2[char])
# print(''.join(s2))
# **********************************************88
# n=4
# d={}
# for i in range(n):
#     l=input().split()
#     key=l[0]
#     if key not in d:
#         d[key]=int(l[1])
#     else:
#         d[key]=d[key]+int(l[1])
# print(d)
# x=0
# y=0
# for k,v in d.items():
#     if k=='север':
#         y=y-v
#
#     elif k=='запад':
#         x=v-x
#
#     elif k=='юг':
#         y=v+y
#
#     elif k=='восток':
#         x=v-x
# print(x,y,end=' ')
# *******************************88
# черепаха
# def pprint(*smth):
#     from sys import stderr
#     print(smth, file=stderr)
#
# n=int(input())
#
# x=0
# y=0
# for i in range(0, n):
#     l=input().split()
#     k=l[0]
#     v=int(l[1])
#     #pprint(k, v)
#     if k=='север':
#         y=y-v
#
#     elif k=='запад':
#         x=x+v
#
#     elif k=='юг':
#         y=y+v
#
#     elif k=='восток':
#         x=x-v
#
# print(y, x)
# ******************************************************************
# РОДОСЛОВНАЯ
# n=int(input())
# d={}
# potom=[]
# for i in range(n-1):
#     l=input().split()
#     potom=potom+l
#     potomok=l[0]
#     roditel=l[1]
#     if potomok not in d:
#         d[potomok]=roditel
# print(d)
# p=set(potom)
# print(potom)
# print(p)
# def getPredokCount(name):
#     ret = 0
#     while name in d:
#         ret += 1
#         name = d[name]
#     return ret
# for name in sorted(p):
#     print(name,getPredokCount(name))

# *************************************************
# students = ['Вася', 'Маша', 'Петя', 'Дима',
#             'Марина', 'Люба', 'Коля', 'Ваня']
#
# grades = {'Вася': 4, 'Петя': 9, 'Люба': 4,
#           'Марина': 7, 'Коля': 5,'Ваня': 10}
# categories = {'отлично' : [8, 9, 10], 'хорошо' : [6, 7],
#               'удовлетворительно' : [4, 5],
#               'неуд' : [0, 1, 2, 3]}

# print('Список студентов,которые не писали контрольную работу:')
# l=list(grades)
# print(l)
# stud=[name for name in students if name not in l ]
# print(stud)
# print('Баллы ниже 8:')
# new_st=dict([(key,value) for key,value in grades.items() if value <8])
# print(new_st)

# dd={'good':[name for name,value in grades.items() if value>8],
#     'bad':[name for name,value in grades.items() if value<8]}
# # for k,v in dd.items():
#     print(k,':',*v, sep=', ')
# ********************************************************
# import random
# n=10
# sl=[random.randint(0,9) for i in range(n)]
# print(sl)
# sl_s=set(sl)
# print(sl_s)
#
# d={i:sl.count(i) for i in sl_s}
# print(d)
# ********************************************************
n = 1
# s=[]
# for i in range(n):
#     l=input().split()
#     s=s+l
# s='apple orange banana banana orange'.split()
# print(s)
# d={}
# for word in s:
#     if word not in d:
#         d[word]=s.count(word)
#     else:
#         d[word]=d[word]+s.count(word)
# print(d)
# slova=tuple((-v,k) for k,v in d.items())
# a=sorted(slova)
# print(a[0][1])
# ********************************************************************

# s='aaaabbcaa'
# col=1
# s2=''
# for i in range(len(s)):
#
#     if i > 0:
#         if s[i]==s[i-1]:
#             col+=1
#         else:
#             if i>0:
#                 s2=s2+s[i-1] + str(col)
#         col=1
# s2=s2+s[-1] + str(col)
# print(s2)
# ******************************************************
# l='The cat sat on the mat'.lower().split()
#
# d={}
# for word in l:
#     z=l.count(word)
#     if word not  in d:
#         d[word]=z
# slova=tuple((-v,k) for k,v in d.items())
# a=sorted(slova)
# print(a[0][1])
# **************************************************************8
# n=2
# d1={}
# for i in range(n):
#     country,*city=input().split()
#     for j in city:
#         d1[j]=country
# c=input()
# print(d1.get(c))
# ***********************************************************
# tovari={}
#
# l=input().split()
# # tovari[l[0]]=[int(l[1]),int(l[2])]
# d=dict([(l[0],[int(l[1]),int(l[2])])  for i in range(int(input())) ])
# print(d)
#
# tovari={}
# for i in range(int(input())):
#     l=input().split()
#     tovari[l[0]]=[int(l[1]),int(l[2])]
# info=tovari.get(input())
# print(info[0]*info[1])
# ****************************************
# ФУТБОЛЬНАЯ КОМАНДА
# n=3
# commands={}
# igri=[]
# for i in range(n):
#     l=input().split()
#     komanda1=l[0]
#     komanda1_ball=l[1]
#     komanda2=l[2]
#     komanda2_ball = l[3]
#     if komanda1 not in commands:
#         commands[komanda1]={
#             'count_of_games':0,
#             'pobeda':0,
#             'tie':0,
#             'loose':0,
#             'points':0
#         }
#     if komanda2 not in commands:
#         commands[komanda2] = {
#             'count_of_games': 0,
#             'pobeda': 0,
#             'tie': 0,
#             'loose': 0,
#             'points': 0
#         }
#     if komanda1_ball>komanda2_ball:
#         commands[komanda1]['pobeda']+=1
#         commands[komanda1]['points']+=3
#         commands[komanda2]['loose'] += 1
#         commands[komanda2]['count_of_games'] += 1
#         commands[komanda1]['count_of_games'] += 1
#     elif komanda1_ball<komanda2_ball:
#         commands[komanda2]['pobeda'] += 1
#         commands[komanda2]['points'] += 3
#         commands[komanda1]['loose'] += 1
#         commands[komanda1]['count_of_games'] += 1
#         commands[komanda2]['count_of_games'] += 1
#     else:
#         commands[komanda2]['count_of_games']+=1
#         commands[komanda1]['count_of_games'] += 1
#         commands[komanda2]['points'] += 1
#         commands[komanda1]['points'] += 1
#         commands[komanda2]['tie'] += 1
#         commands[komanda1]['tie'] += 1
# for k,v in commands.items():
#     print(k,':',v['count_of_games'],v['pobeda'],v['tie'],v['loose'],v['points'])
# **************************************************************************

# import requests
# url='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
# s=requests.get(url)
# print(s.text)
# # col=0
# # for i in range(len(r.text)):
# #     col=r.text.count('\n')
# # print(col)
# while True:
#     if not s.text.startswith('We'):
#         s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s.text)
#         continue
#     else:
#         print(s.text)
#         break
# *******************************************************************************8

# def print_number():
#     is_found = False
#     number = 1
#     while True:
#         for i in range(1, 15):
#             if number % i != 0:
#                 break
#             else:
#                 # is_found = True
#                 if is_found == True:
#                     print(number)
#                     break
#         number += 1
# print_number()
# ****************************************************************
# ужножение двух списков
# first = list(map(int, input().split()))
# second = list(map(int, input().split()))
#
# def mult_list(first,second):
#     a=[]
#     for i in range(len(first)):
#         a.append(int(first[i])*int(second[i]))
#     return a
# result = mult_list(first, second)
# print(result)

# f=[1,2,3]
# s=[2,4,5]
# a=[i*y for i,y in zip(f,s)]
# print(a)
# *****************************************************************
# анаграмма
# first_word, second_word=input().split()
# def is_anagram(a,b):
#     return sorted(a)==sorted(b)
#
# result = is_anagram(first_word, second_word)
# print(result)
# **************************************************************
# a, b, c = map(int, input().split())
# def in_interval(a,b,c):
#     return a<=c<=b
# print(in_interval(a, b, c))

# print((lambda a,b,c:a<=c<=b)(*map(int, input().split())))
# *************************************************************
# n=4
# a=[]
# names=tuple(input().split() for _ in range(n))
# print(names)
#
# def get_youngest(names):
#     return sorted(names,key=lambda x:int(x[1]))[0]
# print(*get_youngest(names))
# *************************
# values = tuple(map(int, input().split()))
#
# def mean(a):
#     summ=0
#     for i in a:
#         summ=summ+i
#     return *a,summ/len(a)
# rez=mean(values)
# print(*rez)
# # *********************************************
# hero_pop = ('Жил-был поп,' +
#             'Толоконный лоб.'+
#             'Пошел поп по базару' +
#             'Посмотреть кой-какого товару.')
# hero_balda = ('Навстречу ему Балда'+
#               'Идет, сам не зная куда.')
#
# def counts(s):
#     s=s.lower()
#     for p in s:
#         if p in '-.,""':
#             s=s.replace(p,'')
#     chars={}
#     for char in s:
#         chars[char]=s.count(char)
#     return chars
# count_pop = counts((hero_pop))
# print(count_pop)
# count_balda=counts((hero_balda))
# print(count_balda)
# print(sorted(count_pop.items(),key=lambda item:item[1],reverse=True)[:3])
# ***********************************************
# a=[]
# with open('d11.txt',encoding='utf-8') as f:
#      line=f.read()
#      sp_line=line.split()
#      print(sp_line)
#      print('Количество слов: ',len(sp_line))
#      print(line)
#      print('Количество строк в файле: ',len(line),line.count('\n'))

# for name in line:
#     lst=name.strip('\n')
#     a=len(lst)
#     print(a)

# for name in reversed(line):
#     a.append(name.strip())
# print(a)0
# ***********************************
# line = {}
# res = {}
# qwe=[]
# with open("d11.txt") as f:
#     for i in range(10):
#         line[i] = f.readline().strip('\n')
#         stroka = list(map(int,line[i].split()))

# print(stroka)
# res[i] = (stroka[0] + stroka[1]) / 2


# with open("result.txt", "a") as result:
#     for i in range(10):
#         res[i] = str(res[i])
#         result.write(res[i] + "\n")


# ****************************************************
# ЗАБАСТОВКИ
# # n,k=list(map(int,input().split()))
# # print(n,k)
# # dni=[]
# # for i in range(k):
# #     x,y = list(map(int,input().split()))
# #     dni.append((x,y))
# # print(dni)
# parties=[(2,3),(3,5),(9,8)]
# n=19
# k=3
# itog=0
# d_of_week=1
# for current_day in range(1,n+1):
#
#     if d_of_week>5:
#         if d_of_week==7:
#             d_of_week=1
#         else:
#             d_of_week+=1
#     else:
#         d_of_week += 1
#         koef_basta=0
#         for parti in parties:
#             d_of_start,d_step=parti
#             if current_day==d_of_start:
#                 koef_basta=1
#                 # print(current_day, parti)
#                 break
#             elif current_day > d_of_start:
#                 if (current_day-d_of_start)%d_step==0:
#                     koef_basta=1
#                     # print(current_day, parti)
#                     break
#
#
#         itog += koef_basta
# print(itog)

# **************************************************88
# with open('cats.txt') as file:
#     text=file.read()
#     words=text.split()
#     print(words)
#     count={}
#     for word in words:
#         count[word]=count.get(word,0)+1
# count_sort=sorted(count.items(),key=lambda item:item[1],reverse=True)
# for key,value in count_sort:
#     print(key,value)
# ************************************
# fhand=open('cats.txt')
# for line in fhand:
#     line=line.rstrip()
#     if line.find('the')==-1:
#         continue
#     words=line.split()
#     print(words)
# ************************************************8
# def histogram(s):
#     d={}
#     for char in s:
#         if char not in d:
#             d[char]=1
#         else:
#             d[char]+=1
#     return d
# rez=histogram('brontosaurus')
# print(rez)
# *****************************************
# fname=open('cats.txt')
# counts={}
# for line in fname:
#     words=line.split()
#     for word in words:
#         if word not  in counts:
#             counts[word]=1
#         else:
#             counts[word]+=1
# lst=list()
# sorted(lst)
# for k,v in counts.items():
#     lst.append((v,k))
# # print(sorted(lst,reverse=True))
# for k,v in sorted(lst,reverse=True):
#     print(k,v)

# ****************************************************888888888
# d = {'r':10, 'b':1, 'c':22}
# t=list()
# for k,v in d.items():
#     t.append((v,k))
# print(sorted(t,reverse=True))
# *****************************************8888
# last=['Ivanov','Petrov','Soloviev']
# first=['Ivan','Petr','Dmitry']
# tel='+79172663574'
# d=dict([((last[i],first[i]),tel) for i in range(3)])
# print(d)
# ************************************************8
import re
# hand=open('cats.txt')
# for line in hand:
#     line=line.rstrip()
#     x= re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
#     if len(x)>0:
#         print(x)

# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# lst=re.findall('\S+@\S+',s)
# print(lst)
# ********************
from itertools import count
# l1 = [1, 5, 3]
# l2 = [0, -1, 4, 2, 3 ]
# print(list(itertools.zip_longest(l1, l2,fillvalue='0')))

# colors = ['белый', 'желтый', 'розовый', 'красный']
# buket = []
# for item in itertools.combinations(colors,3):
#     buket.append(item)
# print(buket)
# a='abcd'
# nabor=[]
# for item in itertools.combinations_with_replacement(a,3):
#     nabor.append(item)
# print(nabor)
# print(list(itertools.permutations('abc',3)))
# ООП
# class Dog():
#     def __init__(self,new_name='No name'):
#         self.name=new_name
#     def set_name(self,new_name):
#         self.name=new_name
#     def get_name(self):
#         return  self.name
#     def bark(self):
#         print(f'Меня зовут :{self.name}')
# my_dog=Dog('Тузик')
# print(my_dog.get_name())
# my_dog.set_name('Шарик')
# print(my_dog.get_name())

# class Cat():
#     def __init__(self):
#         self._name='Без имени'
#         self._count=0
#     def __str__(self):
#         return self._name
#     def get_count(self):
#         return self._count
#     def set_name(self,name):
#         self._name=name
#     def eating(self):
#         self._count+=1
#     def gaming(self):
#         if self._count>0:
#             self._count-=1
#         else:
#             raise Exception('нет сил играть')
#     def meow(self):
#         if self._count==0:
#             print('Хочу есть')
# my_cat=Cat()
# my_cat.set_name('Котик')
# print(my_cat._count)
# for item in range(4):
#     my_cat.eating()
# print(my_cat._count)
# for item in range(4):
#     my_cat.gaming()
# print(my_cat._count)
# print(my_cat)
# class Team():
#     def __init__(self,sport,players):
#         self.sport=sport
#         self.players=players
#
#     def __len__(self):
#         return len(self.players)
#     def __contains__(self, player):
#         return player in self.players
#     def __str__(self):
#         return f'{self.sport} team'
# team=Team('foonball',['play1','play2'])
# print(len(team))
# print('play'in team)
# print(team)
# *********************************************************
# n,k=list(map(int,input().split()))
# parties=[]
# for i in range(k):
#     x,y = list(map(int,input().split()))
#     parties.append((x,y))
# itog=0
# d_of_week=1
# for current_day in range(1,n+1):
#     if d_of_week>5:
#         if d_of_week==7:
#             d_of_week=1
#         else:
#             d_of_week+=1
#     else:
#         d_of_week += 1
#         koef_basta=0
#         for parti in parties:
#             d_of_start,d_step=parti
#             if current_day==d_of_start:
#                 koef_basta=1
#                 break
#             elif current_day > d_of_start:
#                 if (current_day-d_of_start)%d_step==0:
#                     koef_basta=1
#                     break
#         itog += koef_basta
# print(itog)

# a=[x*2 if x%2==0 else x+1 for x in range(5,10)]
# print(a)
#
# f=lambda x,y:x**2+y**2
# print(f(3,4))
# a=[1,4,3]
# b=[2,8,9]
# c=[(a[i]*b[i]) for i in range(3)]
# print(c)
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity=capacity
#         self.v=0
#
#     def can_add(self, v):
#         if self.capacity<=self.v:
#             return True
#         else:
#             return False
#     def add(self, v):
#         self.capacity-=self.v
#         # положить v монет в копилку
# x=MoneyBox(100)
# x.add(300)

# a=[18, 17, 20, 16, 26, 8, 30, 2, 3, 13]
# minn=a[0]
# b=[]
# while len(a)!=0:
#     for elem in a:
#         if elem<minn:
#             minn=elem
#
#     a.remove(minn)
#     b.append(minn)
#     minn = a[0]
#     if len(a)==1:
#         b.append(a[0])
#     #     break
# print(*b)
# ***************************************
# a = [1, 7, 3, 3, 1, 1, 7, 4, 7, 3]
# p=[]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             if a[i] not in p:
#                 p.append(a[i])
# p.sort()
# print(*p)
# print(*sorted(set([m for m in a if a.count(m)>1])))
# ********************************************8888
# n=3
# d={}
# count=1
# for i in range(n):
#     name,ball=input().split()
#     if name not in d:
#         count=1
#         d[name]=[int(ball),count]
#     else:
#         count+=1
#         # d[name]=(d[name]+int(ball)
#         d[name]=d[name]+count
# print(d)
# d={'Демин': 6, 'Сергеев': 4, 'Золотов': 7, 'Иванов': 3, 'Петров': 2, 'Сидоров': 3}
# print(d)
# for k,v in d.items():
#     d[k]=v/count
#     print(k,v)
# *************************************************
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# a=int(input())
# for i in range(len(months)):
#     if (a-1)==i:
#         print(months[i])

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# index=[-1,0,12,7]
# a=[numbers.pop(i) for i in index]
# print(numbers)
# print(sum(a))

# numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# copy_numbers=numbers.copy()
# print(copy_numbers)
# l=input().split()
# print('\n'.join(input().split()))

# l=input()
# print('ДА' if l=='Python' else 'НЕТ')
# l,b =map(int,input().split())
# god=0
# while l<=b:
#     l,b,god = l*3,b*2,god+1
# print(god)

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6,
#            9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1,
#            5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9,
#            8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6,
#            6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9,
#            4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0,
#            2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9,
#            8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2,
#            1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1,
#            2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9,
#            2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# # numbers.remove(4)
# [numbers.remove(4) while 4 in numbers]
# print(*numbers)
# ****************************************************
# l='Правильность'
# while len(l)>=1:
#     print(l)
#     l=l[1:-1]
# ***********************************************
# total=0
# while True:
#     n=int(input())
#     if n==0:
#         break
#     total += n
# print(total)256445d
#
# n=123
# a=[]
# while n>0:
#     print(n%10)
#     a.append(n % 10)
#     n=n//10
# print(f'{min(a)}\n{max(a)}')

# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)
# n=777
# a=[]
# count=0
# while n>0:
#
#     a.append(n % 10)
#     n=n//10
# count=a.count(7)
# print(count)
# n=4
# l=[]
# for i in range(n):
#     l.append(input())
# print(l)
# a=[input() for _ in range(n)]
# print(a)

# a='s'
# l='Diane visited her friends who live in San Francisco'.split()
# print(l)
# for i in l:
#     if a in i.lower():
#         print(i)
# a=[elem for elem in l if a in elem.lower()]
# print(*[elem for elem in l if a in elem.lower()],sep='\n')

# a=list(map(int,input().split()))
# r=int(input())
# for i in range(len(a)):
#     if r==a[i]:
#         print(i+1)
#         break
# else:
#     print('ErrorValue')

# a=list(map(int,input().split()))

# a=[8,11,-9,0,5,-20]
# b=[elem for elem in a if elem>0]
# if len(b)>0:
#     print(min(b))
# else:
#     print('Empty')
# l='Тот'.lower()
# d={}
# for elem in l:
#     if elem not in d:
#         d[elem]=1
#     else:
#         d[elem]+=1
# d_sort = sorted(d.items(), key=lambda item: item[1], reverse=True)
# print(d_sort)
# print(d_sort[0][1])

# m=1
# d={elem:(m if elem not in d else m+1 ) for elem in l}
# print(d)

# l='Тот'.lower()
# print(max(list(l.count(char) for char in l)))

# n=1211
# l=str(n)
# chet=0
# nechet=0
# for i in range(len(l)):
#     if i%2==0:
#         chet+=int(l[i])
#     else:
#         nechet+=int(l[i])
# if abs(chet-nechet)%11==0:
#     print('YES')
# else:
#     print('NO')

# n='2418'
# a=[int(i) for i in n]
# b=sum(a[1::2])
# c=sum(a[::2])
# print('YES' if abs(b-c)%11==0 else 'NO')

# l='Europe cup 2021'
# total=0
# c=0
# for char in l:
#     if char.isdigit():
#         c+=1
#         total+=int(char)
# print(c, total)

# z=[int(char) for char in l if char.isdigit()]
# print(sum(z))
# x=[c+1 for char in l if char.isdigit()]
# print(len(x))

# l='Python is best I love python'.split()
# d=[]
# c=[]
# for elem in l:
#
#     if elem.lower() not in d:
#         d.append(elem.lower())
#         c.append(elem)
# print(*c)

# n='0235346546ty'
# d={}
# for elem in n:
#     if elem.isdigit():
#         if elem not in d:
#             d[elem]=1
#         else:
#             d[elem]+=1
# for k,v in sorted(d.items(),key=lambda item:item[1],reverse=True):
#     print(k,v,sep=' ',end='\n')

# n=5
# l=[-8, 5, -7, 4, -8, 0, 4]
# b=[]
# while len(l)>0:
#     b.append(min(l))
#     l.remove(min(l))
# print(b)

# n=3
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# a=[3,7,1,10,8]
# for i in a:
#     print('*'*i)

# ПОСТУЛАТ БЕРТРАНА
# n=239
# c=0
# for i in range(n+1,2*n+1):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         c+=1
# print(c)

# ПУЗЫРЬКОВАЯ СОРТИРОВКА
# n=7
# a=[8 ,5, 3, 1, 4, 7, 9]
# c=0
# for j in range(n):
#     for i in range(0,len(a)-1):
#         if a[i]>a[i+1]:
#              c+=1
#              b=a[i]
#              a[i]=a[i+1]
#              a[i+1]=b
## print(a)
# print(c)

# n,m=map(int,input().split())
# c=0
# for i in range(n):
#     for j in range(m):
#         if i**2+j==n and i+j**2==m:
#             c+=1
# print(c)

# n=2
# a=[[1,2],
#    [3,4]]
# total=0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i==j:
#             total+=a[j][j]
# print(total)

# n=5
# a = [[3, 4, 9, 1, 2],
#   [8, 2, 0, 5, 1],
#   [4, 7, 4, 8, 7],
#   [7, 1, 3, 3, 8],
#   [5, 6, 3, 7, 0]
# ]
# a=[[int(i) for i in input().split()] for _ in range(n)]
#
# n=int(input())
# for i in range(n):
#     row = list(map(int, input().split()))
#     a.append(row)
# for j in range(n):
#     for i in range(n):
#         print(a[i][j], end=" ")
#     print()

# n=5
# # a=[[int(i) for i in input().split()] for _ in range(n)]
# a=[[3, 4, 9, 6, 2],
#    [8, 2, 0, 5, 1],
#    [4, 7, 4, 8, 7],
#    [7, 1, 3, 3, 8],
#    [5, 6, 3, 7, 0]]
# for i in range(n-1,-1,-1):
#     for j in range(n-1,-1,-1):
#         print(a[j][i],end=' ')
#     print()

# n,m=map(int,input().split())
# a=[[i for i in input().split()] for _ in range(n)]
# for i in sorted(range(len(a)),reverse=True):
#     for j in range(len(a)):
#         print(a[i][j],end=' ')
#     print()

# a=[[0,0,0,0,0],
#    [0,0,0,0,0],
#    [0,0,0,0,0],
#    [0,0,0,1,0],
#    [0,0,0,0,0]]
# b=[]
# sentr=[2,2]
# for i in range(5):
#     for j in range(5):
#         if a[i][j]!=0:
#             b.append([i,j])
# # вот этот вариант надо доделать
# b1=list([(i,j) for i in range(len(a)) if a[i][j]==1] for j in range(len(a)))
# print(b1)
# print(b)
# print(sum((abs(sentr[0]-b1[0][0][0]),abs(sentr[1]-b1[0][0][1]))))

# рабочая программа
# a=[[int(i) for i in input().split()] for _ in range(5)]
# b=[]
# sentr=[2,2]
# for i in range(5):
#     for j in range(5):
#         if a[i][j]!=0:
#             b.append([i,j])
# print(sum((abs(sentr[0]-b[0][0]),abs(sentr[1]-b[0][1]))))

# сумма строк и сумма столбцов
# n,m=map(int,input().split())
# a=[[int(i) for i in input().split()] for _ in range(n)]
# sum_row=[]
# sum_column=[]
# b1=list(zip(*a))
# for i in range(n):
#     for j in range(m):
#         if sum(a[i]) not in sum_row:
#             sum_row.append(sum(a[i]))
# for i in range(m):
#     for j in range(n):
#         if sum(b1[i]) not in sum_column:
#             sum_column.append(sum(b1[i]))
# print(*sum_row)
# print(*sum_column)

# сумма строк и сумма столбцов
# n,m=map(int,input().split())
# a=[[int(i) for i in input().split()] for _ in range(n)]
# sum_row=[0 for _ in range(0, n)]
# sum_column=[0 for _ in range(0, m)]
# for i in range(n):
#     for j in range(m):
#        sum_row[i] += a[i][j]
#        sum_column[j] += a[i][j]
# print(*sum_row)
# print(*sum_column)

# n=3
# a= [[0,1,2],
#     [1,5,3],
#     [8,3,4] ]
# up_d=[]
# down_d=[]
# for i in range(n):
#     for j in range(n):
#         if i<j:
#             up_d.append(a[i][j])
#         elif i>j:
#             down_d.append(a[i][j])
# print('Yes' if sum(up_d)==sum(down_d) else 'No')

# n=3
# m=4
# a=[[1,2,3,4],
#    [9,10,11,12],
#    [5,6,7,8]]
# b=[0 for _ in range(n)]
# total=0
# for i in range(n):
#     for j in range(m):
#        b[i]+=a[i][j]
#
# print(max(b))
# print(b.index(max(b)))
# n=3
# m=4
# a=[ [7,7,7,7],
#     [7,7,7,7],
#     [7,7,7,7]]
# maxx=a[0][0]
# index=[0 for _ in range(2)]
# for i in range(n):
#     for j in range(m):
#         if a[i][j]>maxx:
#             maxx=a[i][j]
#             index.clear()
#             index.extend((i,j))
#
# print(maxx)
# print(*index)

# n=3
# m=3
# a=[ [3,1,2],
#     [1,3,4],
#     [3,3,3]]
# b=[]
# for i in range(n):
#     b.append(max(a[i]))
# print(max(b))
# print(b.index(max(b)),a[b.index(max(b))].index(max(b)))

# НУЖНО ДОДЕЛАТЬ!
# n=3
# m=3
# a=[[1,1,3],
#    [1,1,3],
#    [2,2,2]]
# b_max=[]
# c_sum=[0 for _ in range(n)]
# for i in range(n):
#     b_max.append(max(a[i]))
#     for j in range(m):
#         c_sum[i]+=a[i][j]
# print(b_max)
# print(c_sum)
#
# if b_max.count(max(b_max))==1:
#     print(b_max.index(max(b_max)))
# else:
#     if c_sum.count(max(c_sum))==1:
#         print(c_sum.index(max(c_sum)))
#     else:
#         print(c_sum.index(max(c_sum)))
# ***************************************************
# n=5
# m=3
# a=[[4,9,7],
#    [5,8,9],
#    [1,0,6],
#    [10,4,40],
#    [3,3,3]]
# b1=[max(a[i]) for i in range(n)]
# print(b1.count(max(b1)))
#
# n,m=map(int,input().split())
# a=[[int(i) for i in input().split()] for _ in range(n)]
# b=[]
# for i in range(n):
#     b.append(max(a[i]))
# print(b.count(max(b)))
# ************************************************************
# a=[[i for i in input().split()] for _ in range(4)]
# print(a)
# c=0
# for i in range(3):
#     for j in range(3):
#         if a[i][j]==a[i+1][j]==a[i][j+1]==a[i+1][j+1]:
#             c+=1
# if c==0:
#     print('Yes')
# else:
#     print('No')
#
# n=10
# x=5
# ab=[[i*j for j in range(1,n+1) ].count(x) for i in range(1,n+1)]
# print(sum(ab))

# n,x=map(int,input().split())
# a=[]
# ab=[[i*j for j in range(1,n+1)] for i in range(1,n+1)]
# c=0
# for i in range(len(ab)):
#     for j in range(len(ab)):
#         if x==ab[i][j]:
#             c+=1
# print(c)

# побочная диагональ
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# n=3
#
# print(*max([[a[i][j] for j in range(len(a)) if i+j==n-1]for i in range(len(a))]))
# # print(*max(ab))
# # короткий вариант
# n=int(input())
# a=[[int(i) for i in input().split()] for _ in range(n)]
# ab=[[a[i][j] for j in range(len(a)) if i+j==n-1]for i in range(len(a))]
# print(*max(ab))
# *******************************************************
# n=3
# ab=[]
# a=1
# b=0
# c=3
# for i in range(n):
#     bb=[]
#     for j in range(n):
#        if i==j:
#            bb.append(c)
#        elif i>j:
#            bb.append(b)
#        elif i<j:
#            bb.append(a)
#     ab.append(bb)
# for x in ab:
#     print(x)
# второй вариант
# n=int(input())
# ab=[]
# a,b,c=map(int,input().split())
# var2=[[c if i==j else a if i<j else b for j in range(n) ] for i in range(n)]
# [print(*i) for i in var2]
# **************************************************************
# n=4
# a=[[100,42],
#    [42,100],
#    [5,42],
#    [100,5]]
# c=0
# for i in range(n):
#     for j in range(n):
#         if a[i][0]==a[j][1]:
#             c+=1
# print(c)
# *******************************************************
# n=4
# m=4
# a=[['*','*','*','*'],
#    ['*','*','.','.'],
#    ['*','.','.','.'],
#    ['*','.','.','.']]
# count=0
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if (a[i+1][j]=='.') and (a[i][j+1]=='.') and (a[i-1][j]=='.') and (a[i][j-1]=='.'):
#             count+=1
# print(count)
# n,m = map(int, input().split())
# a=[]
# c=0
# a.append('.'*(m+2))
# for i in range(n):
#     row='.'+input()+'.'
#     a.append(row)
# a.append('.'*(m+2))
# for row in a:
#     print(row)
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if (a[i+1][j]=='.') and (a[i][j+1]=='.') \
#                 and (a[i-1][j]=='.') and (a[i][j-1]=='.') and a[i][j]=='.':
#             c+=1
# print(c)

# треугольник паскаля
# n=int(input())
# triangle=[]
#
# for i in range(n+1):
#     triangle.append([1]+[0]*n)
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(triangle[i][j],end=' ')
#     print()
# *************************************************
# n=4
# m=4
# # a=[[int(i) for i in input().split()] for _ in range(n)]
# a=[ [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [1, 1, 1, 1]]
# for i in range(n-2,-1,-1):
#     for j in range(m-2,-1,-1):
#         a[i][j]=a[i][j+1]+a[i+1][j]
# [print(*i) for i in a]
# ************************************************************************
# n=4
# m=10
# a=[]
# for i in range(n):
#     b=[]
#     if i%2==0:
#         for j in range(m*i,m*i+m):
#            b.append(j)
#     else:
#         for j in range(m*i+m-1,m*i-1,-1):
#            b.append(j)
#     a.append(b)
# [print(*i) for i in a]
# **************************************************************************88
# фотографии Брейнa
# n=2
# m=2
# a=[[i for i in input().split()] for _ in range(n)]
#
# Color=['C','M','Y']
# count='#Black&White'
# for i in range(n):
#     for j in range(m):
#         if a[i][j] in Color:
#            count='#Color'
# print(*[('#Color' for j in range(m) if a[i][j] in Color) for i in range(n)])
# print(count)
# **********************************************************
# ТОРТМИНАТОР
# n,m=map(int,input().split())
# a=[[i for i in input()] for _ in range(n)]
#
# a=[[0 if a[i][j]=='.' else 1 for j in range(m)] for i in range(n)]
# col_row=0
# col_column=0
# for i in range(n):
#    if sum(a[i])==0:
#       col_row+=1
# a1 = list(map(list, zip(*a[::-1])))
#
# for i in range(m):
#    if sum(a1[i])==0:
#          col_column+=1
# print(col_row * m + (col_column * n) -col_row*col_column)
# ***********************************************************
# st = 'Create a list of the first letters of every word in this string'.split()
# print(st)
# b=[char[0]*(char+1) for char in st]
# print(b)
from string import ascii_uppercase
# st='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n=3
# print([st[i]*(i+1) for i in range(len(st[:n]))])

# phrase = 'Take only the words that start with t in this sentence'.split()
# a=[elem for elem in phrase if elem[0]=='t' or elem[0]=='T']
# print(a)
#
# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# result=(a*3+b*5+c*8+d*5)
# print(result)

# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717)
# a=[elem for elem in my_tuple if elem%2!=0]
# print(sum([elem for elem in my_tuple if elem%2!=0])/len([elem for elem in my_tuple if elem%2!=0]))
# *************************************************
# n=31
# d1=dict((i,i*i) for i in range(1,n+1))
# print(d1)
# **********************************************************
# from string import ascii_lowercase
# print(ascii_lowercase)
# st='abcdefghijklmnopqrstuvwxyz'
# alphabet={}
# for i in range(len(st)):
#    alphabet[st[i]]=i+1
# print(alphabet)
#
# print(dict((st[i],i+1) for i in range(len(st))))
# address = {
#   "id": 7973,
#   "uid": "42f2ce1d-90ab-4345-9595-0d9f42e6c085",
#   "city": "East Monteland",
#   "street_name": "Gusikowski Land",
#   "street_address": "3230 Daugherty Centers",
#   "secondary_address": "Apt. 562",
#   "building_number": "58671",
#   "mail_box": "PO Box 5313",
#   "community": "Paradise Square",
#   "zip_code": "58611",
#   "zip": "01667",
#   "postcode": "00563",
#   "time_zone": "America/New_York",
#   "street_suffix": "Burg",
#   "city_suffix": "mouth",
#   "city_prefix": "West",
#   "state": "Wisconsin",
#   "state_abbr": "NY",
#   "country": "Mali",
#   "country_code": "MH",
#   "latitude": -56.97457993706476,
#   "longitude": -104.29509072140858,
#   "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715"
# }
# k=['zip_code','longitude','post_code','street_name','number_house']
# for i in k:
#    print(i in address)

# [print(i in address) for i in k]
# *************************************************************
# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# st='Argentine Peso'
# if st in currencies:
#    print(currencies[st])
# else:
#    print(f'Нет данных по {st}')
# print(currencies[st] if st in currencies else f'Нет данных по {st}' )
# *********************************************************************
# n=4
# st=['abc','abcd','abc','acab']
# d={}
# for key in st:
#    if key not in d:
#       d[key]='OK'
#    else:
#       d[key]=key+str(dict[key])
#
# for k,v in d.items():
#    print(k,v)
# ****************************************************
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
# for k,v in countries.items():
#    if city in v:
#       print(f'INFO: {city} is a city in {k}')
#       break
# else:
#    print(f'ERROR: Country for {city} not found')
# *********************************************************
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17"
# }
# user.setdefault('secret',user.pop('password'))
# user.setdefault('surname',user.pop('last_name'))
# for k in user.items():
#    print(k)
# ****************************************************

# a=list(map(int,input().split()))
# a=[1,2,3]
# # a.reverse()
# d={}
# for i in range(len(a)):
#    d={a[i]:d}
#
# print(d)
# рабочий вариант
# d=a[-1]
# for i in a[-2::-1]:
#    d={i:d}
# print(d)
# **********************************************
# a='ZZzzzZ34 WWw777'.lower()
# d={}
# for char in a:
#    if char.isalpha():
#       if char not in d:
#          d[char]=1
#       else:
#          d[char]+=1
# print(d)
# d1={}
# for i in a:
#    d1[i]=d1.get(i,0)+1
# print(d1)
# генератор словаря
# dd=dict((char,a.count(char)) for char in a if char.isalpha())
# print(dd)
# ******************************************************
# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
# total=0
# print(supermarket['milk']["quantity"])
# for k,v in supermarket.items():
#    total=supermarket[k]["quantity"]*supermarket[k]["price"]+total
# print(total)
# *******************************************************
# анаграмма
# s1='abracadabra'
# s2='cadabraabra'
# d_s1=dict((char,s1.count(char)) for char in s1)
# d_s2=dict((char,s2.count(char)) for char in s2)
# print('YES' if d_s1==d_s2 else 'NO')
# ************************************************************8
# азбука Морзе
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# st='Houston we have a problem'.lower()
# # print(st)
# # for i in st:
# #    for j in i:
# #       print(morze.get(j,0),end=' ')
# #    print()
#
# a=[]
# for char in st:
#    a.append(morze.get(char))
# print(*a,end='\n')
# *************************************************************
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
# s='subscription uid date_of_birth first_name'.split()
# print(s)
# # d={}
# # for key in s:
# #    d[key]=user.get(key,0)
# # print(d)
# print(dict((key,user.get(key,0)) for key in input().split()))
# ***************************************************************
# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
# phone_book={v:k for k,v in people}
# print(phone_book)
# *************************************************************
# a = [
#     ("Sidorov", 1995),
#     ("Lukov", 2002),
#     ("Petrov", 1991),
#     ("Gorbachev", 1984),
#     ("Kostin", 2000),
#     ("Isaev", 2005),
#     ("Eliseev", 1999),
#     ("Kozlov", 2004),
#     ("Bukov", 1995),
#     ("Gavrilov", 1980),
#     ("Efremov", 2006),
# ]
# d={key for key,val in a if val>2000}
# print(d)
# d1={key for key,val in a if key[0][0]=='E'}
# print(d1)
# d2={key[0] for key,val in a if val>2000}
# print(d2)
# **********************************************
# a = {
#     'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
#     'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
#     'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
#     'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
#     'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
#     'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
#     'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
#     'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
# }
# cars=[a[elem]['car'] for elem in a]
# print(cars)
# hobbi=[ a[elem]['hobby'] for elem in a]
# print(hobbi)
# cars_2000=[a[elem]['car'] for elem in a if a[elem]['age']<2000]
# print(cars_2000)
# vlad=[(elem,a[elem]['car']) for elem in a if a[elem]['age']<2000 ]
# print(vlad)
# vlad1=[(elem,a[elem]['car']) for elem in a if a[elem]['age']<2000 and a[elem]['hobby']=='soccer']
# print(vlad1)
# *******************************************************************
# s = 'gfdogjdf45i398gry74y543hgkgreiuYIUGd'
#
# isal=[char for char in s if char.isalpha()]
# print(isal)
# word=[char for char in s if char.isdigit()]
# print(word)
#
# d={char:s.count(char) for char in s if char.isalpha()}
# print(d)
# d1={char:s.count(char) for char in s if char.isdigit()}
# print(d1)
# ***********************************************
from random import randint
# a=[[random.randint(1,9) for j in range(5)] for i in range(5)]
# for i in a:
#     print(i)
# print('-'*10)
# b=[a[i][j] for i in range(5) for j in range(5) if i==j]
# print(b)
# print('-'*10)
# c=[a[i][j] for i in range(5) for j in range(5) if i==2]
# print(c)
# print('-'*10)
# d=[a[i][3] for i in range(5)]
# print(d)
# ****************************************************
# colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
# sizes = ['S', 'M', 'L', 'XL', 'XLL']
#
# a=[(c,s) for c in colors for s in sizes]
# print(a)
# ***********************************************************88
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
#
# a=[j for i in vector for j in i]
# print(a)
# # другой вариант
# # a=[]
# # for i in vector:
# #     for j in i:
# #         a.append(j)
# # print(a)
# *********************************************
# s='sevenkplus'
# print('CHAT WITH HER!' if len(set(s))%2==0 else  'IGNORE HIM!')
# ***************************************************
# a='TheQuickBrownFoxJumpsOverTheLazyDog'.lower()
# my_set=set(a)
# print(len(set(a)))
# print('YES' if len(set(a))>26 else 'NO')
# ***************************************
# красивый год
# a='2013'
# a=int(a)
# while len(set(str(a + 1)))!=4:
#     a=int(a)
#     a+=1
# print(a+1)
# ****************************************
# a='{a, b, c}'
# print(len(set([elem for elem in a if elem.isalpha()])))
# # print(len(b))
# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# print(len(set_a & set_b))
# ********************************************************
# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#         ]
# a=set(word for word in words if len(word)>6)
# print(len(a))
# ************************************************
# n=2
# a=[input().split() for i in range(n)]
# # for i in range(n):
# #     a.append(input().split())
# print(a)
# c=set()
# for elem in a:
#     c=set(elem)|c
# print(len(c))
# *************************************************************
# my_set = {'government', 'control', 'winter', 'few', 'generation',
#           'service', 'national', 'tradition', 'government'}
# a=['concert','brown','jacket','value']
# my_set.update(a)
# print(my_set)
# b=['government','national','tease']
# for elem in b:
#     my_set.discard(elem)
# print(my_set)
# ***********************************************************
# st='Hello world,hi dude,hello world,qwerty'.lower().split(',')
# print(st)
# my_set=set()
# for elem in st:
#     if elem not in my_set:
#         print('НЕТ')
#         my_set.add(elem)
#     else:
#         print('ДА')
# *************************************************
# a={1,3,2,5}
# b={4,3,2,6}
# print(*sorted(a - b))
# ***************************************
# st='qwerty123'
# a=set()
# for char in st:
#     if char.isdigit():
#        if st.count(char)>1:
#             a.add(char)
# print(*sorted(a) if a else ['NO'])
# *******************************************************
# удалить повторяющиеся символы
# st='hello_world!'
# s=set(st)
# print(s)
# for elem in st:
#     if elem in s:
#         print(elem, end='')
#         s.remove(elem)
# ******************************************************
# my_frozen=frozenset(int('7'*i) for i in range(1,78))
# print(my_frozen)
# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
#          'drop', 'produce', 'acquisition', 'cheap', 'strength',
#          'master', 'perception', 'noise', 'strange', 'am']
# words_with_position=[]
# for k,v in enumerate(words,1):
#     words_with_position.append((v,k))
# print(words_with_position)
# ***************************************************************
# english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
#                  'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
#                  'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
#                  'ask', 'go', 'suggest')
# for k,v in enumerate(english_words,1):
#     print(f'Word № {k} = {v}')
# ***********************************************************************
# n='3942682966937054'
# lst = list(map(int, input()))
# s = 0
# for index, value in enumerate(reversed(lst), start = 1):
#     if index %2 == 0:
#         if value * 2 > 9:
#             value = value * 2 - 9
#             s+=value
#         else:
#             value *=2
#             s+=value
#     else:
#         s += value
# if s % 10 == 0:
#     print('True')
# else:
#     print('False')
# ********************************************
# def summa(t):
#     s=sum(range(1,t+1))
#     print(s)
# summa(5)
# def sum_num(s):
#     total=0
#     for char in s:
#         if char.isdigit():
#             total=int(char)+total
#     print(total)
#
# s='123QwertY321'
# sum_num(s)
# ****************************************
# def check_passwor(s):
#     c=0
#     k=0
#     l=0
#     for char in s:
#         if char.isdigit():
#             c+=1
#         elif  char in '!@#$%*':
#             k+=1
#         elif char.isupper():
#             l+=1
#     print("Perfect password" if len(s)>=10 and c>=3 and k>=1 and l>=1 else 'Easy peasy' )
# s=input()
# check_passwor(s)
# ************************************888
# def count_letters(s):
#
#     zagl=[char for char in s if char.isupper()]
#     stroc=[char for char in s if char.isalpha() and not char.isupper()]
#     print(f'Количество заглавных символов: {len(zagl)}')
#     print(f'Количество строчных символов: {len(stroc)}')
# s='QWERTY'
# count_letters(s)
# *************************************************************8
# def repeat_please_n_times(n):
#     for i in range(n):
#         print('Just do it')
# repeat_please_n_times(4)
# ***********************************************************8
# def is_between(a,b,c):
#     print('True' if b<=a<=c and c<=a<=b else 'False')
# is_between(5,3,6)
# *****************************************************
# def count_letter(text, letter):
#     print(text.count(letter))
# text='did you pray desdemona'
# letter='D'
# count_letter(text,letter)
# *******************************************************
# def print_initials(name, surname, middlename):
#     print(f'{surname.title()} {name[0].title()}.{middlename[0].title()}.')
#
# name ='евгЕний'
# surname = 'петросян'
# middlename = 'ВаГАнович'
# print_initials(name, surname, middlename)
# **************************************
# def factorial(x):
#     pr=1
#     for i in range(2,x+1):
#         pr=pr*i
#     return pr
# for i in range(10):
#     print(i,factorial(i))
# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum([6, 3])
# assert max(3, -1, 9) != -1
# print('Проверки пройдены')
# ***********************************************
# def generate_fizz_buzz_list(n):
#     fb=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             fb.append('FizzBuzz')
#         elif i%3==0:
#             fb.append('Fizz')
#         elif i%5==0:
#             fb.append('Buzz')
#         elif not i%3==0 and not i%5==0:
#             fb.append(i)
#     return fb
# n=30
# primer=['FizzBuzz'if (i%3==0 and i%5==0) else 'Fizz' if i% 3==0 else 'Buzz' if i%5==0 else i for i in range(1,n+1)]
# print(primer)
# print(generate_fizz_buzz_list(4))
# ********************************************************************************
# from functools import reduce
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
# n=4
# a=[3,5,9,18]
# print(a)
# print(reduce(gcd,a))
# ************************************************************************
# def find_duplicate(lst):
#     y = []
#     for i in range(len(lst)):
#         if lst.count(lst[i]) >= 2 and y.count(lst[i]) < 1:
#             y.append(lst[i])
#     return y
# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print('Все успешно')
# # l=[1, 2, 3, 4]
# print(find_duplicate(l))
# **************************************************************
# def first_unique_char(s):
#     for i,elem in enumerate(s):
#         if s.count(elem)==1:
#             return i
#     return -1
#     # a=[s.count(elem) for elem in s]
#     # for index,val in enumerate(a):
#     #     if val==1:
#     #         return index
#     # return -1
# s='abracadabra'
# print(first_unique_char(s))
# **************************************************
#
# d=[{'name': 'Bart'}]
# a=[]
# for i,val in enumerate(d):
#     r=val.get('name')
#     a.append(r)
# print(a)
# l=len(a[-1])
# print(l)
# st=''
# for char in a:
#     st+=char+', '
# print(st)
# # s1=st[:-9]+' и '+st[-7(l+2):-2]
# s1=st[:-(l+4)]+' и '+st[-(l+2):-2]
# print(s1)
# if len(a)==1:
#     print(*a)

# s=len(a[-1])
# print(s)
# print(', '.join(a)[:-7]+' и '.join(a)[-7:])

# def format_name_list(names: list):
#     a = []
#     for i, val in enumerate(names):
#         r = val.get('name')
#         a.append(r)
#     if len(a) == 0:
#         return ''
#     l = len(a[-1])
#     if len(a) == 1:
#         return ' '.join(a)
#
#     st = ''
#     for char in a:
#         st += char + ', '
#     s1 = st[:-(l + 4)] + ' и ' + st[-(l + 2):-2]
#     return s1
#     if len(a) == 1:
#         return a
#
# # код ниже не стоит удалять, он нужен для проверки
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
# assert format_name_list([{'name': 'Bart'}]) == 'Bart'
# assert format_name_list([]) == ''
# assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
# assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
# assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
# print('Проверки пройдены')

# def format_name_list(names: list):
#     a = [val.get('name') for i, val in enumerate(names)]
#     if len(a)==1 or len(a)==0:
#         return ' '.join(a)
#     a.append(a.pop(-2)+' и '+ a.pop())
#     return ', '.join(a)
#
# # r=format_name_list([])
# # print(r)
# # код ниже не стоит удалять, он нужен для проверки
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
# assert format_name_list([{'name': 'Bart'}]) == 'Bart'
# assert format_name_list([]) == ''
# assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
# assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
# assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
# print('Проверки пройдены')

# url="www.xakep.ru"
#
# if url.startswith('https://www.'):
#     url=url.replace('https://www.','')
# if url.startswith('www.'):
#    url=url.replace('www','')
# url = url.replace('http://', '')
# url = url.replace('https://', '')
# # url = url.replace('/www.', '')
# # url = url.replace('www.', '')
# rez = url.split('.')
# print(rez)
# print(rez[0])
# ******************************************************
# def factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact
# def trailing_zeros(n):
#     rezult=str(factorial(n))[::-1]
#     print(rezult)
#     c=0
#     for index,elem in enumerate(rezult):
#         if elem=='0':
#             c+=1
#         else:
#             return c
# n=0
# print(trailing_zeros(n))
# # код ниже не стоит удалять, он нужен для проверки
# # # assert trailing_zeros(0) == 0
# # assert trailing_zeros(6) == 1
# # assert trailing_zeros(30) == 7
# # assert trailing_zeros(12) == 2
# # print('Проверки пройдены')
# *********************************************************
# def count_AGTC(dna):
#     return (dna.count('A'), dna.count('G'), dna.count("T"), dna.count("C"))
# # s='AAAATTT'
# # print(count_AGTC(s))
# # # код ниже не стоит удалять, он нужен для проверки
# assert count_AGTC('AGGTC') == (1, 2, 1, 1)
# assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
# assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
# assert count_AGTC('CCT') == (0, 0, 1, 2)
# print('Проверки пройдены')
# *********************************************************************8
from typing import List, Dict,Any,Union
# def first_repeated_word(s):
#     # s=s.split()
#     a=[]
#     for elem in s.split():
#         if elem not in a:
#             a.append(elem)
#         else:
#             return elem
# s='ab ca bc ca ab bc'
#
# print(first_repeated_word(s))
# ******************************************************
# # ШИФР ЦЕЗАРЯ
# def shift_letter(s:str,n:int):
#     rezult=(ord(s) - ord('a') + n) % 26
#     r=chr(rezult+97)
#     return r
# # print(shift_letter('d',-2))
#
# # ЗАШИФРОВАТЬ ФРАЗУ
# def caesar_cipher(s:str,n:int):
#     ''' Шифр цезаря'''
#     itog=' '
#     for elem in s:
#         if elem.isalpha():
#             sh=shift_letter(elem,n)
#             itog=itog+sh
#         elif elem==' ':
#             itog=itog+' '
#
#     return itog
#
# s='lost in the echo'
# n=27
# print(caesar_cipher(s,n))
# *******************************************************
# MIN_DRIVING_AGE = 18
# def allowed_driving(name: str, age: int) -> None:
#     if age<MIN_DRIVING_AGE:
#         return f'{name} еще рано садиться за руль'
#     elif age>=MIN_DRIVING_AGE:
#         return f'{name} может водить'
#
# print(allowed_driving('tim',18))
#
# def allowed_driving(name, age):
#     print(name,["еще рано садиться за руль", "может водить"][age>=MIN_DRIVING_AGE])
# ***********************************************************************888
# def get_word_indices(strings: list[str]) -> dict:
#     d={}
#     for i in range(len(strings)):
#         for j in strings[i].lower().split():
#             if j not in d:
#                 d[j] = [i]
#             else:
#                 d[j].append(i)
#     return d
# st=['This is a string','test String','test','string']
# print(get_word_indices(st))
# ********************************************************
# замена символав
# def replace(text:str,old:str,new:str =''):
#     text=text.split(old)
#     print(text)
#     return new.join(text)
# text='Bella Ciao'
# old='a'
# print(replace(text,old))
# ***********************************************
# def make_header(st:str,n:int=1):
#     return f'<h{n}>{st}</h{n}>'
#
# print(make_header('Bella Ciao'))
# ***********************************************
# def create_matrix(size:int=3,up_fill:int=0,down_fill:int=0):
#     a=[]
#     for i in range(1,size+1):
#         b=[]
#         for j in range(1,size+1):
#             b.append(j)
#             if i<j:
#                 b[j-1]=up_fill
#             elif i>j:
#                 b[j-1]=down_fill
#         a.append(b)
#     return a
#
# print(create_matrix())
# n=4
# aa= [[7 if i<j  else 9 if i>j  else j for j in range(1,n+1)] for i in range(1,n+1)]
# for i in aa:
#     print(i)
# def create_matrix(size:int=3,up_fill:int=0,down_fill:int=0):
#     aa= [[up_fill if i<j  else down_fill if i>j  else j for j in range(1,size+1)] for i in range(1,size+1)]
#     return aa
# print(create_matrix(size=4, up_fill=7, down_fill=9))
# ******************************************************************************
# def count_args(*args):
#     return len(args)
# print(count_args(1, 2, 3))
# ***************************************************************888
# def check_sum(*args):
#     total=0
#     for i in args:
#         total+=i
#     return 'not enough' if total<50 else 'verification passed'
# print(check_sum(8,11))
# ***********************************************************8
# def multiply(*args,a=1):
#     total=[a:=a*i for i in args]
#     return a
# print(multiply(1,2,3,10))
#******************************************************
# def only_one_positive(*args):
#     a=[i for i in args if i>0]
#     return True if len(a)==1 else False
# print(only_one_positive(1,-2,-9,-99))
# *********************************************************8
# def print_goods(*args):
#     a=[v for v in args if type(v) == str and v!='']
#     if len(a) >= 1:
#         for i,v in enumerate(a):
#             print(f'{i+1}. {v}')
#     else:
#         print('Нет товаров')
#
# print_goods(1,90,'ju')

# def print_goods(*args):
#     a=[v for v in args if type(v) == str and v!='']
#     if len(a) >= 1:
#         for i,v in enumerate(a):
#             print(f'{i+1}. {v}')
#     else:
#         print('Нет товаров')
#
# print_goods(1,90,'ju')
# *****************************************************************
# def info_kwargs(**kwargs):
#     for k,v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
# info_kwargs(first_name="John", last_name="Doe", age=33)
#***********************************************************
# def create_actor(**kwargs):
#     d={'name':'Райан',
#        'surname':'Рейнольдс',
#        'age':46 }
#
#     for k,v in kwargs.items():
#         if k not in d:
#             d[k]=v
#     print(d)
# create_actor(height=190, movies=['Дедпул', 'Главный герой'])
#************************************************
# *****************************РЕКУРСИИ****************
# палиндром
# def palindrom(s):
#     if len(s)<=1:
#         return  True
#     if s[0]!=s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom('шалаш'))
# ***************************************************
# def print_from(n):
#     if n>0:
#         print(n)
#         print_from(n-1)
# n=4
# print_from(n)
# ****************************************************88
# def print_to(n):
#     if 1<=n:
#         print_to(n-1)
#         print(n)
# print_to(5)

# def rec(n,l):
#     if n>0:
#         rec(n-1,l)
#         print(l[-n], end=' ')
# n=3
# l=[1,2,3]
# rec(n,l)
# *********************************************************
# def double_fact(n):
#     if n<=2:
#         return n
#     if n>2:
#         return double_fact(n-2)*n
# print(double_fact(7))
# **********************************************************
# ФИБОНАЧЧИ
# def fibanachi(n):
#     if n<=1:
#         return n
#     if n>1:
#         return fibanachi(n-1)+fibanachi(n-2)
#
# print(fibanachi(7))

# def tribonacci(n):
#     if n==0 or n==1:
#         return 0
#     if n==2:
#         return 1
#     if n>2:
#         return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
# n=7
# print(tribonacci(n))
#**************************************************
# def get_combin(n,k):
#     if k==0 or k==n:
#         return 1
#     if 0<k<n:
#         return get_combin(n-1,k)+get_combin(n-1,k-1)
# print(get_combin(5,2))

# def ackermann(m,n):
#     if m==0:
#         return n+1
#     if m>0 and n==0:
#         return ackermann(m-1,1)
#     if m>0 and n>0:
#         return ackermann(m-1,ackermann(m,n-1))
#
# print(ackermann(3,2))

# def list_sum_recursive(l:list):
#     if len(l)==0:
#         return 0
#     return l.pop()+list_sum_recursive(l)
# l=[1,2,3]
# print(list_sum_recursive(l))
# ***************************************************************
# def flatten(a):
#     l = []
#     def flat2(a, l):
#         for elem in a:
#             if type(elem)==list:
#                 flat2(elem, l)
#             else:
#                 l.append(elem)
#     flat2(a, l)
#     return l
# a=[1, [2, 3, [4]], 5]
# print(flatten(a))
#************************************************************
# def flatten_dict(d):
#     d_new={}
#     def f2(currentKey, d, d_new):
#         for key, value in d.items():
#             if type(value) == dict:
#                 f2(currentKey + '_' + key, value, d_new)
#             else:
#                 d_new[currentKey + '_' + key] = value
#     for key,value in d.items():
#         if type(value) == dict:
#             f2(key, value, d_new)
#         else:
#             d_new[key] = value
#     return d_new
# def flatten_dict(d: dict) -> dict:
#     for k, v in d.items():
#         if isinstance(v, dict):
#             d1 = {f'{k}_{k1}': v1 for k1, v1 in v.items()}
#             d.update(d1)
#             del d[k]
#             return flatten_dict(d)
#     return d
# nested = {'Germany': 7,
#           'Europe': {'italy': {'Rome': 3}},
#           'USA': {'washington': 1, 'New York': 4}}
# print(flatten_dict(nested))
#**********************************************************************888
# def zvezda(s):
#     if len(s)==1:
#         return s
#     if len(s)==2:
#         return s[0]+'*'+s[-1]
#     return s[0]+'*'+zvezda(s[1:-1])+'*'+s[-1]
#
# s='aStarCalledTheSu'
# print(zvezda(s))
# ******************************************************
# добавить новую строку справа зеркальную с закрывающимися скобками
# def skobki(s):
#     s1=''
#     for elem in s[::-1]:
#
#         if elem=='(':
#             s1 = s[::-1]
#             s1=s1.replace('(',')')
#     return s+s1
# s='(abc(def(g(ih(k'
# s_new='(abc(def(gg)fed)cba)'
# print(skobki(s))
# ****************************************************************88
# количество отрицательных чисел в наборе
# def count_otris(a):
#     if len(a)==0:
#         return 0
#     else:
#         con=count_otris(a[1:])
#     if a[0]<0:
#         con+=1
#     return con
# a = [ -2, 3, 8, -11, -4, 6 ]
# print(count_otris(a))
# максимальный элемент списка
# def max_rec(a):
#     if len(a)==1:
#         return a[0]
#     if len(a)>1:
#         max_sp=max_rec(a[1:])
#         if a[0]>max_sp:
#             return a[0]
#         else:
#             return max_sp
#
#
# a = [ 500, 2300, 800, 114, 36]
# print(max_rec(a))
#**************************************************************
# функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     pass
#
#
#
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     pass
# *********************************************************
# a=input().lower()
# print(a)
# print("ДА" if a==a[::-1] else 'НЕТ')
#
# a=input().replace('Москва','')
# print(''.join(a))

# a=list(map(str,input().split()))
# if 'Москва' in a:
#      a.remove('Москва')
# print(*a)

# a,b,c,d=list(map(int,input().split()))
# n='811235'
# a=int(n[0])+int(n[1])+int(n[2])
# b=int(n[3])+int(n[4])+int(n[5])
#
# print('ДА'if a==b else 'НЕТ')



# if a<=60:
#     print(1)
# elif a<=64:
#     print(2)
# elif a<=69:
#     print(3)
# else:
#     print(4)
# print(1 if a <= 60 else 2 if a <= 64 else 3 if a <= 69 else 4)
# import time
#
# start = time.time()
# # i=100
# # while i<999:
# #     if i%47==43 and i%3==0:
# #         print(i,end=' ')
# #     i+=1
#
# a,b=100,999
#
# while a<=b:
#     if a%47==43 and a%3==0:
#         print(a, end=" ")
#         a+=47
#     else:
#         a+=1
# end = time.time() - start
# print(end)
# s='World'
#
# starts_with=lambda s: True if s[0]=='W' else False
# print(starts_with(s))
# *********************************************************
# сортировка
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# for i in sorted(subject_marks,key=lambda x: (-x[1],x[0])):
#     print(*i,end='\n')

# СОРТИРОВКА СЛОВАРЯ
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# print(models[0].get('make'))
# for elem in sorted(models,key=lambda x:x['color']):
#     print(f"Производитель: {elem['make']}, модель: {elem['model']}, цвет: {elem['color']}")


# a=[i.split(':') for i in iter(input, 'конец')]
# a=[['Sony PlayStation 5', ' 46000'], ['Телевизор QLED Samsung QE65Q60TAU', ' 87090'],
#    ['Смартфон Samsung Galaxy A11', ' 10000'], ['Планшет Samsung Galaxy Tab S6', ' 26600']]
# for i in sorted(a,key=lambda x:x[1],reverse=True):
#     print(i[0])


#***************************************************************************
# n=6
# d={}
# for i in range(n):
#     name=input()
#     d[name]=d.get(name,0)+1
# print(d)
# dd={}
# for k in sorted(d.items(),key=lambda x: -x[1],reverse=True):
#     if k[1]==max(d.values()) or k[1]==min(d.values()):
#         dd[k[0]]=k[1]
# print(f"{list(dd.keys())[-1]}, {list(dd.values())[-1]}")
# print(f"{list(dd.keys())[0]}, {list(dd.values())[0]}")

# ************************************************************************
# n=3
# d={}
# for i in range(n):
#     phone,name=input().split()
#     d.setdefault(name,[]).append(phone)
# print(d)
# m=3
# for j in range(m):
#     name1=input()
#     print(*d.get(name1,'Неизвестный номер'))

# классический вариант
# n=3
# d={}
# for i in range(n):
#     phone,name=input().split()
#     if name not in d:
#         d[name]=[phone]
#     else:
#         d[name].append(phone)
# # d={'Женя': ['444444', '79129874521'], 'Оля': ['79604845827']}
# print(d)
# m=3
# for j in range(m):
#     name1=input()
#     if name1 in d.keys():
#         print(*d.get(name1))
#     else:
#         print('Неизвестный номер')
#*****************************************************************
# n=4
# months=['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен',
#        'окт', 'ноя', 'дек']
# d={}
# for i in range(n):
#     a=input().split()
#     d.setdefault(a[2],[]).append(a[0])
# d={'янв': ['Саша', 'Карл'], 'июн': ['Артем'], 'июл': ['Коля']}
# print(d)
# m=3
#
# for i in range(m):
#     month=input()
#     print(*sorted(d.get(month,['Нет данных'])))
#************************************************************888
# d={}
# while True:
#     name=input().split(', ')
#     if name[0]=='конец':
#         break
#     d.setdefault(name[0],[]).append(int(name[1]))
# # d={'Зина': [5, 3], 'Гермиона': [4, 4]}
# print(d.items())
# d={k:sum(v)/len(v) for k,v in d.items()}
# for k,v in sorted(d.items(),key=lambda x:(-x[1],x[0])):
#     print(k,v)

# d={'Дили':set(),'Били':set(),'Вили':set()}
# # while True:
# #     name=input().split(': ')
# #     if name[0]=='конец':
# #         break
# #     d.setdefault(name[0],[]).add(name[1])
# d={'Дили': {'aaaa'}, 'Били': {'aaaa', 'aaa'}, 'Вили': set()}
# # for i in iter(input,'конец'):
# #     name = input().split(': ')
# #     d.setdefault(name[0], []).append(name[1])
# print(d)
# # d={'Дили': ['navalny', 'realdonaldtrump', 'joebiden'], 'Били': ['navalny', 'joebiden'],
# #    'Вили': ['realdonaldtrump', 'realdonaldtrump']}
# # d={k:set(v) for k,v in d.items()}
# # print(sorted(d.items()))
# for k,v in sorted(d.items(),key=lambda x:(-len(x[1]))):
#     print(f'Количество уникальных комментаторов у {k} - {len(v)}')

# def color() -> None:
#     g = 'green'
#     def grey() -> None:
#         nonlocal g
#         g = 'grey'
#         print(g)
#     grey()
#     print(g)
# color()
# **********************************************************
# def calculate(x,y,operation='a'):
#     def addition():
#         print(x+y)
#     def subtraction():
#         print(x-y)
#     def division():
#         print(x/y if y>0 else 'На ноль делить нельзя!')
#     def multiplication():
#         print(x*y)
#     if operation=='a':
#         return addition()
#     elif operation=='s':
#         return subtraction()
#     elif operation=='d':
#         return division()
#     elif operation=='m':
#         return multiplication()
#     else:
#         print('Ошибка. Данной операции не существует')
#
# calculate(50,40,'s')
# ***************************************************************
#


# **************************************************************8888
# name=input()
# dd={}
# dd={input():count if input() not in dd else count+1 for i in range(n)}
# print(dd)

# n=int(input())
# summ=(n if n>0 else 1)
# while n!=0:
#     n=int(input())
#     if n>0:
#         summ*=n
#     else:
#         continue
# print(summ)

# n=47
# i=1
# print('слишком большое значение n' if n>=100 else '')
# while i<=n and n<100:
#     if i%3==0 and i%5==0:
#         print(i,end=' ')
#     i+=1
#
# x=20
# day=1
# km=10
# while km<x:
#     km=km+km*.1
#     day+=1
# print(day)

import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
# print(lst_in)
# a=[elem.split() for elem in lst_in]
# b=[elem for elem in a if len(elem)==1]
# for elem in b:
#     print(*elem,end=' ')

# a=['Москва', 'Уфа', 'Караганда', 'Тверь', 'Минск', 'Казань']
# print(*[len(elem) for elem in a])

# n=12
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
# print(*[i for i in range(1,n+1) if n % i == 0])

# n=11
# a=[1 if n%i==0 else 0 for i in range(1,n+1)]
# print(a)
# print('ДА' if sum(a)==2 else 'НЕТ' )

# a=['Москва', 'астрахань', 'новгород', 'димитровград', 'душанбе']
# is_ok = 'ДА'
# last_letter = ''
# for word in a:
#     if last_letter and last_letter != word[0]:
#         is_ok = 'НЕТ'
#         break
#     last_letter = word[-1]
#     if last_letter in ['ь', 'ъ', 'ы']:
#         last_letter = word[-2]
# print(is_ok)
# ************************************************************
# n=21
# # summ=0
# # for i in range(n):
# #     if i%3==0 or i%5==0:
# #       summ+=i
# # print(summ)
#
# sum1=sum([i for i in range(n) if i%3==0 or i%5==0 ])
# print(sum1)
#******************************************************
# поиск подстроки в строке если не найдена вывести -1
# s='Барабанщик бил бой в барабанр'
# a=[]
# a=[s.find('ра',i) for i in range(len(s)) if s.find('ра',i) not in a]
# print(*a)
# for i,val in enumerate(s):
#     if not 'ра' in s:
#         print(-1)
#         break
#     if s[i:i+2]=='ра':
#     # if val=='а' and s[i-1]=='р':
#         print(i,end=' ')

# rez=[i for i in range(len(s)-1) if s[i]=='р' and s[i+1]=='а' ]
# # print(*[i if val=='р' and s[i+1]=='а' else -1 for i,val in enumerate(s) ])
# print(*rez or [-1])
#*************************************************************
# s='+7(123)456-78-99'
# etalon='+7(xxx)xxx-xx-xx'
# result = 'ДА'
# for i in range(len(s)):
#     t = etalon[i]
#     c = s[i]
#     if t=='x':
#         ok = c.isdigit()
#     else:
#         ok = t==c
#     if not ok:
#         result='НЕТ'
#         break
# print(result)
#****************************************************************************
# s=eval('10 + 25 - 12 + 20 - 1 + 3')
# print(s)
# a=[]
# s1='10 + 25 - 12 + 20 - 1 + 3'.replace(' ','').replace('-',' -').replace('+',' +').split()
# print(sum(map(int,s1)))

# txt = input().replace(" ", "").replace("+", " + ").replace("-", " - ")
# print(txt)
# a = [i for i in txt.split()]
# print(a)
# sumshit = int(a[0])
# for i in range(1, len(a) - 1, 2):
#     if a[i] == "+":
#         sumshit += int(a[i + 1])
#         print(a[i+1])
#         print(sumshit)
#     else:
#         sumshit -= int(a[i + 1])
# print(sumshit)

# a=[8, -11, 4, 3, 6]
# print(*list(map(lambda x:x*x,a)))

# a=[8,11,2]
# for i in range(0,len(a)*2,2):
#     a.insert(i+1,a[i])
# print(a)

# a=[8.6, 9.11, -4.567, -10.0, 1.45]
# minn=a[0]
# for i in range(1,len(a)):
#     if a[i]<minn:
#         minn=a[i]
# print(minn)

# a=[-5.67, 3.5, 6.89, -3.0]
# b=[-1.0 if i<0 else i for i in a ]
# print(*b)

# n='4387'
# t=iter(n)
# i=0
# while  len(n)>i:
#     print(next(t),sep='',end=' ')
#     i+=1

 # ВЛОЖЕННЫЕ ЦИКЛЫ
# n=4
# a=[]
# for i in range(n):
#     b=[]
#     for j in range(n):
#         b.append(1)
#     a.append(b)
#     a[i][3]=5

# aa=[[5 if j==n-1 else 1  for j in range(n)] for i in range(n)]
# for i in aa:
#     print(*i)
# **************************************************8888
import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_in=['django chto  eto takoe    poryadok ustanovki',
#          'model mtv   marshrutizaciya funkcii  predstavleniya',
#          'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# a=[]
# for i in range(len(lst_in)):
#     a.append(lst_in[i].split())
#     # print(lst_in[i].split())
#     print('-'.join(lst_in[i].split()))

# print(lst_in)
# for i in range(len(lst_in)):
#     for j in range(len(lst_in[i])):
#         lst_in[i].replace(' '*7,'-')
#
# for i in lst_in:
#     print(i)
# **********************************************
import sys
# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# lst_in = [[1, 0, 0, 0, 0],
#           [0, 0, 1, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 0]]
# print(lst_in)
# s=sum([sum(i) for i in lst_in])
# print(s)
# ok='ДА'
# lst_in2 = [
#     [0,0,0,0,0,0,0]
# ]
# for i in range(len(lst_in)):
#     next_row = [0]
#     for j in range(len(lst_in)):
#         next_row.append(lst_in[i][j])
#     next_row.append(0)
#     lst_in2.append(next_row)
# lst_in2.append( [0,0,0,0,0,0,0])
# for i in lst_in2:
#     print(i)
# for i in range(len(lst_in2)-1):
#     for j in range(len(lst_in2)-1):
#         if lst_in2[i][j] == 1:
#             if lst_in2[i-1][j]+lst_in2[i+1][j]+lst_in2[i][j-1]+lst_in2[i][j+1]!=0:
#                 ok = 'НЕТ'
# print(ok)

# симметрична ли матрица отноистельно главной диагонали
# a=[ [2, 3, 4, 5, 6],
#     [3, 2, 7, 8, 9],
#     [4, 7, 2, 0, 4],
#     [5, 8, 0, 2, 1],
#     [6, 9, 4, 1, 2]]
# flag='ДА'
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i][j]!=a[j][i]:
#             print(a[i][j],a[j][i])
#             flag='НЕТ'
#             break
# print(flag)
# **************************************************88
# a=[8, 11, -53, 2, 10, 11]
# print(a)
# minn=a[0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j]<minn:
#             a[0],a[-1]=a[-1][0]
# print(a)

# a=['Москва', '15000', 'Уфа', '1200', 'Самара', '1090', 'Казань', '1300']
# print([[a[i],int(a[i+1])]for i in range(0,len(a),2)])
# print(b)

# a=[[1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 8, 7, 6],
#     [5, 4, 3, 2]
#    ]
# for i in a[::-1]:
#     for j in i[::-1]:
#         print(j,end=' ')

# a=[1,2,3,4,5,6,7,8,9]
# n1=1
# while n1*n1!=(len(a)):
#    n1+=1
#
# it=iter(a)
# print([[next(it) for j in range(n1)] for i in range(n1)])

# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
# tt=[[j for j in i.split() if len(j)>3] for i in t ]
# print(tt)
# ****************************************************88
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9],
#    [5,4,3]]
# b=[]
# for i in range(len(a)-1):
#     c=[]
#     for j in range(len(a)):
#         c.append(a[j][i])
#         print(a[j][i],end=' ')
#     print()
#     b.append(c)
# print()

# A=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
# for i in A:
#     print(*i)
# *******************************************************8888
# a=list(input().split())
# print(a)
# b=[[i.split('=')[0],int(i.split('=')[1])] for i in list(input().split())]
# d=dict(b)
# print(*sorted(d.items()))
# *********************************************************
import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['5=отлично', '4=хорошо', '3=удовлетворительно']
# print(lst_in)
# # b=list(i.split('=') for i in lst_in)
# bb=[ (int(i.split('=')[0]),i.split('=')[1]) for i in lst_in]
# print(bb)
# d=dict(bb)
# print(*sorted(d.items()))

# lst_in=['5=отлично', '4=хорошо', '3=удовлетворительно']
# print(lst_in)
# b=list(i.split('=') for i in lst_in)
# bb=[ (int(i[0]),i[1]) for i in b]
# print(bb)
# d=dict(bb)
# print(*sorted(d.items()))
# ***********************************************************8888
# b=[i.split('=') for i in list(input().split())]
# d=dict(b)
# flag='ДА'
# for k in ['house','True','5']:
#     if k not in d.keys():
#         flag='НЕТ'
# print(flag)
# ********************************************************
# b=[i.split('=') for i in list(input().split())]
# b=[['лена', 'имя'], ['дон', 'река'], ['москва', 'город'], ['False', 'ложь'],
#     ['3', 'удовлетворительно'], ['True', 'истина']]
# d=dict([i.split('=') for i in list(input().split())])
# if 'False' in d :
#     del d['False']
# if '3' in d:
#     del d['3']
# print(*sorted(d.items()))
# *******************************************************************8
# b=[i for i in list(input().split())]
# print(b)
# b=['+71234567890', '+71234567854', '+61234576890',
#    '+52134567890', '+21235777890', '+21234567110', '+71232267890']
# d={}
# for elem in b:
#     key=elem[:2]
#     if key not in d:
#         d[key]=[elem]
#     else:
#         d[key].append(elem)
# print(*sorted(d.items()))
# *******************************************************************88
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in=[['+71234567890', 'Сергей'], ['+71234567810', 'Сергей'], ['+51234567890', 'Михаил'], ['+72134567890', 'Николай']]
# d={}
# for elem in lst_in:
#     key=elem[1]
#     if key not in d:
#         d[key]=[elem[0]]
#     else:
#         d[key].append(elem[0])
# print(*sorted(d.items()))
# ******************************************************
# import math
# d={}
# while True:
#     n=int(input())
#     if  n==0:
#         break
#     if n not in d:
#         d[n]=round(math.sqrt(n),2)
#         print(round(math.sqrt(n),2))
#     else:
#         print(f'значение из кэша: {d.get(n)}')
# *************************************************************
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # lst_in=['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
# #         'peremennyye-operator-prisvaivaniya-tipy-dannykh',
# #         'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']
# # print(lst_in)
# d={}
# for elem in lst_in:
#     if elem not in d:
#         d[elem]=elem
#         print(f'HTML-страница для адреса {d[elem]}')
#     else:
#         print(f"Взято из кэша: HTML-страница для адреса {d.get(elem)}")
# *************************************************************************
# d = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
#      'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
#      'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
#      'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....',
#      'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
#      'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
# #
# # s='Сергей Балакирев'.upper()
# # for i in s:
# #     print(d.get(i),end=' ')
#
# revers_d={v:k for k,v in d.items()}
# s1='.-- ... . -...- .-- . .-. -. ---'.split()
# a=[revers_d.get(elem).lower() for elem in s1]
# print(''.join(a))
# **************************************************************8888
# a=[8, 11, -4, 5, 2, 11, 4, 8]
# d=dict.fromkeys(i for i in a)
# print(d)
# d={}
# for elem in a:
#     if elem not in d:
#         d[elem]=1
#     else:
#         d[elem]+=1
# print(*d.keys())
#***************************************************************
import sys
# считывание списка из входного потока
# lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in=[['3', 'Сергей'], ['5', 'Николай'], ['4', 'Елена'], ['7', 'Владимир'], ['5', 'Юлия'], ['4', 'Светлана']]
# d={}
# for elem in lst_in:
#     if elem[0] not in d:
#         d[elem[0]]=[elem[1]]
#     else:
#         d[elem[0]].append(elem[1])
# for k,v in d.items():
#     print(f'{k}:',', '.join(v))
# *****************************************************
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# n=100_000
# ost=0
#
# while n!=0 and n>0:
#     if len(things)==0:
#         break
#     for k,v in sorted(things.items(),key=lambda x:x[1],reverse=True):
    # print(k,v)
#**********************************************************************
# a=tuple(map(int,input().split()))
# a=(8, 11, -5, -2, 8, 11, -5)
# print(a)
# # b=[]
# # for elem in a:
# #     if elem not in b:
# #         b.append(elem)
# bb=[]
# bb=[v for i,v in enumerate(a) if v not in a[:i]]
#
# print(*tuple(bb))
# *************************************************************************888
# # a=tuple(map(int,input().split()))
# a=(5, 4, -3, 2, 4, 5, 10, 11)
# print(a)
# # for i,elem in enumerate(a):
# #     if a.count(elem)>1:
# #         print(i, end=' ')
#
# [print(*[i for i,elem in enumerate(a) if a.count(elem)>1])]
# ****************************************************************888
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# n=3
# z=()
# for i in range(n):
#     z+=t[i][:n],
# for i in z:
#     print(*i)
# ***********************************************
import sys
# считывание списка из входного потока
# lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in=[['Главная', 'home'], ['Python', 'learn-python'],
#         ['Java', 'learn-java'], ['PHP', 'learn-php']]
# t=()
# for elem in lst_in:
#     t+=tuple(elem),
# print(t)
# ***************************************
# a=input()
# # a=[-5.1, -3.0, 7.6, 10.3, -4.6, 2.78]
#
# b=set([elem  for elem in a if elem.isdigit() ])
# # for elem in a:
# #     if elem.isdigit():
# #         b.add(elem)
# print(*sorted(b) if b else ["НЕТ"])
#************************************************************
# import sys
# # считывание списка из входного потока
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!',
#         'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю',
#         'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']
# print(lst_in)
# a=set([elem.split(':')[0] for elem in lst_in])
# # for elem in lst_in:
# #     a.add(elem.split(':')[0])
# print(a)
# **********************************8**************************
# a=set()
# while True:
#     s = input()
#     if s=='q':
#         break
#     a.add(s)
# print(len(a))
# *******************************************
# a=set(map(int,input().split()))
# # b=set(input().split())
# # c=set(map(int,input().split())) - set(map(int,input().split()))
# print('ДОПУЩЕН' if 2 in a else 'НЕ ДОПУЩЕН')

# n=210
# a=set()
# for i in range(1,11):
#     if n%i==0:
#         a.add(i)
# print('ДА' if {2,3,5}<a else 'НЕТ')
#******************************************************************8
# s=input().split()
# # print(s)
# # s=['2', 'неудовлетворительно', 'удовлетворительно', 'хорошо', 'отлично']
# print(s)
#
# d={i:v for i,v in enumerate(s[1:],int(s[0]))}
# print(d[4])
#*******************************************************
# import sys
#
# # считывание списка из входного потока
# lst_in = set(map(str.strip, sys.stdin.readlines()))
# # lst_in=['А323ГД', 'Д456ВВ', 'Б001ББ', 'Д456ВВ', 'С111СС']
# print(len(lst_in))

# s=input().lower().split()
# d={elem:s.count(elem) for elem in s}
# print(d['и'] if 'и' in d else 0)

# import sys
# # считывание списка из входного потока
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму',
#         'Пушкин: Евгений Онегин', 'Есенин: Русь']
#
# d={}
# # for elem in lst_in:
# #      if elem.split(': ')[0] not in d:
# #         d[elem.split(': ')[0]]={elem.split(': ')[1]}
# #     else:
# #         d[elem.split(': ')[0]].add(elem.split(': ')[1])
# # print(d)
# dd={}
# dd={elem.split(': ')[0]:{elem.split(': ')[1]} for elem in lst_in}
# s1,s2=input().split()

# фибанвччи
# f1=f2=1
# n=8
# i=2
# a=[1,1]
# while i<n:
#
#     f1,f2=f2,f1+f2
#     i+=1
#     a.append(f2)
# print(*a, end=' ')
# ****************************************
# def IsPrime(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n
#
# n=11
# i=2
# a=[]
# while i<n:
#     i+=1
#     if IsPrime(i) == True:
#         a.append(i)
# print(*a)
# ******************************************************************
# СОРТИРОВАКА ВЫБОРОМ
# a=[8, 11, -53, 2, 10, 11]
#
# for i in range(0, len(a) - 1):
#     min_indx = i
#     for j in range(i + 1, len(a)):
#         if a[j] < a[min_indx]:
#             min_indx = j
#
#     a[i], a[min_indx] = a[min_indx], a[i]
# print(a)
# ******************************************************
# СОРТИРОВКА ВСПЛЫВАЮЩЕГО ПУЗЫРЬКА
# a=[4, 5, 2, 0, 6, 3, -56, 3, -1]
#
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j+1],a[j]=a[j],a[j+1]
# print(a)
# *********************************************888
# ДЕНЕЖНЫЕ КУПЮРЫ
# a=[64, 32, 16, 8, 4, 2, 1]
# print(a)
# n=221
# for v in a:
#     while n >= v:
#        n = n - v
#        print(v, end=' ')
# *****************************************************8
# def url(s):
#
#     set_A = {'A','E','I','O','U','Y','B','C','D','F','G','H','J','K','L','M','N','P','Q','R',
#              'S','T','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_','a','e',
#              'i','o','u','y','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t',
#              'v','w','x','y','z','@','.'}
#     rez=s-set_A
#     print(len(rez))
#     print('ДА' if len(rez)==0  else 'НЕТ')
# s=set('sc_l@iblist.ru')
# # print(s)
# url(s)

# def is_triangle(a,b,c):
#     return True if a<b+c or b<a+c or c<a+b else False
# a,b,c=list(map(int,input().split()))
# print(is_triangle(a,b,c))

# def is_large(s):
#     return False if len(s)<3 else True

# def nechetnoe(a):
#     return a%2!=0
#
# n=list(map(int,input().split()))
# # for elem in n:
# #     if nechetnoe(elem):
# #         print(elem,end=' ')
# lst=[elem for elem in n if nechetnoe(elem)]
# print(*lst)
# ***************************************************************
# tp=input()
# tp='RECT'
# if tp=='RECT':
#     def get_sq(x,y):
#         return x*y
# else:
#     def get_sq(x):
#         return x*x
# **********************************************************
# def dlina_s(s):
#     return len(s)>=6
#
# lst=[c for c in list(input().split()) if dlina_s(c)]
# print(*lst)
# def stroka(st):
#     return st,len(st)
# lst=list(input().split())
# a,b=stroka(lst)
#
# # d={}
# # for elem in lst:
# #     a, b = stroka(elem)
# #     d[a]=b
# d={stroka(elem)[0]:stroka(elem)[1] for elem in lst }
# print(d)
# for key,value in sorted(d.items(),key=lambda x:x[1]):
#     print(key,end=' ')
# *****************************************************
# def max_min(minn,maxx):
#     return minn*maxx
# n=list(map(int,input().split()))
# print(max_min(min(n),max(n)))
#*******************************************************
# быстрый алгоритм Евклида
# def get_nod(a,b):
#     if a<b:
#         a,b=b,a
#     while b!=0:
#         a,b=b,a%b
#     return a
# a=15
# b=121050
# print(get_nod(a,b))
#******************************************
# n=3
# a=[]
# for i in range(1,n+1):
#     b=[]
#     for j in range(1,n+1):
#         b.append(i*j)
#     a.append(b)
# for i in a:
#     print(*i)

# def get_rect_value(a,b,type=0):
#     if type==0:
#         return 2*(a+b)
#     return a*b
# l=get_rect_value(3,4)
# print(l)

# def check_password(st,chars ="$%!?@#"):
#     return  True if (set(st) & set(chars)) and len(st)>=8 else False
#
# st='12345678'
# print(check_password(st))

# def get_latin(st,sep='-'):
#     s_new=[]
#     for elem in st.lower().replace(' ',sep):
#         s_new.append(t.get(elem,elem))
#     return ''.join(s_new)
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# st='Лучший курс по Python!'
# print(get_latin(st))
# print(get_latin(st,sep='+'))
# ************************************************************
# def my_func(st,tag='h1'):
#     return f'<{tag}>{st}</{tag}>'
# st='Работаем с функциями'
# print(my_func(st))
# print(my_func(st,'div'))
# ********************************************************
# def my_func(st,tag='h1',up=True):
#     return f'<{tag.upper()}>{st}</{tag.upper()}>' if up else f'<{tag}>{st}</{tag}>'
# st='Работаем с функциями'
# print(my_func(st,'div'),my_func(st,'div',False),sep='\n')

# def  get_even(*args):
#     return [elem for elem in args if elem%2==0]
# print(get_even(*list(map(int,input().split()))))

# def get_biggest_city(*args):
#     a=max([(len(elem),elem) for elem in args])[1]
#     return a
# a=list(input().split())
# print(get_biggest_city(*a))
# def get_data_fig(*args,**kwargs):
#     d=['type','color','closed','width']
#     # a=[kwargs[k] for k in d if k in kwargs]
#     a=[]
#     for k in d:
#         print(k)
#         if k in kwargs:
#             a.append(kwargs[k])
#             print(kwargs[k])
#     return (sum(args),)+tuple(a)
#
# a=[2,3,4,5]
# print(get_data_fig(1,23,4,5,5,7,width=2,type=True,color=1,closed=False))
# def is_isolate(a):
#    if (a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]+a[i-1][j+1]+
#         a[i-1][j-1]+a[i+1][j+1]+a[i+1][j-1])!=0:
#     return 'НЕТ'
# def verify(a):
#     ok = 'ДА'
#     lst_in2 = [[0,0,0,0,0,0,0] ]
#     for i in range(len(a)):
#         next_row = [0]
#         for j in range(len(a)):
#             next_row.append(a[i][j])
#         next_row.append(0)
#         lst_in2.append(next_row)
#     lst_in2.append( [0,0,0,0,0,0,0])
#     for i in range(len(a) - 1):
#         for j in range(len(a)-1):
#             if a[i][j] == 1:


# def verify(a):
#     n = len(lst_in)
#     ok=True
#     lst_in2 = [ [0]*(n+2)]
#     for i in range(len(lst_in)):
#         next_row = [0]
#         for j in range(len(lst_in)):
#             next_row.append(lst_in[i][j])
#         next_row.append(0)
#         lst_in2.append(next_row)
#     lst_in2.append( [0]*(n+2))
#     for i in lst_in2:
#         print(i)
#     for i in range(len(lst_in2)-1):
#         for j in range(len(lst_in2)-1):
#             if lst_in2[i][j] == 1:
#                 if lst_in2[i-1][j]+lst_in2[i+1][j]+lst_in2[i][j-1]+lst_in2[i][j+1]\
#                         +lst_in2[i-1][j+1]+lst_in2[i-1][j-1]+lst_in2[i+1][j-1]\
#                         +lst_in2[i+1][j+1]!=0:
#                     ok = False
#     return ok
## lst_in = [[1, 0, 0, 0, 0],
#           [0, 0, 1, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 0]]
# print(verify(lst_in))
# ************************************************************
# def str_min(s1,s2):
#     return s1 if s1<s2 else s2
# def str_min3 (s1,s2,s3):
#     return s1 if s1 < str_min(s2,s3) else s2
#
# def str_min4 (s1,s2,s3,s4):
#     ss=str_min(s1,s2)
#     sss=str_min(s3,s4)
#     return ss if ss < sss else sss
# s1='aa'
# s2='my python'
# s3='test'
# s4='bbfucthion'
#
# print(str_min(s1,s2))
# print(str_min3(s1,s2,s3))
# print(str_min4(s1,s2,s3,s4))

import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# d={elem.split('=')[0]:elem.split('=')[1] for elem in lst_in}
# men = {**dict([i.split("=") for i in lst_in])}
# print(men)
# print(**d)
# ************************************************************8
# n=int(input())
# def get_rec_N(n):
#     if n<=0:
#         return
#     get_rec_N(n-1)
#     print(n)
#
# get_rec_N(n)

# def get_rec_sum(a):
#    return a[0] if len(a)==1 else a.pop()+ get_rec_sum(a)
#
# a=[8, 11, -5, 4, 3]
# print(get_rec_sum(a))
# ПОСЛЕДОВАТЕЛЬНОСТЬ ФИБАНАЧЧИ
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# data = list(fibonacci(10))
# print(data)

# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
# a=[5, 4, -3, 4, 5, -24, -6, 9, 0]
# keys=[None,lambda x:x<0,lambda x:x>=0,lambda x:3<=x<=5]
# for i in keys:
#     print(*filter_lst(a,i))
#*************************************************************
# ГЕНЕРАТОРЫ
# a=int(input())
# gen_abs=(abs(x) for x in range(-a,a+1))
# gen_kub=(x**3 for x in gen_abs)
# [print(*[next(gen_kub) for i in range(4)])]
# ***********************************************
# from string import ascii_lowercase
# print(ascii_lowercase)
# asci='abcdefghijklmnopqrstuvwxyz'
# # asci='abcd'
#
# # for i,v in enumerate(asci):
# #     for j,b in enumerate(asci,start=1):
# #         print(v+b,end=' ')
# geb_ascki=( b+v for j,b in enumerate(asci,start=1) for i,v in enumerate(asci))
# [print(*[next(geb_ascki) for i in range(40)])]
# *************************************************************
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen_cities=(i for i in cities*1000000)
# [print(*[next(gen_cities) for i in range(20)])]
# *************************************************************8
# a,b=list(map(int,input().split()))
# a=0
# b=10
# gen_f=(round(0.5*pow(x/100,2)-2.0,2) for x in range(a*100,b*100+1))
# [print(*[next(gen_f) for i in range(20)])]
#*********************************************************************8
# ФУЕКЦИИ ГЕНЕРАТОРЫ
# n=5
# def get_sum(n):
#     for x in range(1,n+1):
#         yield sum(range(1,x+1))
# a=get_sum(n)
# print(list(a))
# *****************************************************************
# def fib_three(n):
#     a,b,c = 1,1,1
#     for x in range(n):
#         if x < 3:
#             yield 1
#         else:
#             yield a + b + c
#             a, b, c = b, c, (a + b + c)
# n=7
# a=fib_three(n)
# for i in range(1,n+1):
#     print(next(a),end=' ')
# ******************************************************
# import random
# random.seed(1)
# indx = random.randint(1, 10)
# print(indx)
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# n=10
# def gen_password(n):
#     for x in chars:

# n=6
# def fact_rec(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fact_rec(n-1)*n
#
# print(fact_rec(n))
# ****************************************************
# УМНОЖЕНИЕ ПО СХЕМЕ МУДРЕЦА
# def simple_multiplication(x, y):
#       return (100-((100-x)+(100-y)))*100 + (100-x)*(100-y)

# def multiplication_check(x, y):
#     return (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y) == x * y
#
# x,y = 97,96
# print(multiplication_check(x,y))
# x,y = 10,10
# print(multiplication_check(x,y))

# def multiplication_check_list(start=10, stop=99):
#     lists_true = [];  lists_false = []
#     for i in range(start,stop+1):
#         for j in range(start,stop+1):
#             if (100 - ((100 - i) + (100 - j))) * 100 + (100 - i) * (100 - j) == i * j:
#                 lists_true.append(1)
#             else:
#                 lists_false.append(1)
#     print(f'Правильных результатов: {len(lists_true)}')
#     print(f'Неправильных результатов: {len(lists_false)}')
# multiplication_check_list(96,97)
# multiplication_check_list(start=50)
# multiplication_check_list(stop=10)
#********************************************************************88
# def wisdom_multiplication(x, y,length_check = False):
#     # length_check = False
#     x = 100 - x
#     y = 100 - y
#     left_num = str(100 - (x + y))
#     right = str(x * y)
#     if length_check and x*y<10:
#         return left_num + '0'+right
#     else:
#         return left_num + right
# x,y = 10, 10
# print(wisdom_multiplication(x,y))
# x,y = 99, 99
# print(wisdom_multiplication(x,y))
# **********************************************
# def multiplication_check_list(start=10, stop=99,length_check = False):
#     lists_true = [];  lists_false = []
#     for i in range(start,stop+1):
#         for j in range(start,stop+1):
#             if (100 - ((100 - i) + (100 - j))) * 100 + (100 - i) * (100 - j) == int(wisdom_multiplication(i,j,length_check = length_check)):
#                 lists_true.append(1)
#             else:
#                 lists_false.append(1)
#     print(f'Правильных результатов: {len(lists_true)}')
#     print(f'Неправильных результатов: {len(lists_false)}')
#
# multiplication_check_list(10,99)
# # *******************************************************************
# engl = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
# rus = "йцукенгшщзхъфывапролджэячсмитьбюё"
#
# d1 = dict(zip(engl,rus))
# d2 = dict(zip(rus,engl))
# d = {**d1,**d2}
# d={'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ',
#    'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о',
#    'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т',
#    'm': 'ь', ',': 'б', '.': 'ю', '`': 'ё', 'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y',
#    'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f',
#    'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c',
#    'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`'}
# print(d)

# d = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
#              'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f',
#              'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z',
#              'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
#              'ё': '`', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
#              'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в',
#              'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
#              'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б',
#              '.': 'ю', '`': 'ё'}

# s = 'qwerty'
# engl = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./`'
# rus = 'йцукенгшщзхъфывапролджэячсмитьбю.ё'
# d1 = {engl[i]:rus[i] for i in range(len(engl))}
# d2 = {rus[i]:engl[i] for i in range(len(rus))}
# d = {**d1, **d2}
# res = [d[i] for i in s]
# r =''
# if s[0] in d:
#     for i in s:
#         r += d.get(i,i)
# print(r)
# ***************************************************************************
# МЕТОД СЛИЯНИЯ 2-Х ОТСТОРТИРОВАННЫХ СПИСКОВ
# a = [2,8,8]
# b = [3,4,5,5,10]
# res = []
# n = 3
# m = 5
# i=0
# j=0
# while i < n and j < m:
#     if a[i] < b[j]:
#         res.append(a[i])
#         i+=1
#     else:
#         res.append(b[j])
#         j+=1
# res += a[i:] + b[j:]
# print(res)
#***********************************************************************8
# n = 4
# m = 5
# a = [1,2,4,6]
# b = [1,5,5,7,9]
#
# i = j = 0
# count = 0
# while i < n and j < m:
#         if abs(a[i] - b[j]) <= 1:
#             count += 1
#             j += 1
#             i +=1
#         elif b[j] < a[i]:
#             j += 1
#         else:
#             i +=1
# print(count)
# *******************************************************
# n = 3
# i = 2
# count = 1
# kub = 1
# while kub < n-1:
#     kub += i
#     count += 1
#     i += 1
#     n = n - kub
#     if n <= 0:
#         print(1)
#         exit(0)
# print(count)
# ***********************************
# a = list(map(int,input().split()))
import collections
# a = [-3, -5, 3, 4, 2, -3, 8, 3, 2, -10]
# print(a)
#
# b= [str(i*i) for i in a ]
# print(' '.join(b))
#
# ФИБАНАЧЧИ
# def gen_fibonacci_numbers(n):
#     f1,f2=0,1
#     for i in range(1,n+1):
#         f1,f2=f2,f1+f2
#     yield f1
# n = 3
# for i in range(n+1):
#     print(*gen_fibonacci_numbers(i),end=' ')

# s = 'Веcичайший урок жизни в том, что и дураки бывают правы.( Уинстон Черчилль )'
# st = 'л'
# # b = [for i in s if st.count(i)]
# print(s.count(st) or len(s))

import numpy as np
# Скалярное произведение векторов
# A = np.array([1.5, 2.5, 3.5])
# B = np.array([4, 5, 6])
# Z = np.dot(A,B)
# print(Z)

# Умножение матриц
# A1= np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# B1 = np.array([
#     [11.5, 12.5, 13.5]
# ])
# try:
#     Z1 = A1.dot(B1)
#     print(Z1)
# except:
#     print('Упс! Что-то пошло не так...')

# Z = np.arange(11)
# Z[(3 < Z) & (Z < 8)] *= -1
#
# print(Z)

# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))


# Z = np.array([-3.1, -5.9, 0, 2.2, 9.8])
#
# print(np.copysign(np.ceil(np.abs(Z)), Z))
# print(np.where(Z>0, np.ceil(Z), np.floor(Z)))

# A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
# B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])
# Z = np.intersect1d(A,B)
# print(Z)

# n = 4
# d = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
# for i in range(n):
#     key, n = input().split()
#     d[key] += int(n)
#
# print(d['восток'] - d['запад'], d['север'] - d['юг'])
#
# import requests
#
# link = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
# with open('dataset_3378_3 (5).txt') as inf:
#     l = inf.readline().strip()
#
# r = requests.get(l)
# r = link + r.text
#
# flag = True
# while(flag):
#     r = requests.get(r)
#     if (r.text.count('.txt')):
#         print(r.text) # Что бы было видно что консоль не просто висит
#         r = link + r.text
#     else:
#         flag = False
#         print(r.text)

# a = [1,2,3,4,5]
#
# for i in range(len(a)-1,0,-1):
#     a[i], a[i-1] = a[i-1], a[i]
# print(a)

# n = 4
# # l = [int(input()) for i in range(n)]
# l = [1,5,1,25]
# flag = 'НЕТ'
# for i in range(len(l)-1):
#     for j in range(1,len(l)-1):
#         if l[i] * l[j] == l[-1] and i != j:
#             flag = 'ДА'
# print(flag)

# t = 'камень'
# r = 'бумага'
# a, b = input(), input()
# op = ['каменьножницы','бумагакамень','ножницыбумага','каменьящерица',
#       'ящерицаСпок','ножницыящерица','ящерицабумага','Споккамень']
# print('ничья' if a == b else 'Тимур' if a + b in op else 'Руслан')

# from itertools import groupby
# s = 'ОООООООООО'
# if 'Р' in s:
#     lst = [(len(tuple(g)),i,c) for i, (c,g) in enumerate(groupby(s)) if c=='Р']
#     print(lst)
#     res = max(lst)
#     print(res[0])
# else: print(0)
# import re
# n = 9
# # lst = [input() for i in range(n)]
# # print(lst)
# lst = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
#        'anton','aoooooooooontooooo','elelelelelelelelelel',
#         'ntoneeee','tonee','253235235a5323352n25235352t253523523235oo235523523523n','antoooooooooooooooooooooooooooooooooooooooooooooooooooon','unton']
# d={}
# for i,elem in enumerate(lst):
#    if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', elem):
#         print(i+1, end=' ')


# import re
# n = int(input())
# lst = [input() for i in range(n)]
# d = {}
# for i,elem in enumerate(lst):
#     if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', elem):
#         d[i+1] = re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', elem)
# print(*d.keys())

# b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# word = 'тимур' + ' запретил букву'
#
# for char in b:
#     if char in word:
#         print(word, char)
#         word = word.replace(' ',' ').replace(char,'').strip()
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for elem in list1:
#    total += sum(elem)
#    counter += len(elem)
# print(total/counter)

# треугольник паскаля
# def pascal(n):
#     triangle = []
#     for i in range(n+1):
#         triangle.append([1] + [0]*n)
#
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
#     for i in range(0, n + 1):
#         for j in range(0, i + 1):
#             print(triangle[i][j], end=" ")
#         print()

# n = 3
# pascal(n)

# Упаковка дубликатов
# s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
# lst = [[s[0]]]
# for i in range(1,len(s)):
#     if s[i-1] == s[i]:
#         lst[-1].append(s[i])
#     else:
#         lst.append([s[i]])
# print(lst)

# Разбиение на чанки
# def chunked(s:str,n:int):
#     lst = []
#     for i in range(0, len(s),n):
#         lst.append([s[i:i+n]])
#     return lst
#
# s = 'a b c d e f'.split()
# n = 2
# print(chunked(s,n))

# Подсписки списка
# s = ['a','b','v']
# new_s = [[]]
# for j in range(1, len(s) + 1):
#     n = 0
#     for i in range(j, len(s) + 1):
#         elem = s[n:i]
#         print(elem)
#         new_s.append(elem)
#         print(new_s)
#         n += 1
# print(new_s)

# a = ['a','b','c','d','e','f']
# n = 2
# lst = []
# for i in range(0,len(a), n):
#     lst.append(a[i:n+i])
# print(lst)
# n = 4
# m = 2
# lst = []
# a = []
# for i in range(n):
#     lst = []
#     for j in range(m):
#         lst.append(input())
#     a.append(lst)
# print(a)

# # a = [[input() for _ in range(m)] for _ in range(n)]
# a = [['и', 'швец'], ['и', 'жнец'], ['и', 'на'], ['дуде', 'игрец']]
# # print(a)
# # [print(*i) for i in a]
# print()
# for i in range(m):
#     for j in range(n):
#         print(a[j][i],end=' ')
#     print()

# След матрицы
# n = 3
# # a = [list(map(int,input().split())) for i in range(n)]
# a= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# summ = sum([a[i][j] for j in range(len(a)) for i in range(len(a)) if i == j])
# print(summ)

# Больше среднего
# n = 4
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[1, 2, 3, 4], [5, 6, 3, 15], [0, 2, 3, 1], [5, 2, 8, 5]]
# for i in range(len(a)):
#     c = 0
#     for j in range(len(a)):
#         if a[i][j] > sum(a[i])/len(a[i]):
#             c += 1
#     print(c)

# Максимальный в области 2
# n = 6
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[1, 4, 9, 9, 4, 7],
#      [6, 9, 8, 6, 7, 4],
#      [1, 1, 6, 1, 1, 1],
#      [1, 4, 5, 8, 7, 5],
#      [6, 7, 8, 1, 1, 0],
#      [6, 9, 9, 9, 7, 7]]
# print(a)
# maxx = a[0][0]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if j <= i <= n-1-j or j >= i >= n-1-j:
#              if a[i][j] > maxx:
#                  maxx = a[i][j]
# print(maxx)

# n = 4
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [3, 4, 5, 6], [1, 2, 3, 4]]
# print(a)
# c1 = c2 = c3 = c4 = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if (i < j and i< n-1-j):   c1 += a[i][j]
#         elif (i<j and i>n-1-j) :   c2 += a[i][j]
#         elif (i>j and i>n-1-j):    c3 += a[i][j]
#         elif (i>j and i<n-1-j):    c4 += a[i][j]
# print('Верхняя четверть:',c1)
# print( 'Правая четверть:', c2)
# print('Нижняя четверть:', c3)
# print('Левая четверть:', c4)

# n = 4
# m = 6
# mult = []
# for i in range(n):
#     l = []
#     for j in range(m):
#         l.append(i*j)
#     mult.append(str(l).ljust(3))
# for i in mult:
#     print(*i)

# mult = [[str(i*j).ljust(3) for j in range(m)] for i in range(n)]
# for i in mult:
#     print(*i)

# n = 2
# m = 8
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[4, 3, 4, 4, 1, 2, 2, 3], [2, 3, 0, 3, 3, 4, 4, 5]]
# print(a)
#
# q,w = 0,0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > a[q][w]:
#             q,w = i,j
# print(q,w)

# n = 2
# m = 8
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# print(matrix)
# matrix2 = sum(matrix, [])
# print(matrix2)
# maxx = max(matrix2)
# print(maxx)
# position = matrix2.index(maxx)
# print(position)
# print(position// m, position % m)

# n = 4
# m = 9
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[71, 14, 41, 13, 57, 22, 24, 21, 13],
#      [12, 74, 11, 13, 81, 22, 24, 21, 23],
#      [12, 14, 82, 13, 25, 72, 24, 21, 23],
#      [12, 14, 11, 13, 25, 22, 10, 21, 23]]
# print(len(a))
# q, w = 5, 3
# b = [a[i][q], a[i][w] = a[i][w], a[i][q] for i in range(n)]
# for i in range(n):
#      a[i][q], a[i][w] = a[i][w], a[i][q]
#
# [print(*i) for i in a]

# Симметричная матрица
# 1) variant
# n = 3
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[0, 1, 2], [1, 2, 7], [2, 3, 4]]
#
# flag = 'YES'
# for i in range(len(a)):
#      for j in range(len(a)):
#           if a[i][j] != a[j][i]:
#                flag = 'NO'
#                break
#
# print(flag)
# транспонированная матрица
# 2) variant
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# m_transpose = [list(x) for x in zip(*matrix)]
# print("YES" if matrix == m_transpose else "NO")
# ******************************************************************
# Обмен диагоналей
# n = 3
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[1,2,3], [4,5,6], [7,8,9]]
# for i in range(len(a)):
#      a[i][i], a[n-1-i][i] = a[n-1-i][i], a[i][i]
# [print(*i) for i in a]
# *********************************************************
# Зеркальное отображение
# n = 3
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)
# a.reverse()
# # for i in range(n):
# #      for j in range(n):
# #           a[i][j], a[n - 1 - i][j] = a[n - 1 - i][j], a[i][j]
#
# [print(*i) for i in a]
# Поворот матрицы на 90 по часовой стрелке.
# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# for j in range(len(a)):
#      for i in range(len(a)):
#           print(a[n-1-i][j], end=' ')
#      print()
# *********************************************************8888
# Магический квадрат
# n = 3
# # a = [list(map(int,input().split())) for i in range(n)]
# a= [[8, 1, 6],
#      [3, 5, 7],
#      [4, 9, 2]]

# sum_rows = []
# sum_column = []
# for i in a:
#      if sum(i) not in sum_rows:
#           sum_rows.append(sum(i))
# for i in zip(*a):
#      if sum(i) not in sum_column:
#           sum_column.append(sum(i))
# sum_rows = [sum(row) for row in a]
# sum_column=[sum(col) for col in zip(*a)]
#
# sum_gl = [a[i][j] for j in range(len(a)) for i in range(len(a)) if i == j]
# sum_pob = [a[i][j] for j in range(len(a)) for i in range(len(a)) if j == n-1-i]
# print(sum_rows)
# print(sum_column)
# print(sum(sum_gl))
# print(sum_pob)
# # print(sum_rows[0]==sum(sum_gl))
# print('YES' if sum_rows[0]==sum(sum_gl)==sum(sum_pob)==sum_column[0] and set(sum(a,[])) == set(range(1,n*n+1)) else 'NO')


# n = int(input())
# a = [list(map(int,input().split())) for i in range(n)]
# sum_rows = []
# sum_column = []
# for i in a:
#     if sum(i) not in sum_rows:
#         sum_rows.append(sum(i))
# for i in zip(*a):
#     if sum(i) not in sum_column:
#         sum_column.append(sum(i))
# sum_gl = [a[i][j] for j in range(len(a)) for i in range(len(a)) if i == j]
# sum_pob = [a[i][j] for j in range(len(a)) for i in range(len(a)) if j == n-1-i]
# print('YES' if sum_rows[0]==sum(sum_gl)==sum(sum_pob)==sum_column[0] and set(sum(a,[])) == set(range(1,n*n+1)) else 'NO')
# ****************************************************
# заполнить в шахматном порядке
# import numpy as np
# n, m = map(int,input().split())
# x = np.array([['.', '*'],['*', '.']])
# Z = np.tile(x,(n//2+1,m//2+1))
# Z = Z[:n, :m]
# for i in Z:
#      print(*i)
# ****************************************************************
# Побочная диагональ
# n = 4
# a = [[1 if j == n-1-i else 2 if i+j >= n else 0 for j in range(n)] for i in range(n)]
# for i in a:
#      print(i)
#
# n = int(input())
# a = []
# for i in range(n):
#     l = []
#     for j in range(n):
#         if j == n-1-i:   l.append(1)
#         elif i+j >= n:   l.append(2)
#         else:            l.append(0)
#     a.append(l)
# [print(*i)for i in a]
# ********************************************************************************
# Заполнение 1
# n = 3
# m = 4
# a = []
# k = 1
# for i in range(1, n+1):
#      l = []
#      for j in range(k, m+k):
#           l.append(j)
#           k = j + 1
#      a.append(l)
# for i in a:
#      print(i)
# ****************************************************************
# n = 7
# m = 3
# a = []
# k = 1
# for i in range(1, n+1):
#      l = []
#      for j in range(k, m+k):
#           l.append(j)
#           k = j + 1
#      a.append(l)
# for j in range(m):
#     for i in range(n):
#         print(a[i][j], end=' ')
#     print()
#****************************************************************
# n = 5
# a = []
# for i in range(n):
#      l = []
#      for j in range(n):
#           if i==j or j ==n-1-i:
#                l.append(1)
#           else:
#                l.append(0)
#      a.append(l)

# a = [[1 if (i<=j and i<=n-1-j) or (i>=j and i>=n-1-j) else 0 for j in range(n)] for i in range(n)]
# [print(*i) for i in a]

# ********************************************************************88
# Заполнение 5
# n = 3
# m = 7
# a = [[(i+j)%m+1 for j in range(-1, m-1)] for i in range(1,n+1)]
# for i in a:
#      print(*i)
# ********************************************************************
# n = 3
# m = 5
#
# a = []
# k = 1
# for i in range(1, n+1):
#      l = []
#      for j in range(k, m+k):
#           l.append(j)
#           k = j + 1
#      if i%2!=0:   a.append(l)
#      else:        a.append(l[::-1])
# for i in a:
#      print(*i)

# **************************************************888
# n = 3
# m = 5
# a = []
# l = n*m
# for i in range(n):
#      l = []
#      for j in range(m):
#           if i+j == l:
#                l.append(j)
#      a.append(l)
#
# for i in a:
#      print(*i)
import numpy as np
# n = 2
# m = 4
# a = [[1,2,3,4],
#      [5,6,7,1]]
# b= [[3,2,1,2],
#     [1,3,1,3]]
# A= np.array(a)
# B = np.array(b)
# for i in A+B:
#      print(*i)
import numpy as np
# n, m = 2, 4
# A = np.array((map(int,input().split())) for i in range(n))
# print(A)
# B = np.array([list(map(int,input().split())) for j in range(n)])
# print(B)
#
# [print(*i) for i in A+B]
# n = 3
# m = 2
# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
#
# A = np.array(a)
# res = np.linalg.matrix_power(a,m)
# for i in res:
#      print(*i)

# n = 5
# k = 2
# res = 0
# for i in range(1,n+1):
#      res = (res + k)% i
#
# print(res+1)

# n = list(input())
# n= ['1', '2', '3', '4', '5']
# print(n)

# c = 3
# for i in range(len(n)-3,0,-3):
#      n.insert(i,',')
#
# print(''.join(n))

# n= ['1', '2', '3', '4', '5','6']
# sn = ''
# c = 3
# count = 0
# for i in range(len(n)-1,-1,-1):
#      sn += n[i]
#      count +=1
#      if count%3 == 0 and count!= len(n):
#           sn += ','
#
# print(sn[::-1])

# num = input()
# for idx in range(len(num) - 3, 0, -3):
#     num = num[:idx] + ',' + num[idx:]
#     print(num)
#     print(idx)
# print(num)

# n = '25000'
# st = ''
# print(int(n[:-5] + n[-5:][::-1]))

# n = 1945
# years = {0:    'Обезьяна', 1: 'Петух', 2: 'Собака', 3:    'Свинья', 4: 'Крыса', 5: 'Бык',
#         6: 'Тигр', 7: 'Заяц', 8: 'Дракон', 9: 'Змея', 10: 'Лошадь', 11: 'Овца'}
# print(years[n%12])

# s = 'Я собираюсь сделать ему предложение, от которого он не сможет отказаться.'
#
# print(len(s)*0.6)
# kop = len(s)*60
# print(kop)
# print(f'{kop//100} р. {kop%100} коп.')
#
# import functools
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# a = functools.reduce(lambda x,y:x*y,list(numbers))
# print(a)

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# a = [sum(i)/len(i) for i in numbers]
# print(a)

# ТРИБАНАЧЧИ0
# n = 10
# t1, t2, t3 = 1, 1, 1
# for i in range(10):
#     print(t2, end = ' ')
#     t1, t2, t3 = t3, t1, t1 + t2 + t3

# n = 5
# # a = [input().lower() for i in range(n)]
# a = ['aaa', 'bb', 'ccc', 'dddd', 'ppppp']
# b = ''.join(a)
# print(len(set(b)))

# import string
# s = 'Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. ' \
#     'Making a blanket, soft and white. Making a blanket in the night.'.lower()
# ss = s.translate(str.maketrans('', '', string.punctuation)).split()
# print(ss)
# print(len(set(ss)))
# s = 'Snowflakes, snowflakes falling down.'
# print([w.strip('.,;:-?!') for w in s.lower().split()])

# a = [1,1, 2, 2, 5, 5, 5, 5, 6, 7, 8]
# b = set()
# for i,val in enumerate(a):
#      if val not in b:
#           print('NO')
#           b.add(val)
#      else:
#           print('YES')

# n = 6
# # a = ['1234567890','87654321','34567890','987234356','1236789','987532']
# a = [input() for i in range(n)]
# rez = set()
# for i in range(1,len(a)):
#
#      a[i] = set(a[i-1]).intersection(set(a[i]))
#      if i == len(a)-1:
#           print( *sorted(set(a[i-1]).intersection(set(a[i]))))

# a = set([2,9,3,4,6,9])
# b = set([2,3,4,5,2,10])
# c = set([2,3,4,5,3,10])
# r = (a | b | c )-(a & b & c)
# print(*sorted(r))


# n = int(input())
# a = [list(map(int,input().split())) for i in range(n)]
# sum_rows = [sum(row) for row in a]
# print(sum_rows)
# sum_column=[sum(col) for col in zip(*a)]
# print(sum_column)
# sum_gl = [a[i][j] for j in range(len(a)) for i in range(len(a)) if i == j]
# print(sum_gl)
# sum_pob = [a[i][j] for j in range(len(a)) for i in range(len(a)) if j == n-1-i]
# print(sum_pob)
# s_r = sum_rows[0]
#
# if_1 = len(set(sum_rows))+len(set(sum_column))==2
# print('YES' if s_r==sum(sum_gl)== sum(sum_pob) and set(sum(a,[])) == set(range(1,n*n+1)) and if_1 else 'NO')

# a = set([2,9,2,4,6,10])
# b = set([2,2,4,5,2,10])
# c = set([2,3,4,5,3,9])
# s = a|b
# r = s - c
# print(r)
# *******************************************************
# МАГИЧЕСКИЙ КВАДРАТ
# n = 4
# # a = [list(map(int,input().split())) for i in range(n)]
# a = [[7, 12, 1, 14],
#      [2, 13, 8, 11],
#      [16, 3, 10, 6],
#      [9, 5, 15, 4]]
#
# glav = 0
# pob = 0
# rows = []
# prev_row_sum = 0
# curr_row_sum = 0
# flag = True
# column_sums = [0 for j in range(len(a))]
#
# for i in range(len(a)):
#      curr_row_sum = sum(a[i])
#      if prev_row_sum and prev_row_sum != curr_row_sum:
#           flag = False
#           break
#      prev_row_sum = curr_row_sum
#      for j in range(len(a)):
#           column_sums[j] += a[i][j]
#           if i == j:
#                glav += a[i][j]
#           elif j == n-1-i:
#                pob += a[i][j]
# #      print (column_sums)
# # print('главная', glav)
# # print('побочная', pob)
# # print('rows', curr_row_sum)
# # print(column_sums)
# # print(len(set(column_sums)))
#
# print('YES' if flag and len(set(column_sums))==1 and column_sums[0]==glav==pob==curr_row_sum and set(sum(a,[])) == set(range(1,n*n+1)) else 'NO')
# print('____________________________')
#
#
# # sum_rows = [sum(row) for row in a]
# # sum_column=[sum(col) for col in zip(*a)]
# # sum_gl = [a[i][j] for j in range(len(a)) for i in range(len(a)) if i == j]
# # sum_pob = [a[i][j] for j in range(len(a)) for i in range(len(a)) if j == n-1-i]
# # s_r = sum_rows[0]
# # print(sum(sum_gl))
# # print(sum(sum_pob))
# #
# # if_1 = len(set(sum_rows))+len(set(sum_column))==2
# # print('YES' if s_r==sum(sum_gl)== sum(sum_pob) and set(sum(a,[])) == set(range(1,n*n+1)) and if_1 else 'NO')
# *******************************************************************
import re


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three,
# and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells
# of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy
#  had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# words = re.sub(r'[.,;:-?-!)(]', '', sentence)
# # myset = set(words.split())
# myset = {i.lower() for i in words.split()}
# print(*sorted(myset))

# words = re.sub(r'[.,;:-?-!)(]', '', sentence)
# myset = set(words.split())
# print(*sorted(myset))


# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt',
#          'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png',
#          'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
#
# myset = {i.lower() for i in files if i.lower().endswith('png')}
# print(*sorted(myset))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'}]
# 1
# names = [elem['name'] for elem in users if 'email' not in elem.keys() or not elem['email']]
# 2
# for elem in users:
#     if 'email' not in elem.keys() or not elem['email']:
#         names.append(elem['name'])
# 3
# names = []
# for elem in users:
#     if elem.get('email','') == '':
#         names.append(elem['name'])
# print(*sorted(names))
# ***************************************
# n = 230
# my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# # for i in str(n):
# #     print(my_dict[i], end=' ')
# print(*[my_dict[i] for i in str(n)])

# courses = {'CS101': ['3004', 'Хайнс', '8:00'],
#            'CS102': ['4501', 'Альварадо', '9:00'],
#            'CS103': ['6755', 'Рич', '10:00'],
#            'NT110': ['1244', 'Берк', '11:00'],
#            'CM241': ['1411', 'Ли', '13:00']}
# n = 'CS101'
# a,b,c = courses[n]
# print(f'{n}: {a}, {b}, {c}')
# ****************************************************************
# Набор сообщений На мобильных кнопочных телефонах
# 1
# import time
# start = time.time() ## точка отсчета времени
# my_spis = [' ', '.,?!:','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# ss = "The universe is enormous, so the chances of us being the only living creatures are small. Although we think we are intelligent and that we know a lot about Space, we have only explored a very small area. We might be the only creatures that can travel in Space, but it is unlikely.In fact, some people say that we might have been visited by aliens. These people point to 'wonders' such as Stonehenge in Britain and the Nazca lines in Peru as proof that aliens have been here.So, what are the chances that there is life out there?".upper().replace("'",'')
# s = ss*1000
# letters = {}
# for i,symbols in enumerate(my_spis):    #формируем словарь
#     for pos,symbol in enumerate(symbols):
#         letters[symbol] = str(i)*(pos+1)
# print(*[letters[elem] for elem in s],sep='')
# end = time.time() - start ## собственно время работы программы
# print('--------------------')
# print(end) #1.959594488143921

# 2 вариант долгий и не оптимальный
# import time
# start = time.time() ## точка отсчета времени
# d = {1:	'.,?!:',
#      2:	'ABC',
#      3: 'DEF',
#      4:	'GHI',
#      5: 'JKL',
#      6:	'MNO',
#      7:	'PQRS',
#      8:	'TUV',
#      9:	'WXYZ',
#      0:	' '}
# ss = "The universe is enormous, so the chances of us being the only living creatures are small. Although we think we are intelligent and that we know a lot about Space, we have only explored a very small area. We might be the only creatures that can travel in Space, but it is unlikely.In fact, some people say that we might have been visited by aliens. These people point to 'wonders' such as Stonehenge in Britain and the Nazca lines in Peru as proof that aliens have been here.So, what are the chances that there is life out there?".upper().replace("'",'')
# s = ss*1000
# for elem in s:
#     for key, val in d.items():
#         if elem in val:
#             print(str(key)*(val.index(elem)+1), end='')
# end = time.time() - start ## собственно время работы программы
# print('--------------------')
# print(end) #3.4442665576934814
#**********************************************************
# s = 'Agent007'.upper().re
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse_code = {char: morse[ind] for ind, char in enumerate(letters)}
# print(*[morse_code[i] for i in s])

# import string
# s = input().upper()
# s = s.translate(str.maketrans('', '', string.punctuation+' '))
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse_code = {char: morse[ind] for ind, char in enumerate(letters)}
# print(*[morse_code[i] for i in s])

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# # result = {k:dict2.get(k,0)+v for k,v in dict1.items() }
# # print(result)
# result = dict2.copy()
# for k,v in dict1.items():
#     result[k] = result.get(k,0)+v
# print(result)

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {elem : text.count(elem) for elem in text}
# print(result)

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate ' \
#     'banana banana orange barley apricot plum grapefruit banana quince strawberry barley ' \
#     'grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry ' \
#     'apricot currant orange lime quince grapefruit barley banana melon pomegranate barley ' \
#     'banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry ' \
#     'apple barley apricot currant orange melon pomegranate banana banana orange apricot barley ' \
#     'plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana ' \
#     'quince barley lime grapefruit pomegranate barley'.split()
# my_dict = {elem:s.count(elem) for elem in s}
# print(sorted(my_dict.items(),key = lambda x: (-x[1],x[0]))[0][0])

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),  ]
# 1
# result = {}
# for pet in pets:
#     key = (pet[1],pet[2],pet[3])
#     result.setdefault(key,[]).append(pet[0])
# print(result)
# 2
# result = {}
# for pet in pets:
#     result.setdefault(pet[1:],[]).append(pet[0])
# print(result)
# ******************************************************
# import string
# s = 'I bought two books: a new book and an old book. The new book was more expensive than the old book.'.lower()
# ss = s.translate(str.maketrans('', '', string.punctuation)).split()
# result = {elem: ss.count(elem) for elem in ss}
# print(sorted(result.items(),key=lambda x:(x[1],x[0])))

# Самое редкое слово
# s = 'I bought two books: a new book and an old book. an The new book was more expensive than the old book.'.lower().split()
# d = {}
# for elem in s:
#      d[elem.strip(',.;:!?')] = d.get(elem.strip(',.;:!?'),0) + 1
# print(sorted(d.items(),key=lambda x:(x[1],x[0]))[0][0])
# **************************************************************************
# Исправление дубликатов
# 1
# s = 'a b c a a d c'.split()
# d = {}
# dd = {}
# s_new = []
# for elem in s:
#     dd[elem] = dd.get(elem, 0) + 1
#     s_new.append(f'{elem}{f"_{dd[elem]-1}" if dd[elem]>1 else ""}')
# print(*s_new)
# print(d)
# print(dd)

# 2
# s = 'a b c a a d c'.split()
# d = {}
# s_new = []
# for elem in s:
#     if elem not in d:
#         d[elem] = 1
#         s_new.append(elem)
#     else:
#         s_new.append(f'{elem}_{d[elem]}')
#         d[elem] += 1
# print(*s_new)
# ***********************************************************88
# Словарь программиста
# n = 5
# # d = {}
# # for i in range(n):
# #     key, value = input().split(': ')
# #     d[key.lower()] = value
# d ={'змея': 'язык программирования Python',
#     'баг': 'от англ. bug — жучок, клоп, ошибка в программе',
#     'конфа': 'конференция',
#     'костыль': 'код, который нужен, чтобы исправить несовершенство ранее написанного кода',
#     'бета': 'бета-версия, приложение на стадии публичного тестирования'}
# print(d)
# m = 3
# for i in range(m):
#     print(d.get(input().lower(), 'Не найдено'))
# ***************************************************************88
# Анаграммы 1
# s1 = 'thing'
# d1 = {elem: s1.count(elem) for elem in s1}
# s2 = 'night'
# d2 = {elem: s2.count(elem) for elem in s2}
# print('YES' if d1 == d2 else 'NO')
# ***************************************************************88
# Анаграммы 2
# import string
# s1 = 'С мая весной'.lower()
# ss1 = s1.translate(str.maketrans('', '', string.punctuation + ' '))
# d1 = {elem: ss1.count(elem)  for elem in ss1}
# print(d1)
# s2 = 'сам я не свой'.lower()
# ss2 = s2.translate(str.maketrans('', '', string.punctuation + ' '))
# d2 = {elem: ss2.count(elem)  for elem in ss2}
# print(d2)
# print('YES' if d1 == d2 else 'NO')
# &****************************************************************
# Словарь синонимов
# 1
# n = 4
# d = {}
# for i in range(n):
#     key, val = input().split()
#     d[key] = val
#     d[val] = key
# print(d[input()])
# # 2
# n = 4
# d = {}
# for i in range(n):
#     key, val = input().split()
#     d[key], d[val] = val, key
# print(d[input()])
# ***************************************************************88
# Страны и города
# n = 1
# d = {}
# for i in range(n):
#     country, *city = input().split()
#     for j in city:
#         d[j] = country
#
# m=4
# for i in range(m):
#     print(d[input()])
# ***************************************************************88
# Телефонная книга
# n = 3
# d= {}
# for i in range(n):
#     phone, name = input().lower().split()
#     d.setdefault(name,[]).append(phone)
# print(d)
# m = 3
# for j in range(m):
#     print(d.get(input().lower(),'абонент не найден'))
# **************************************************************************888
# Секретное слово
# 1
# s = '*!*!*?'
# d = {}
# n = 3
# # for i in range(n):
# #     k,v = input().split(': ')
# #     d[k] = int(v)
# d = {'а': 3, 'н': 2, 'с': 1}
# print(d)
# s_new = ''
# for char in s:
#     for key,val in d.items():
#         if s.count(char) == val:
#             s_new += key

#  2
# s = '*!*!*?'
# d = {}
# n = 3
# # for i in range(n):
# #     k,v = input().split(': ')
# #     d[k] = int(v)
# d = {3:'а',2: 'н', 1:'с'}
# print(d)
# s_new = ''
# for i in s:
#     print(d[s.count(i)])
# *******************************************************
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow',
#           'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black',
#           'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure',
#           'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl',
#           'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {}
# for key,val in colors.items():
#     if val is not None:
#         result[key] = val
# print(result)
# *******************************************************
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {key: val for key,val in favorite_numbers.items() if 9 < val < 100}
# print(result)
#
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'.split()
# result = {elem.split(':')[0]: elem.split(':')[1] for elem in s}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {}
# for key in numbers:
#     for num in range(1, key+1):
#         if key % num == 0:
#             result.setdefault(key,[]).append(num)
# print(result)

# элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# # 1
# result = {}
# for elem in words:
#     for char in elem:
#         result.setdefault(elem,[]).append(ord(char))
# print(result)
# # 2
# dd = {elem: [ord(char) for char in elem] for elem in words}
# print(dd)

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {k: v for k,v in letters.items() if k not in remove_keys}
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70),
#             'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {}
# for k,v in students.items():
#     if v[0] > 167 and v[1] < 75:
#         result[k] = v
# print(result)
# result = {k: v for k,v in students.items() if v[0] > 167 and v[1] < 75}

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {elem[0]:elem[1:] for elem in tuples}
# print(result)
# ***********************************************************
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = []
# my_dict = [{a: {b:c}} for a,b,c in zip(student_ids,student_names,student_grades) ]
#
# print(my_dict)
# ****************************************************
# n = 4
# dd = {}
# s_new = []
# for i in range(n):
#     code = input()
#     dd[code] = dd.get(code, 0) + 1
#     print(f"{code}{dd[code]-1}" if dd[code]>1 else "OK")
#     ****************************************************************

# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595')]
# my_dict = {elem[0]: {'salary':elem[1],'gender':elem[2],'passport':elem[3]} for elem in persons}
# print(my_dict)
# data = {
#     "my_friends": {
#         "count": 10,
#         "people": [{
#             "first_name": "Kurt",
#             "id": 621547005,
#             "last_name": "Cobain",
#             "bdate": "31.8.2005"
#         }, {
#             "first_name": "Виолетта",
#             "id": 484200150,
#             "last_name": "Кастилио",
#         }, {
#             "first_name": "Иринка",
#             "id": 21886133,
#             "last_name": "Бушуева",
#             "bdate": "28.8.1942"
#         }, {
#             "first_name": "Данил",
#             "id": 282456573,
#             "last_name": "Греков",
#             "bdate": "4.7.2002"
#         }, {
#             "first_name": "Валентин",
#             "id": 184902932,
#             "last_name": "Долматов",
#             "bdate": "25.5"
#         }, {
#             "first_name": "Евгений",
#             "id": 620469646,
#             "last_name": "Шапорин",
#             "bdate": "6.12.1982"
#         }, {
#             "first_name": "Ангелина",
#             "id": 622328862,
#             "last_name": "Краснова",
#             "bdate": "4.11.1995"
#         }, {
#             "first_name": "Иван",
#             "id": 576015198,
#             "last_name": "Вирин",
#             "bdate": "2.2.1915"
#         }, {
#             "first_name": "Паша",
#             "id": 386922406,
#             "last_name": "Воронов",
#             "bdate": "27.9"
#         }, {
#             "first_name": "Ольга",
#             "id": 622170942,
#             "last_name": "Савченкова",
#             "bdate": "20.12"
#         }]
#     }
# }
#
# names = []
# for frend in data['my_friends']['people']:
#    names.append(frend['first_name'])
#
# print(*sorted(names),sep='\n')

# s = 'дуб дуб я осина как меня слышно прием прием как слышно билет номер восемь повторяю билет номер восемь номер восемь прием'
# d = {}
# for elem in s.split():
#     print(d.get(elem,0),end=' ')
#     d[elem] = d.get(elem,0) + 1

# n = 8
# d = {}
# for i in range(n):
#     name, title = input().split('\t')
#     d.setdefault(name,[]).append(title)

# d = {'Александ Пушкин': ['Цыганы', 'Пиковая дама', 'Медный всадник'], 'Антон Чехов': ['Беседа пьяного с трезвым чертом', 'Студент'], 'Иван Тургеньев': ['Бежин луг', 'Рудин', 'Записки охотника']}
#
# print(d)
# m=3
# for j in range(m):
#     name = input()
#     r = d.get(name,['Нет в списке'])
#     print(*r,sep=', ')

# n = 2
# d = {}
# for i in range(n):
#     k, v = input().split()
#     d[k], d[v] = v, k
# print(d[input()])

# s = 'a aa abC aa ac abc bcd a'.lower().split()
# d = {}
# for elem in s:
#     d[elem] = d.get(elem,0) + 1
# print(d)

# s = [str(i) for i in input().lower().split()]
# w = 0
# d = {}
# for i in range(len(s)):
#     a = s[i]
#     for k in s:
#         if k == a:
#             w += 1
#         else: continue
#     d[a] = w
#     w = 0
# for key,value in d.items():
#     print (key, value)


# def generate_ip():
#     return f'{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}'
# print(generate_ip())
# import random, string
# from string import ascii_uppercase
# def generate_index():
#     maska = 'LLN_NLL'
#     code = ''
#     for i in maska:
#         if i == 'L':      code += random.choice(ascii_uppercase)
#         elif i == 'N':    code += str(random.randrange(100))
#         else:             code += i
#     return code
# print(generate_index())
# def generate_index1():
#     f'{}{}{}_{}{}{}'

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for row in matrix:
#     random.shuffle(row)
#     print(row)
# ******************************************************************888
# генерирует 100 случайных номеров лотерейных билетов
# tickeds = set()
# n = 0
# while n<100:
#     tic = str(random.randrange(1,10))
#     while len(tic) < 7:
#         tic += str(random.randrange(0,10))
#     n += 1
#     if tic not in tickeds:
#         tickeds.add(tic)
# print(*tickeds,sep='\n')
# ****************************************************************88
# import random
# word = list('apple')
# random.shuffle(word)
# print(''.join(word))
# *******************************************************************8
# бинго
# import random
# myset = random.sample(range(1, 76), 25)
# bingo = [myset[i: i+5] for i in range(0, len(myset),5)]
# bingo[2][2] = 0
# for i in bingo:
#     print(*(str(k).ljust(3) for k in i))


# import random
# myset = set()
# while len(myset)<25:
#     myset.add(str(random.randint(1,75)).ljust(3))
# myset = list(myset)
# myset[12] = str(0).ljust(3)
# bingo = [myset[i: i+5]for i in range(0, len(myset),5)]
# [print(*i)for i in bingo]
# ************************************************************************
# генерирует 100 случайных номеров лотерейных билетов
# tickeds = set()
# n = 0
# while n<100:
#     tic = random.sample(range(1, 10), 1) + random.sample(range(0, 10), 6)
#     n += 1
#     if ''.join(str(tic)) not in tickeds:
#         tickeds.add(''.join(str(tic)))
# # print(*tickeds,sep='\n')
# for i in tickeds:
#     print(''.join(i))
# import random
# n = 3
# a = []
# # for i in range(n):
# #     name = input()
# #     a.append(name)
# names = ['Светлана Зуева', 'Аркадий Белых', 'Борис Боков']
# lastIndex = len(names)-1
# while True:
#     nah = []
#     for cur_index in range(len(names)):
#         if cur_index == lastIndex and cur_index not in nah:
#             # print ('error, restart')
#             break
#         r = random.randint(0, lastIndex)
#         while r == cur_index or r in nah:
#             r = random.randint(0, lastIndex)
#         nah.append(r)
#         # print(f'{names[cur_index]} - {names[r]}')
#     if len(nah)==len(names):
#         break
# for i in nah:
#     print(f'{names[i]} - {names[nah[i]]}')



# cur_index = 1
# r = random.randint(0,2)
# while r == cur_index:
#     r = random.randint(0, 2)
# print(f'{names[cur_index]} - {names[r]}')

# from decimal import Decimal as D
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'.split()
# a = [D(num) for num in s]
# print(sum(a))
# print(*sorted(a,reverse=True)[:5])
# from fractions import Fraction
# n = 3
# nf = Fraction(1,2)
# total = 0
# for i in range(1,(n*n)+1):
#     total += Fraction(1,i**n)
#     print(total)

# a1 = 3
# b1 = 7
# a2 = 1
# b2 = 5
# # put your python code here
# if a1 > a2:
#     a1, a2 = a2, a1
#     b1, b2 = b2, b1
#
# if b1 < a2:    print("пустое множество")
# elif b1 == a2: print(b1)
# else:          print(a2, min(b1, b2))

# m = 7
# n = 1
# for i in range(m,n+1 if m<n else n-1,(1 if m<n else -1)):
#     print(i)
# maxx = 0
# prev_maxx = 0
# for i in range(8):
#     n = int(input())
#     if n > maxx:
#         prev_maxx = maxx
#         maxx = n
#     elif n < maxx and n > prev_maxx:
#         prev_maxx = n
# print(maxx,prev_maxx,sep='\n')

# a = [(n:=int(input()))  for _ in range(10)]
# flag = 0
# for i in a:
#     if i%2 ==0:
#         flag += 1
# print('YES' if flag==10 else 'NO')
#
# n = 5
# f1 = 0
# f2 = 1
# for i in range(n):
#     f1, f2 = f2, f1+f2
#     print(f1,end = ' ')
# count = 0
# while (n:=input()) != 'стоп' and n!= 'хватит'and n!='достаточно':
#     count += 1
# print(count)

# count = 0
# while (n:=int(input())) >= 0 and n <= 5:
#     count += 1 if n == 5 else 0
# print(count)

# n = 100
# monets = [25,10,5,1]
# count = 0
# for m in monets:
#     while m <= n:
#         n = n - m
#         count += 1
# print(count)

# num = 7645897791
# maxx = num % 10
# minn = num % 10
# while num != 0:
#     maxx = max(num % 10, maxx)
#     minn = min(num % 10, minn)
#     num = num // 10
# print(f'Максимальная цифра равна {maxx}',f'Минимальная цифра равна {minn}',sep='\n')

# n = 5678
# nn = n
# summ = 0
# pr = 1
# count = 0
# while n != 0:
#     summ += n % 10
#     pr *= n % 10
#     count += 1
#     n = n // 10
# one = int(nn*(10**(1-count)))
# for i in summ,count,pr,summ/count, one, one + nn%10 :
#     print(i)

# n = 9777
# z = n%10 # Находим последнюю цифру
# flag = 'YES' # Вводим флажок
# while n !=0: # Запускаем цикл
#     if z != n % 10: # Сравниваем последнее число с последним числом каждой интерации
#         flag = 'NO' # Еслм число не равно то флажок переходит в состояние NO
#     n = n//10 # Удаляем лишнее
# print(flag)


# n = 9663
# while n % 10 <= n // 10 % 10:
#     n //= 10
# print('YES' if n < 10 else 'NO')

# n = 111
# max_digit = -1
# c = 0
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#        if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# Цифровой корень
# n = 192
# while n > 9:
#     summ = 0
#     while n > 0:
#         summ += n % 10
#         n //= 10
#     n = summ
# print(n)
# Сумма факториалов
# n = 10
# pr = 1
# summ = 0
# for i in range(1,n+1):
#     pr *=i
#     summ += pr
# print(summ)

# a = 2
# b = 15
# for i in range(a,b+1):
#     c = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             c += 1
#     if c == 2:
#         print(i)


# s = 'fffffffffffffff'
# print(s.find('f'))
# print(s.rfind('f'))
# p_in = s.find('f') if s.find('f')>=0 else 'NO'
# l_in = s.rfind('f') if s.find('f')>=0 else 'NO'
#
# print(*[p_in] if p_in == l_in else [p_in,l_in])

# from string import ascii_lowercase
# key = 14
# s = 'fsfftsfufksttskskt'
# res = ''
# for i in s:
#     res += ascii_lowercase[(ascii_lowercase.index(i) - key) % len(ascii_lowercase)]
# print(res)

# from string import ascii_lowercase
# lst = [ ascii_lowercase[i]*(i+1) for i in range(len(ascii_lowercase))]
# print(lst)
# n = 3
# k = 3
# # a = [list(input()) for i in range(n)]
# a = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# print(sum(a,[]))
# b = []
#
# for i in a:
#     b.extend(list(i))
#
# print(b)

# s = 'Python'
# for i,v in enumerate(s):
#     if i % 3 !=0:
#         print(v,end='')

# s = 'foooooooooooooof'
# # s = 'python'
# # s = 'father'
# print(s.find('f', s.find('f')+1))
#
# s = input()
# count = s.count('f')
# if s.count('f') >= 2:     print(s.find('f', s.find('f') + 1))
# elif s.count('f') == 1:   print(-1)
# elif s.count('f') ==0:    print(-2)
# **************************************
# n = 5
#
# # a = [input().lower() for i in range(n)]
# a = ['язык python прекрасен', 'c# - отличный язык программирования', 'stepik - отличная платформа', 'beegeek forever!', 'язык python появился 20 февраля 1991']
#
# m =3
# # aget = [input() for i in range(m)]
# aget = ['язык', 'python', 'прекрасен']
#
# flag = True
# for elem in a:
#     for it in aget:
#         if it in elem:
#            flag = True
#         else:
#             flag = False
#             break
#     if flag == True:
#         print(elem)

# n = 7
# negatives = []
# zeros = []
# pozitive = []
# for i in range(n):
#     x = int(input())
#     if x < 0:
#         negatives.append(x)
#     elif x == 0:
#         zeros.append(x)
#     elif x > 0:
#         pozitive.append(x)
# print(*negatives,*zeros,*pozitive,sep='\n')
#
# s = '192.168.0.300'.split('.')
# flag = 'ДА'
# for i in s:
#     if int(i) not in range(0, 256):
#         flag = 'НЕТ'
# print(flag)
# a = [1,7,5,7,5,1,2]
# count = 0
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] == a[j]:
#             count += 1
# print(count)

import time
t = time.perf_counter()
count = 0
s1 = 'William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.'.split()
s = s1*10000
for elem in s:
    if elem.lower()  in ['a', 'an', 'the']:
        count += 1
print(f'Общее количество артиклей: {count}')

# seq = s
# res = seq.count("a") + seq.count("an") + seq.count("the")
#
# print(f"Общее количество артиклей: {res}")
print(time.perf_counter() - t) #0.0304169999435544 #0.14960170001722872