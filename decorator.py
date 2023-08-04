# ЗАМЫКАНИЯ
# def counter_add(value):
#     def inner():
#         # nonlocal value
#         return value+5
#     return inner
# k=70
# n=counter_add(k)
# print(n())
import decimal
import dis
import heapq
import itertools
# def counter_add(value):
#     def inner(k):
#
#         return value+k
#     return inner
# k=70
# cnt=counter_add(2)
# print(cnt(k))


# def counter_add(tp):
#     def inner(k):
#         if tp=='list':
#             return k
#         else:
#             return tuple(k)
#     return inner
# tp='lii'
# k=[-5, 6, 8, 11, 0, 111, -456, 3]
#
# cnt=counter_add(tp)
# print(cnt(k))
# *******************************************8
# def create_accumulator(value=0):
#
#     def inner(a):
#         nonlocal value
#         value+=a
#         return value
#
#     return inner
#
# s1=create_accumulator(100)
# print(s1(3))
# print(s1(4))

# def multiply(n):
#     def inner(a):
#         return n*a
#
#     return inner
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5))
# print("Умножение 2 на 15 =", f_2(15))
#***************************************************************
# def dekor(func):
#     def wrapper(width,height):
#         rez=func(width,height)
#         print(f'Площадь прямоугольника: {rez}')
#         return rez
#     return wrapper
#
# def get_sq(width,height):
#     rez=width*height
#     return rez
#
# get_sq=dekor(get_sq)
# get_sq(8,11)
# ************************************************
# def show_menu(func):
#     def wrapper(s):
#         s=func(s)
#         for i,v in enumerate(s,1):
#             print(f'{i}. {v}')
#     return wrapper
# @show_menu
# def get_menu(s):
#     s=s.split()
#     return s
#
# s='Главная Добавить Удалить Выйти'
# get_menu=show_menu(get_menu)
# get_menu(s)
# ********************************************************
# def decor(func):
#     def wrapper(a):
#         return sorted(func(a))
#     return wrapper
#
# def get_list(a):
#     a=[int(i) for i in a]
#     return a
#
# get_list=decor(get_list)
# lst = get_list(input().split())
# print(*lst)
# ******************************************
# def decor(func):
#     def wrapper(key,val):
#         rez1,rez2=func(key,val)
#         d = dict(zip(rez1, rez2))
#         return d
#     return wrapper
#
# def get_dict(key,val):
#     return key.split(),val.split()
#
# get_dict=decor(get_dict)
# d = get_dict(input(),input())
# print(*sorted(d.items()))
# ***********************************************************************
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# def decor(func):
#     def wrapper(st):
#         rez=func(st)
#         for i in rez:
#             rez=rez.replace('---','-')
#         return rez
#     return wrapper
#
# def get_str(st):
#
#     st=st.replace(' ','-')
#     ss=''
#     for i in st:
#         ss = ss + t.get(i, i)
#     return ss
#
# get_str=decor(get_str)
# rez = get_str(input().lower())
# print(rez)

#
# **********************************************************
# def df_decor(start=0):
#     def decor(func):
#         def wrapper(a):
#             rez=func(a)
#             return sum(rez)+start
#         return wrapper
#     return decor
# @df_decor(start=500)
# def get_sum(a):
#     a=[int(i) for i in a]
#     return a
#
# # get_sum=df_decor(start=5)(get_sum)
# a = get_sum(input().split())
# print(a)
#**********************************************************************
# def df_decor(tag='h1'):
#     def decor(func):
#         def wrapper(a):
#             rez=func(a)
#             return f'<{tag}>{rez}</{tag}>'
#         return wrapper
#     return decor
# @df_decor(tag='div')
# def get_str_lower(a):
#     return a.lower()
#
# a = get_str_lower(input())
# print(a)
# ***************************************************
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# def df_decor(chars='!?'):
#     def decor(func):
#         def wrapper(st):
#             rez=func(st)
#             for i in rez:
#                 if i in chars:
#                     rez=rez.replace(i,'-')
#
#             return rez
#         return wrapper
#     return decor
# @df_decor(chars='!?')
# def get_str(st):
#     st=st.replace(' ','-')
#     ss=''
#     for i in st:
#         ss = ss + t.get(i, i)
#     return ss.replace('---','-')
#
# rez = get_str(input().lower())
# print(rez)
# ******************************************************
# from functools import wraps
# def df_decor(start=0):
#     def decor(func):
#         @wraps(func)
#         def wrapper(a):
#             rez=func(a)
#             return sum(rez)+start
#         return wrapper
#     return decor
#
# @df_decor(start=0)
# def get_list(a):
#     '''Функция для формирования списка целых значений'''
#     a = [int(i) for i in a]
#     return a

# a = get_list(input().split())
# print(get_list.__doc__)

# Напишите декоратор text_decor, который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»:
# фраза «Hello» печатается до вызова, фраза «Goodbye!» - после
# def text_decor(func):
#     def wrapper():
#         print('Hello')
#         func()
#         print('Goodbye!')
#     return wrapper
#
# @text_decor
# def simple_func():
#     print('I just simple python func')
#
# simple_func()
#*****************************************************
# Напишите декоратор repeater, который дважды вызывает декорированную функцию
# def repeater(func):
#     def wrapper(*args):
#         func(*args)
#         func(*args)
#     return wrapper
#
# @repeater
# def multiply(num1, num2):
#     print(num1 * num2)
# multiply(2, 7)
# multiply(5, 3)
# ****************************************************
# Напишите декоратор double_it, который возвращает
# удвоенный результат вызова декорированной функции
# def double_it(func):
#     def wrapper(*args):
#         res=func(*args)
#         return 2*res
#     return wrapper
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
# res = multiply(9, 4)
# print(res)
# *********************************************************
# Напишите декоратор add_args, который добавляет к переданным аргументам
# еще два значения: строку begin в начало аргументов, строку end в конец.
# from functools import wraps
# def add_args(func):
#     @wraps(func)
#     def wrapper(*args):
#         args = 'begin', *args, 'end'
#         return  func(*args)
#     return wrapper
#
# @add_args
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
#***********************************************************************
# from functools import wraps
# def validate_args(func):
#     @wraps(func)
#     def wrapper(*args):
#         if len(args)<2:
#             return 'Not enough arguments'
#         if len(args)>2:
#             return 'Too many arguments'
#         if len(args)==2:
#             a, b = args
#             if type(a)!=int or type(b)!=int:
#                 return 'Wrong types'
#             else:
#                 return func(*args)
#     return wrapper
# @validate_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
# # print(add_numbers(4,5))
# assert add_numbers(4, 5) == 9
# assert add_numbers(4) == 'Not enough arguments'
# assert add_numbers() == 'Not enough arguments'
# assert add_numbers('hello') == 'Not enough arguments'
# assert add_numbers(3, 5, 6) == 'Too many arguments'
# assert add_numbers('a', 'b', 'c') == 'Too many arguments'
# assert add_numbers(4.5, 5.1) == 'Wrong types'
# assert add_numbers('hello', 4) == 'Wrong types'
# assert add_numbers(9, 'hello') == 'Wrong types'
# assert add_numbers([1, 3], {}) == 'Wrong types'
# assert add_numbers.__name__ == 'add_numbers'
# assert add_numbers.__doc__.strip() == 'Return sum of x and y'
# print('Good')
#***************************************************************************************
# from functools import wraps
# def memoize(func):
#     cache = {}
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         n = args
#         if n not in cache:
#             cache[n] = func(*args)
#         return cache[n]
#     return wrapper
#
# @memoize
# def fibonacci(n):
#     """
#     Возвращает n-ое число Фибоначчи
#     """
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# assert fibonacci(50) == 12586269025
# assert fibonacci(60) == 1548008755920
# assert fibonacci(70) == 190392490709135
# assert fibonacci(80) == 23416728348467685
# assert fibonacci(90) == 2880067194370816120
# assert fibonacci(100) == 354224848179261915075
# assert fibonacci.__name__ == 'fibonacci'
# assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
# print('Good')
#***********************************************************************************
# import calendar
#
# c = calendar.TextCalendar()
# print(c.formatyear(2023))
# ********************************88888
# import string
# print(string.punctuation)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# ***********************************************
# import random
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# random.seed(1)
# def gen_password(n):
#     while True:
#         password=''
#
#         for i in range(n):
#             indx = random.randint(0, len(chars)-1)
#             password+=chars[indx]
#         yield password
# a=gen_password(10)
# for i in range(5):
#     print(next(a))

#***************************************************************************
# days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']*77
# gen_days=((i,days[i+4]) for i in range(1,len(days)))
# for i in range(10):
#     print(next(gen_days))
# **************************************************
# import random
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# random.seed(1)
# def gen_email(n):
#     while True:
#         email=''
#         for i in range(n):
#             indx = random.randint(0, len(chars)-1)
#             email+=chars[indx]
#         yield email+'@mail.ru'
# a=gen_email(8)
# for i in range(5):
#     print(next(a))

import math
# def isprime(n=2):
#
#     while True:
#         if all((n % i) for i in range(2, int(n ** 0.5) + 1)):
#             yield n
# бесконечный цикл простых чисел
# def get_simple():
#     number = 1
#     while True:
#         number += 1
#         for i in range(2, number // 2 + 1):
#             if number % i == 0:
#                 break
#         else:
#             yield number
#
#
# gen = get_simple()
# for i in range(20):
#     print(next(gen), end=' ')
# # ******************************************************************
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# s='Привет Питон'.lower()
# # s_new=(t.get(i,'-') for i in s)
# # [print(*[i for i in s_new],sep='')]
# ss=map(lambda x:t.get(x,'-'),s)
# print(''.join(ss))
# *******************************************************************
# s='Москва Уфа Вологда Тула Владивосток Хабаровск'.split()
# def cicties(s):
#     for x in s:
#         yield x if len(x)>5 else '-'
# a=cicties(s)
# [print(*[i for i in a],sep=' ')]

# print(*map(lambda x: ('-', x)[len(x) > 5], s))
# ************************************************
# def gen_squares(n):
#     for i in range(1,n+1):
#         yield i*i
#
# for i in gen_squares(5):
#     print(i)
# ****************************************************88
# фибаначчи
# def gen_fibonacci_numbers(n):
#     f1,f2=0,1
#     for i in range(1,n+1):
#         f1,f2=f2,f1+f2
#         yield f1
#
# for i in gen_fibonacci_numbers(5):
#     print(i)

# def my_range_gen(*args):
#     if len(args)==1 or len(args) == 2:
#         if len(args) == 2:
#             start, stop = args
#         else:
#             stop=args[0]
#             start=0
#         while start<stop:
#             yield start
#             start+=1
#     elif len(args)==3:
#         start, stop, step = args
#         if start<stop and stop>0:
#             while start < stop:
#                 yield start
#                 start += step
#         elif start>stop:
#             while start>stop:
#                 yield start
#                 start = start+step
#
# for i in my_range_gen(8, 5, -1):
#     print(i)




# def from_hex_to_rgb(color: str) -> tuple:
#         a=int(color[1:3],16)
#         b=int(color[3:5],16)
#         c=int(color[5:],16)
#         return a,b,c
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in list(map(from_hex_to_rgb, colors)):
#     print(f"Red={red}, Green={green}, Blue={blue}")
#**********************************************************************
# s='T y k P e'.split()
# a=list(map(lambda x:(x.upper(),x.lower()),s))
# print(a)
#
# names = [('Monica', 'Waters'), ('Juan', 'Lee'), ('Donna', 'Walker')]
# names_new=list(map((lambda x:f'{x[0]} {x[1]}'),names))
# print(names_new)
# persons = [    {
#         'birthday': '1983-10-25',
#         'job': 'Field seismologist',
#         'name': 'Andrew Hernandez',
#         'phone': '680-436-8521x3468'
#     },
#     {   'birthday': '1993-10-03',
#         'job': 'Pathologist',
#         'name': 'Paul Harmon',
#         'phone': '602.518.4130'
#     },    {
#         'birthday': '2002-06-11',
#         'job': 'Designer, multimedia',
#         'name': 'Gregory Flores',
#         'phone': '691-498-5303x079'
#     }]
#
# phones=list(map(lambda x:x.get('phone'),persons))
# print(phones)

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# sort_days=filter(lambda x:(len(x)==4 or x[0]=='S') ,days)
# print(*sorted(sort_days),sep='\n')
# *******************************************************
import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
# lst_map=tuple(tuple(map(lambda  x:(x.split('=')[0],x.split('=')[1]),lst_in)))
# lst_filt=filter(lambda x:int(x[1])>500,lst_map)
# [print(*[x[0] for x in lst_filt])]

# a=list(map(int,input().split()))
# ***************************************************************

# rez=map(lambda x:x[0]*x[1],zip(list(map(int,input().split())),list(map(int,input().split()))))
# for i in range(3):
#     print(next(rez),end=' ')

import sys

# считывание списка из входного потока
# lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in=[['1', '2', '3', '4', '5', '6'], ['3', '4', '5', '6']]
# print(lst_in)
# args,j=*lst_in
# print(args)
# rez=zip(*args)
# for i in rez:
#     print(*i)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*zip(iter(x),iter(x),iter(x)))

# employees = ['Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin']
#
# identifiers = [77, 48, 88, 85, 76]
# employees_data={}
# for i,v in enumerate(identifiers):
#
#     employees_data[identifiers[i]]=employees[i]
# print(employees_data)

# def zip_with_function(lists,func):
#     # a=zip(*lists)
#     # return list(map(func(*a),zip(*lists)))
#     return (func(*i) for i in zip(*lists))
#
#
# def get_sum_two_numbers(a: int, b: int) -> int:
#     return a + b
# print(*zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers))

# СОРТИРОВКА КОЛЛЕКЦИЙ
# def get_sort(d):
#     return [v for k, v in sorted(d.items(), reverse=True)]
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# print(get_sort(d))
# a=sorted(map(int,input().split()))
#
#import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
#
# d={int(i.split(':')[1]):i.split(':')[0] for i in lst_in}
# for k,v in sorted(d.items())[:3]:
#     print(v,end=' ')

# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']
# print(lst_in)
# d={i.split('=')[0]:int(i.split('=')[1]) for i in lst_in}
#
# for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True):
#     print(k,end=' ')

# a=['до', 'фа', 'соль', 'до', 'ре', 'фа', 'ля', 'си']
# d={'до':[],'ре':[],'ми':[],'фа':[],'соль':[],'ля':[],'си':[]}
# for i in a:
#     d.get(i,i).append(i)
# val=d.values()
# for i in d.values():
#     if i:
#         print(*i, end=' ')

# d = {'до': 0, 'ре': 1, 'ми': 2, 'фа': 3, 'соль': 4, 'ля': 5, 'си': 6}
# print(*sorted(input().split(), key=lambda x: d[x]))

import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['Номер;Имя;Оценка;Зачет','1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет", '5;Балакирев;1;Нет']
# l=[i.split(';') for i in lst_in]
#
# l=[[int(l[i][j]) if l[i][j].isdigit() else l[i][j] for j in range(len(l[0])) ] for i in range(len(l))]
# print(l)
# t_sorted=tuple([(b,d,c,a) for a,b,c,d in l])
# for i in t_sorted:
#     print(i)
# ******************************************************************88
import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in=['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан", 'Арамис=лейтенант', 'Балакирев=рядовой']
# zv=['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
# lst=[i.split('=') for i in lst_in]
# lst=sorted(lst,key=lambda x:zv.index(x[1]))
# print(lst)

# do=['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# s='до фа соль до ре фа ля си'.split()
# lst=sorted(s,key=lambda x:do.index(x))
# print(lst)
# for i in s:
#     print(do.index(i),end=' ')

# ISISTANCE
# def get_add(a, b):
#     if type(a) in (int,float) and type(b) in (int,float) or type(a) is str and type(b) is str:
#         return a+b
# print(get_add(4.6,True))

# def get_sum(it):
#     # sum=0
#     # for elem in it:
#     #     if type(elem) is int:
#     #         sum+=elem
#     # return sum
#     return  sum([elem for elem in it if type(elem) is int])
# print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))

# def get_even_sum(it):
#     return sum([elem for elem in it if type(elem) is int if elem%2==0])
#
# print(get_even_sum([3,4,6,7,3]))
# def get_list_dig(lst):
#     return list(elem for elem in lst if type(elem) in (int,float))
#
# print(get_list_dig([3,5,3.4,True,'ert']))
#**************************************************
# def count_strings(*args):
#     return len([elem for elem in args if isinstance(elem,str)])
# print(count_strings(1, 2, 'hello', [2, 3, 4], True))

# def find_keys(**kwargs):
    # классический вариант
    # a=[]
    # for elem in kwargs:
    #     if isinstance(kwargs[elem],(list,tuple)):
    #         a.append(elem)
    # return sorted(a,key=lambda x:x.lower())
    # короткий вариант
#     return sorted([elem for elem in kwargs if isinstance(kwargs[elem],(list,tuple))],key=lambda x:x.lower())
# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
# *************************************************
# a='appendix expose ensure salon north'.split()
# b=[1 if  elem.lower().endswith('ought') else 0 for elem in a]
# print(any(b))
# a=list(map(float,input().split()))

# def is_string(lst):
#     return all([1 if isinstance(elem,str) else 0 for elem in lst ])

# a=[3,4,5,3,5,4]
# print('отчислен' if any(map(lambda x:x<3,a)) else 'учится')

import sys
# lst_in = list(map(str.split, sys.stdin.readlines()))

# def is_free(lst):
#
#     return any([1  if '#' in i else 0 for i in lst])
#
#
# lst_in=[['#', 'x', 'o'], ['x', '#', 'x'], ['o', 'o', '#']]
# print(is_free(lst_in))
# a='A , y'.split()
# for i in a:
#     print(f'Simvol code {i} is {ord(i)}.')

# a=58
# f = 0x09
# g =  a ^ 9
# i = a & f
# print(bin(58))
# print(bin(g), g)
# print(bin(i), i)
# *********************************************

# a = list(map(int, input().split()))

# if (n:=int(input())):
#     print(f'Ого! {n}! Куда вам столько? Мы заберем {n-10000}')
# else:
#     print(f'Сумма {n} не превышает лимит, проходите')

# print(f'Ого! {n}! Куда вам столько? Мы заберем {n-10000}' if (n:=int(input()))>10000 else
#       f'Сумма {n} не превышает лимит, проходите')
#
# print('Нашли моржа' if 'walrus' in (s:=input()) else 'Никаких моржей тут нет')

# print('YES' if (s:=input())==(t:=input()[::-1]) else 'NO' )
# n=list(map(int,list(input())))
# a=900
# b=800
# print(*(minimum,maximum) if (minimum:=a) < (maximum:=b) else (maximum,minimum))

# print(experiment:= 'Притягиваются' if input()==input() else 'Отталкиваются')

# s1='Лондоньъ'
# s2='Норильск'.lower()
# s1=s1.rstrip('ьъ') if s1[-1] in 'ьъ' else s1
# print(s1)
# print('Good' if s1[-1]==s2[0] else 'Bad')
# a=6
# ages_mapping = {
#     'Младенец': range(0, 2),
#     'Малыш': range(2, 4),
#     'Ребенок': range(4, 12),
#     'Подросток': range(12, 19),
#     'Взрослый человек': range(19, 65),
#     'Пожилой человек': range(65, 100),
# }
# for key,val in ages_mapping.items():
#   if a in val:
#     print(key)
# a=3.5
# b=0
# d_oper={ '+':a+b,
#          '-':a-b,
#          '*':a*b,
#          '/':a/b if b!=0 else 'No'}
# symb='/'
# # print(a+b if symb=='+'else a*b if symb=='*' else a-b if symb=='-' else a/b if (symb=='/' and b!=0) else 'Неизвестно')
# print(d_oper.get(symb,'Неизвестно'))

# s1='qwertyuio'
# # s2='qwertyuio'
# print('Short' if len(s1)<7 else 'OK' if (len(s1)>7 and s1==input()) else 'Difference')

# k=123
# s='ѩкю[щюлцхZ'
# for c in s:
#     c2 = ord(c)
#     co = c2 ^ k
#     print(chr(co),end='')


# a=str(bin(8))[2:]
# i=1
# while a!='' and i<=len(a):
#     print(a[-i])
#     i+=1

# НАХОЖДЕНИЕ СУММЫ ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА
# n=34
# i=1
# a=[]
# while i*i<=n:
#     if n%i==0:
#         a.append(i)
#         if i!=n//i:
#             a.append(n//i)
#     i+=1
# print(sum(a))

# ЯВЛЯЕТСЯ ЛИ ЧИСЛО ПРОСТЫМ?

# n = int(input())
# i = 1
# count = 0
# while i*i <= n:
#     if n % i == 0:
#         if i == n//i:
#             count += 1
#         else:
#             count += 2
#     i += 1
# print('No' if count != 2 else 'Yes')

# n=10
# i=1
# a=[]
# while i*i<=n:
#     if n%i==0:
#         a.append(i)
#         if i!=n//i:
#             a.append(n//i)
#     i+=1
# print(sum(a))

# НОД ДВУХ ЧИСЕЛ
# медленный
# a=75
# b=120
# r=[]
# while a!=b:
#     if a>b:
#         a=a-b
#         r.append(a)
#     else:
#         b=b-a
#         r.append(b)
# print(min(r))
# print((a*b)/15)

# # быстрый
# a=75
# b=120
# r=a*b
# while b>0:
#     # c=a%b
#     # a=b
#     # b=c
#     a,b=b,a%b
# nod=a
#  print(r/nod)

# a=1
# b=7
# a=a-1
# while a<b:
#     a += 1
#     if a%777==0:
#         break
#     elif a%2==0 or a%3==0:
#         continue
#     print(a)

# n=16
# count=0
# while n!=1:
#     if n%2==0:
#         n=n//2
#         count+=1
#     else:
#         n=3*n+1
#         count+=1
# print(count)
# s='phrase'
# i = 0
# while i < len(s):
#     if s[i] == 'a' or s[i]=='e':
#         print('Ага! Нашлась')
#         break
#     print(s[i])
#     i += 1
# else:
#     print("Распечатали все буквы")

# a=9
# b=15
# for i in range(a,b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#
#     else:
#         print(i)
#
# [print(['FizzBuzz' if i % 15 == 0 else 'Fizz' if i%3==0 else 'Buzz'if i%5==0 else i for i in range(a,b+1) ])]

# ***************************************************
# n=3
# count_m=count_c=0
# for i in range(n):
#     m,c=map(int,input().split())
#     if m>c: count_m+=1
#     if m<c: count_c+=1
# print('Mishka' if count_m>count_c else 'Friendship is magic!^^' if count_m==count_c else 'Chris')
#
# n=3
# for i in range(1,n+1):
#     s=input().lower()
#     if 'рок' in s:print(i,s.index('рок')+1)
# n=5
# a=[]
# for i in range(1,n+1):
#     s=input()
#     if 'соль' not in s: a.append(s)
# print(','.join(a))
# s=input().split()

# n=4
# for i in range(n):
#     print(s[0]+str(len(s[1:-1]))+s[-1] if len(s:=input())>10 else s)

# СКОБОЧНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ
# s='{[]}()'
# count=0
# for elem in s:
#     if elem == ')': count -= 1
#     if count<0:  break
#     if elem=='(': count+=1
#     # print(count)
#
# print('YES' if count==0 else 'NO')

# while '()' in s:
#     print(s)
#     s = s.replace('()', '')
#     print(s)
# print('NO' if s else 'YES')

# import sys
# import random
# random.seed(1)
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in=[['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '8', '6', '7']]
# lst_in = list(zip(*map(str.split, lst_in)))
# random.shuffle(lst_in)
# for row in zip(*lst_in):
#     print(*row)
#     print()
# ****************************************************
# cmd = input()
# match cmd:
#     case 'top'|'Top'|'TOP':
#         print("Команда top")
#     case 'bottom'|'Bottom'|'BOTTOM' :
#         print("Команда bottom")
#     case 'right'| 'Right'| 'RIGHT':
#         print("Команда right")
#     case 'left'|'Left'|'LEFT':
#         print('Команда left')

# def get_data(value):
#     match value:
#         case int() as command if command>0:
#             return command
#         case float() as command if -100<=command<=100:
#             return command
#         case str() as command:
#             return command
#     return None

# t =(int, str, str, float, int)
# book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
# # book=[1, 'Балакирев С.М.', 'Python', 2100.0, 2023]
# match  book:
#     case (_,str(aut), str(tit)) if len(aut)>6 and len(tit)>10:               # 1-й case
#         print('Yes')
#     case(_, str(aut), str(tit), float(pr))if len(aut)>6 and pr>0:  # 3-й case
#         print('Yes')
#     case (_, str(aut),str(tit),int(year), *_) if year>2020: # 3-й case
#         print('Yes')
#     case(_, str(aut), str(tit), float(pr), int(year), *_) if pr>0 and year>2020:  # 3-й case
#         print('Yes')
#     case _:                             # 5-й case
#         print("No")
# def parse_json(data):
#     match data:
#         case {'access':'True','data':[_,{'login':str() as login,'email':str() as email}]}:
#             return (login,email)
#         case {'id': ids, 'data': [_, {'login': login}, _, _]}:
#             return ids, login
#
#     return None
#
# json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
# s='abacabadaba'
# s1='ab'
# k=-1
# a=[]
# while s.find(s1,k)!=-1:
#     if s.find(s1,k) not in a: a.append(s.find(s1,k))
#     k+=1
#
# print(*a if a  else [-1])
# for i in range(len(s)):
#     print(i,s.find(s1,i))
#     if s.find(s1,i)==i:
#         print(i)
# users = {
#     "JohnDoe": {
#         "email": "johndoe@example.com",
#         "phone": "+323456789",
#         "password": "pa$$w0rd"
#     },
#     "JaneSmith": {
#         "email": "janesmith@example.com",
#         "phone": "+987654321",
#         "password": "secret789"}}

#a='Johne'
# b='pa$$w0d'
# if a in users.keys():
#     print("Доступ разрешен" if users[a]["password"] == b else'Доступ запрещен')
# else:
#     print('Нет такого пользователя')

# [print({name: pr for name,pr in zip(map(input().split(',')),map(int,input().split(',')))})]
# a=list(map(int,input().split(',')))
# a=[2, 4, 6]
# b=[1,3,5]
# for i,j in zip(a,b):
#     print(i+j,end=' ')
# [print(*[i+j for i,j in zip(a,b)],sep=', ')]
# [print({name: pr for name,pr in zip(a,b)})]

# names=['Анна', 'Петр', 'Мария', 'Иван', 'Ольга']
# balls=[5, 4, 3, 4, 2]
# d={}
# # for name,ball in zip(names,balls):
# #     if ball>=4:
# #         d[name]=ball
# # print(*d.keys())
# print(*{name: ball for name,ball in zip(names,balls) if ball>=4})

# a=[4,2,2,2,0,3]
# b=[3,1,5,2,0,1]
# [print(*['Победа' if i>j else 'Ничья' if i==j else 'Поражение' for i,j in zip(a,b)])]

# students = {
#     "Alice": {
#         "English": 85
#     },
#     "Bob": {
#         "English": 92 },
#     "Tom": {
#         "English": 92}}
#
#
# additional_scores = {
#     "Alice": {
#         "History": 87,
#         "Geography": 76
#     },
#     "Bob": {
#         "History": 91,
#         "Geography": 83  }}
# for k,v in additional_scores.items():
#     if k in students:
#         students[k].update(v)
# print(students)
# s='The cat sat on the mat'.lower().split()
# d={elem: s.count(elem) for elem in s}
# print(d)
# # print(sorted(d.items(),key=lambda x:x[1],reverse=True)[0][1])
# dd={}
# for elem in s:
#     dd[elem]=dd.get(elem,0)+1
# print(dd)
# a=[5, 3, 5, 4, 2, 4]
# b=set()
# for elem in a:
#     # if elem not in b:
#     #     print('no',end=' ')
#     #     b.add(elem)
#     # else:
#     #     print('yes',end=' ')
#     if elem in b: print('yes',end=' ')
#     if elem not in b:print('no',end=' ');b.add(elem)
#
# [print(['yes' if elem in d else 'no' for elem in a])]
# a=list(map(int,input().split()))
# b=set()
# for elem in a:
#     if elem not in b:
#         print('no',end=' ')
#         b.add(elem)
#     else:
#         print('yes',end=' ')


# a={'John', 'Mary', 'David'}
# b={'Mary','Kate', 'Peter'}
# print(', '.join(sorted(a|b)))

# paper_article=set(input().split(', '))
# # set(input().split(', ')) | paper_article
#
# print(', '.join(sorted(set(input().split(', ')) | paper_article)))
# *****************************************88
# a=[5,8,2,7,8,8,2,4]
# n=82
# for i,v in enumerate(a):
#     if v==n:
#         print(i,end=' ')
# else:
#     print('None')
# i=0
# b=[]
# while i<=len(a)-1:
#     if n==a[i] and i not in b:
#         b.append(i)
#     i+=1
# print(*b if b else [None])
# *************************************
import math
# n=99
# pretend = n**0.5
# print('Квадрат' if abs(int(n**0.5) - n**0.5) < 0.01 else 'Не квадрат')
# # print('Квадрат' if 1  else 'Не квадрат')
# print(pretend%1)

# start,stop=map(int,input().split(','))
# print(start,stop)
# print(', '.join(map(str,range(stop,start-1,-1))) if stop>start else ', '.join(map(str,range(start,stop+1,1))))

# a=input().split()
# a=['Хлеб', 'Молоко', 'Яйца', 'Сахар']
# # com,pr=input().split()
# com='Удалить'
# # com='Добавить'
# pr='Хлеб'
# if (pr in a) and com=='Удалить':
#     a.remove(pr)
#     print(*a)
# elif com=='Добавить':
#     a.append(pr)
#     print(*a)
# elif pr not in a:
#     print('Такого продукта нет в списке')

# a=[1, 2, 3, 4, 5]
# n=2
# i=len(a)-1
# flag=True
# while flag:
#     if n not in a:
#         print('Числа нет!')
#         break
#     if n==a[i]:
#         print(i)
#         flag=False
#         break
#     i-=1
# a='apple, , banana, , cherry, date, , , elderberry'.split(', ')
# print(a, len(a))
# new_a=[]
# i=0
# while i<len(a):
#     if not a[i]:
#         i+=1
#         continue
#     new_a.append(a[i])
#     i += 1
# print(', '.join(new_a))

# n=int(input())
# fact=i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# a=[-9,-8]
# i=1
# maxx=a[0]
# while i<len(a):
#     if a[i]>maxx: maxx=a[i]
#     i+=1
# print(maxx)

# n=123
# i=0
# sum_n=0
# while n!=0:
#     sum_n+=n%10
#     n = n // 10
#     i+=1
# print(sum_n)


# n=8
# i=1
# count=0
# while i*i<=n:
#     if n%i==0:
#         if i==n//i: count+=1
#         else: count+=2
#     i+=1
# print(False if count!=2 else True)
# def func(n):
#     for i in range(2, n):
#         if not n % i: return False
#     return True
# print(func(int(input())))

# a=30
# b=18
# while b>0:
#     a,b=b,a%b
# print(a)

# a=input().split()
# i=0
# flag=True
# summ=counter=0
# while i<len(a):
#     if a[i]=='Неявка': i+=1; continue
#     summ+=int(a[i])
#     counter+=1
#     i+=1
# print(summ/counter if counter else 'Не явился ни на один' )

# summ1=sum(float(input()[12:16])  for i in range(24) )
# print(round(summ1/24,1))

# s='резюме_Иванов.doc фотография_отпуск.jpg Протокол_собрания.pdf' \
#   ' Лето.mp3 договор_аренды.docx фактура_№12345.pdf план_поездки.txt ' \
#   'фото_пейзаж_1.jpeg изображение_портрет.jpg'.split()
# print(s)
# a=[elem for elem in s if elem.endswith('.jpg') or elem.endswith('.jpeg')]
# print(*a if a else ['Картинок нет!'])

# s='У меня в кармане 10 рублей, в сумке 100, а в рюкзаке ещё 15.'.strip(',.!').split()
# print(s)
# s_new=list(int(elem) for elem in s if elem.isdigit())
# print(sum(s_new))

# s='Оборудование - это ТОП-1, что доставляет наша компания'
# sn=''
# for char in s:
#     if char.isalpha() or char.isdigit():
#         sn+=char
#     elif char=='_' or char=='-' or char==' ':
#         sn+=' '
# print(sn.replace('   ',' ').lower())

# s='!!!???!..!'
# sn=''
# glas=['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# count=0
# for i in s:
#     if i in glas:  count+=1
#     if i.isalpha(): sn+=i
# print(round(count/len(sn),1) if sn else 0)

# a=[1, True,True,  3, 4, 4, 5]
# a=input().split(', ')
# b=[]
# for i in a:
#     if i not in b:    b.append(i)
# print(*b,sep=', ')

# a=list(map(int,input().split(', ')))
# a=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
# x=[1]
# [print(*[v for i,v in enumerate(a) if i not in x])]

# a=list(map(int,input().split(', ')))
# profit=[100, 50, 200, 0, 300, 400, 500, 100, 200, 600, 700, 150]
# print(profit)
# defis=[i+1 for i,v in enumerate(profit) if v<0]
# print(*defis if defis else ['Убыточных месяцев не было'],sep=', ')
# m=4
# for i in range(1,m+1):
#     for j in range(1,m+1):
#         print(f'{i*j:>2}',end=' ')
#     print()

# a=input().split(', ')

# a=['Любознательная', 'Решительная', 'МудраяКобра']
# b=[ 'Горилла', 'Лама', 'Щука']
# c=[]
# for i in a:
#     for j in b:
#         c.append(f'{i} {j}')
# print(sorted(c))
#
# rezult=[f'{i} {j}' for j in b for i in a]
# print(rezult)

# a=['Багдасарян', 'Кобаяши', 'Давиденко', 'Лопес', 'Смирнов']
# rez=[]
# print(*sorted([f'{a[i]} {a[j]}' for i in range(len(a)) for j in range(i+1,len(a))]),sep='\n')

# a=map(int,input().split(', '))
# print(a)
# # a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n=12
# rez=[]
# for i,v in enumerate(a):
#     for j,k in enumerate(a):
#         if v+k==n and v!=k and (k,v) not in rez:
#             rez.append((v,k))
# if rez:
#     for i in rez:
#         print(*i,sep=', ',end='\n')
# else:    print('Такую сумму получить нельзя!')

# n=2
# m=3
# a=[[1,2,3],[4,5,6]]
#
# summ=0
# for i in a:
#     for j in range(m):
#         summ+=a[i][j]
# print(summ)
# **************************************************************
# сапеnр
# n=4
# m=5

# Чтение игрового поля
# field = [input().split() for _ in range(n)]
# field=[['0', '0', '0', '1', 'x', '?', '?', '?', '?'],
#        ['1', '1', '0', '1', '2', '?', '?', '?', '?'],
#        ['x', '1', '0', '0', '1', '*', '?', '*', '*'],
#        ['?', '2', '1', '1', '1', '1', '3', '*', '?'],
#        ['?', '?', 'x', '1', '0', '0', '1', '1', '?'],
#        ['?', '*', '2', '1', '0', '0', '0', '1', '?'],
#        ['1', '1', '1', '0', '0', '0', '0', '1', '*'],
#        ['0', '0', '0', '0', '1', '1', '1', '1', '?'],
#        ['0', '0', '0', '0', '1', 'x', '?', '?', '?']]
# field=[['0', '?', '?', '?', '0'],
#        ['1', '?', '?', '3', '0'],
#        ['0', '2', '?', '?', '1'],
#        ['0', '?', '?', '?', '1']]
# #
# # Переменные для отслеживания состояния игры
# has_mine = False
# has_closed_cells = False
# has_go=False
# for row in field:
#     for elem in row:
#         if elem =='*':
#             has_mine = True
#             break
#         elif elem=='?' or elem=='x':
#             has_go = True
#     if has_mine:
#         break
# if has_mine:
#     print('Проигрыш')
# elif has_go:
#     print('Игра идет')
# else :
#     print('Выигрыш')



# n=3
# m=3
# a=[[1.0, 2.0, 3.0],
#     [4.0, 5.0, 6.0],
#     [7.0, 8.0, 9.0]]
# b=[]
# for i in range(m):
#     c=[]
#     for j in range(n-1,-1,-1):
#         c.append(a[j][i])
#     b.append(c)
# for i in b:
#     print(*i)
# ***************************************88
#  **********************************************************************
# n=3
# m=3
# a = [(list(map(float,input().split()))) for _ in range(n)]
# print(a)
# b=[[a[j][i] for j in range(n-1,-1,-1)] for i in range(n)]
# for i in b:
#     print(*i)

# n, m = map(int, input().split())
# a = []
#
# for _ in range(n):
#     row = list(map(float, input().split()))
#     a.append(row)
#
# b=[]
# for i in range(m):
#     c=[]
#     for j in range(n-1,-1,-1):
#         c.append(a[j][i])
#     b.append(c)
# for i in b:
#     print(*i)

# n=23
#
# if n in range(6, 11):  print('Доброе утро!')
# elif n in range(12, 17): print('Добрый день!')
# elif n in range(18, 22): print('Добрый вечер!')
# elif n not in range(-1,24): print('Некорректное время')
# else: print('Доброй ночи!')
# a=list(map(int,input().split()))
# n=int(input())
# i=0
# if n not in a: print(*a)
# else:
#     while n!=a[i]:
#         print(a[i],end=' ')
#         i+=1

# n=5
# k=0
# for i in range(1,n+1):
#     if i%2!=0:
#         for j in range(1,n+1-k):
#             print(j,end=' ')
#     else:
#         for j in range(n, k, -1):
#             print(j, end=' ')
#     k+=1
#     print()

# n = 1331
# k=n
# reversed_n = n % 10
#
# while (n := n // 10) > 0:
#     reversed_n = reversed_n* 10 + n% 10
#     # reversed_n += n % 10
# print(reversed_n==k)
# print(reversed_n)
# n=119
# m=19
# c=30
# print((((m*60+n+c))//60)%24, (n+c)%60)
# ******************************************************
# ШИФР ЦЕЗАРЯ
# s='def'
# key=3
# for i in s:
#     if chr(ord(i) - key).isalpha():
#         print(chr(ord(i)-key), sep='', end='')
#     else:
#         print(chr(ord(i) - key + 26), sep='', end='')

# s='aabccccdddddd'
#
# def r2(s):
#     prevsymb, count, maxx, symb = '', 1, 0, ''
#     for i in s:
#         if i == prevsymb:
#             count += 1
#         else:
#             count = 1
#         if maxx <= count:
#             maxx = count
#             symb = i
#         prevsymb = i
#     return symb, maxx
#
# def r1(s):
#     count=1
#     maxx=1
#     symb=''
#     prevsymb = ''
#     for i in s:
#         # print('befor' ,prevsymb, s[i], maxx, count, symb)
#         if prevsymb:
#             if i==prevsymb:
#                 count+=1
#                 if maxx<=count:
#                     maxx=count
#                     symb = i
#             else:
#                 count = 1
#                 if maxx==count:
#                     symb = i
#         else:
#             symb = i
#         prevsymb = i
#         # print('after', prevsymb, s[i], maxx, count, symb)
#     return (symb, maxx)
#
# tests = {
#     'abcd' : ('d', 1),
#     'aabcd' : ('a', 2),
#     'aabbcd': ('b', 2),
#     'aabbccdd': ('d', 2),
#     'aaabcddd': ('d', 3)
# }
# for k, v in tests.items():
#     res = r1(k)
#     print( k, v, '=>', res, 'OK' if res == v else '')
# print ('*'*20)
# for k, v in tests.items():
#     res = r2(k)
#     print( k, v, '=>', res, 'OK' if res == v else '')

# s='aaabbccccaaaab'
# def myf(s):
#     count=1
#     maxx=0
#     symb=''
#     for i in range(1,len(s)):
#         if s[i-1]==s[i]:
#             count+=1
#             maxx=count
#             symb = s[i-1]
#         else:
#             if maxx<=count:
#                 maxx=count
#                 symb=s[i-1]
#             count=1
#     if maxx<=count:
#         maxx=count
#         symb=s[i]
#     return symb,maxx
# t={'aaabbccccaaaab':('a',4),
#    'abcd':('d',1),
#    'aabcd':('d',1),
#    'abbcd':('b',2),
#    'abcdd':('d',2)}
# for i,v in t.items():
#     print(f'{i},{v} => {myf(i)}')
# айдите в ней подстроку, где наибольшее количество подряд идущих одинаковых символов.
# Выведите символ и длину последовательности.
# Если таких несколько – выведите последнюю.
# s='abcd'
# data = ''
#
# for c in s:
#     print(f'data={data}, c = {c}')
#     if data and data[-1] != c:
#         data += ' '
#     data += c
#     print('data=',data)
#
# result = sorted(data.split(), key=len)[-1]
# print(data.split())
# print(result)
# print(result[0], len(result), sep='\n')
# from itertools import groupby
# s='aaabbccccaaab'
# a=[]
# for i,v in groupby(s):
#     a.append(list(v))
#
# print(a)
# q=''
# n=0
# for i in a:
#    if len(i)>=n:
#        q=i[0]
#        n=len(i)
# print(q,n)
# ************************************************
# моя рабочая программа по поиску подряд идуш послед max
# s='aabbbcccdddddd'
# s1=s[0]
# new_s=''
# for char in s:
#     if char==s1:
#         new_s+=char
#         # print('new_s=',new_s)
#     else:
#         s1=char
#         new_s+=' '+char
#         # print('s1=',s1)
# print(new_s)
# a=[(i[0],len(i)) for i in new_s.split()]
# print(a)
# print(*sorted(a,key=lambda x:x[1])[-1],sep='\n')
#**************************************************8
# def r1(s):
#     count=1
#     maxx=1
#     symb=''
#     prevsymb = ''
#     for i in range(0,len(s)):
#         # print('befor' ,prevsymb, s[i], maxx, count, symb)
#         if prevsymb:
#             if s[i]==prevsymb:
#                 count+=1
#                 if maxx<=count:
#                     maxx=count
#                     symb = prevsymb
#             else:
#                 count = 1
#                 if maxx==count:
#                     symb = s[i]
#         else:
#             maxx = 1
#             symb = s[i]
#         prevsymb = s[i]
#         # print('after', prevsymb, s[i], maxx, count, symb)
#     return (symb, maxx)
#
# s=input()
# print(*r1(s),sep='\n')
# ******************************************************************
# превратить строку 'aabbbcccdddddd' в 'a2b2c3d6'
# s='aabbbcccdddddd'
# s1=s[0]
# new_s=''
# count=1
# for char in s:
#     if char==s1:
#         new_s+=char
#         count+=1
#         # print('new_s=',new_s)
#     else:
#         s1=char
#         new_s+=' '+char+str(count)
#         # print('s1=',s1)
# print(new_s)
# a=[(i[0],len(i)) for i in new_s.split()]
# print(a)
# print(*sorted(a,key=lambda x:x[1])[-1],sep='\n')
# *********************************************************************8888888
# a=[1,2,3,4,5,4,2,3,4,5]
# b=[a[i-1]+a[i] for i in range(1,len(a))]
# c=list(map(lambda x:x[0]+x[1],enumerate(a,start=0)))
# print(b)
# print(c)
from itertools import groupby
# a=[2,3,4,4,2,3,84,5]
# # print(sorted(set(a))[-2])
# maxx1=max(a)
# maxx2=a[0]
# for i in a:
#     if i<maxx1 and i!=maxx1:
#         maxx2=max(maxx2,i)
# print(maxx2)
# Отсортируйте массив так, чтобы все нули в нем оказались в
# конце массива, сохранив при этом порядок чисел.
# a=[10, 0, 3, 0, 4, 0, 0, 5, 6, 7, 8]
# # b=[i for i in a if i!=0]
# # s=[0 for _ in range(len(a)-len(b))]
# # print(*b+s)
# i=0
# k=0
# while i<len(a):
#      if a[i]!=0:
#         a[k],a[i]=a[i],a[k]
#         k+=1
#     i+=1
# print(a)

# Удалите из массива все элементы, значения которых являются нечетными.
# a=[1, 2, 3, 4, 5]
# b=[i for i in a if i%2==0]
# print(*b)

# print(*filter(lambda x:x%2==0,a))
# *******************************************************
# Найдите медиану этого списка. (медиана это значение по центру в отсортированном списке,
# причем если длина четная то возьмите среднее арифметическое двух значений)
# b=sorted([int(i) for i in input().split()])
# b=[2,3,6]
# print(b)
# summ_b=(b[len(b)//2]+b[len(b)//2-1])
# mediana=summ_b//2 if summ_b%2==0 else summ_b/2
# print(mediana.is_integer())
# print(sorted(b)[(len(b)//2)] if len(b)%2!=0 else mediana)
# ********************************************************************

# a= set()
# while n:=int(input()):
#     a.add(n)
# print(len(a)+1)
# a=['a','b','c','a']
# # a = [i for i in input().split()]
# key=set(a)
# d=dict.fromkeys(key,0)
# for key in a:
#     d[key]+=1
# for i,v in d.items():
#     print(i,v)
# # d={i:a.count(i) for i in a}
# ********************************************
# DICT
# # a=[i.split() for i in iter(input, 'end')]
# a=[['/api/admin', '200'], ['/api/admin', '400'], ['/cities', '200'],
#    ['/users/create', '201'], ['/users/1/delete', '204'], ['/users/2/delete', '204'],
#    ['/users/2/delete', '404']]
# from collections import defaultdict
#
# d_code=defaultdict(int)
# d_http=defaultdict(int)
# for i in a:
#     d_code[i[1]]+=1
#     d_http[i[0]]+=1
# for i in sorted(d_code.items())+sorted(d_http.items()):
#     print(*i)
#
# from collections import Counter
# z=['a','x','a','b','x']
# d=Counter(z)
# print(d)
# ***********************************************************
# a=[i for i in iter(input,'close')]
# a=['add 5', 'add 10', 'head', 'pop', 'add 7', 'add 9', 'pop', 'pop', 'head']
# print(a)
# stek=[]
# for i in a:
#     # print(int(i.split()[1]))
#     if i.split()[0]=='add': stek.append(int(i.split()[1]))
#     elif i.split()[0]=='head': print(stek[-1])
#     elif i.split()[0]=='pop': stek.pop()
#
# print(stek)
# stek=[]
# while (i := input()) != "close":
#     if i.split()[0] == 'add':
#         stek.append(int(i.split()[1]))
#     elif i.split()[0]=='head':
#         print(stek[-1])
#     elif i.split()[0]=='pop':
#         stek.pop()
# print(stek)
# **********************************************************

# number = 0
# while True:
#     s=input().split()
#     a=s[0]
#     b=s[-1]
#     match a:
#         case "add":    number=number+int(b)
#         case "mul":    number=number*int(b)
#         case 'minus':  number = number - int(b)
#         case "div":    number = number // int(b)
#         case "zero":   number = 0
#     match b:
#         case 'result': print(number)
#         case 'exit':   exit()
#     if a=='exit':      break
# print(number)
# *************************************************8
# command=input()
# match command:
#     case "Flask"|'Django'| 'Fast-API' as framework :
#         print(f'Python({framework}),Backend-dev')
#     case "Angular"|'React'|'Vue'as framework:
#         print(f'JavaScript/TypeScript({framework}),Frontend-dev')
#     case 'Flutter'|'React Native'as framework :
#         print(f'JavaScript({framework}),Cross-Mobile-dev')
#     case 'Pandas'|'skit-learn'|'keras 'as framework:
#         print(f'Python({framework}),Data-Scientist')
#     case _:
#         print(f'модель еще не обучена')

# def true_ip(ip_address):
#     arr = ip_address.split('.')
#     for i in arr:
#         if int(i) > 255 or int(i) < 0:
#             return False
#     if arr == ['0', '0', '0', '0'] or arr == ['255', '255', '255', '255']:
#         return False
#     return True
#
# s='255.255.255.255'
# print(true_ip(s))
# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# *************************************************************
# import json
# d = json.loads(input())
# d=[{'id': 1, 'parents': [1, 2, 3, 4], 'chief': {'name': 'Paul', 'age': 50},
#     'age': 100}, {'id': 1, 'parents': [1, 2, 3, 4], 'chief': {'name': 'Paul', 'age': 62},
#     'age': 80}]
# rez=0
# for i in d:
#     for k,v in i.items():
#         if max(i['age'],i['chief']['age']) > rez:
#             rez=max(i['age'],i['chief']['age'])
# print(rez)
# **********************************************************************
# НУЖНО ДОДЕЛАТТЬ, НЕ ЗНАЮ КАК
from itertools import groupby
# d={}
#
# for i in range(5):
#     s=input().split()
#     d.setdefault(s[1],[]).append(s[0])

# d= {'Россия': ['Краснодар', 'Москва'],
#    'Нидерланды': ['Амстердам'],
#    'США': ['Вашингтон', 'Нью-Йорк']}
# a=[]
# for k,v in sorted(d.items()):
#     g = []
#     for j in v:
#         g.append(k+' '+j)
#     a.append('\n'.join(sorted(g)))
# print('\n<->\n'.join( a))

# n = int(input())
# d = {}
# for i in range(n):
#     s = input().split()
#     d.setdefault(s[1],[]).append(s[0])
# a=[]
# for k,v in sorted(d.items()):
#     g = []
#     for j in v:
#         g.append(k+' '+j)
#     a.append('\n'.join(sorted(g)))
# print('\n<->\n'.join( a))

# d={'Краснодар': 'Россия',
#    'Амстердам': 'Нидерланды',
#    'Москва': 'Россия',
#    'Вашингтон': 'США',
#    'Нью-Йорк': 'США'}
# for k,v in sorted(d.items(),key=lambda x:x[1]):
#     print(v,k)


# print('\n<->\n'.join( a))




# *****************************************************************
# s='aabbccdddd'
# group_s=itertools.groupby(s)
# for i,v in group_s:
#     print(f'Ключ : {i}')
#     for j in v:
#         print(j,end=' ')
#     print()
#********************************************************
# Сначала вашей программе на вход поступает поток чисел.
# Сохраните их в массиве в отсортированном виде. После ключевого слова "change"
# меняется состояние программы, и на каждое введенное число она должна выдавать
# индекс элемента, на котором находится данное число (правый). Программа завершается,
# когда встречает слово "close".

# a=sorted([int(i) for i in iter(input,'change')])
# for i in iter(input,'close'):
#     all_occur = [j for j, elem in enumerate(a) if elem == int(i)]
#     print(all_occur[-1],sep='\n')

# ****************************************************
# ПОИСК ИНДЕКСОВ - ВХОЖДЕНИЙ
# my_list = [2,2,2,3,5,10]
# all_occur = [i for i, elem in enumerate(my_list) if elem == 2]
# print(all_occur[-1])
# *****************************************************

# ***************************************************
# Вам на вход поступает две даты в формате ISO 8601.
# Поменяйте в них местами годы если это возможно.
# from datetime import date
# # s1=input()
# # s2=input()
# d1 = date.fromisoformat('2020-02-29')
# d2 = date.fromisoformat('2021-12-12')
# try:
#     dd1 = date(year=d1.year,month=d2.month,day=d2.day)
#     dd2 = date(year=d2.year,month=d1.month,day=d1.day)
#     print(dd2, dd1, sep='\n')
# except:
#     ValueError: print('Год изменить невозможно')
#***********************************************************
# print(d1.weekday())
import calendar
# print(calendar.calendar(2023))
# print(calendar.monthcalendar(year=2023,month=4))
# print(calendar.monthrange(year=2023,month=7))
# *************************************************************
from datetime import date; import calendar

# from datetime import datetime,timedelta,time
# t1=time.fromisoformat('12:00:00')
# t2=time.fromisoformat('15:00:00')
# # tt1=time.isoformat('12:00:00')
#
# # t1=time.fromisoformat('12:00:00')
# # t2=time.fromisoformat('15:00:00')
# ttr1=timedelta(hours=t1.hour,minutes=t1.minute,seconds=t1.second)
# ttr2=timedelta(hours=t2.hour,minutes=t1.minute,seconds=t1.second)
# # tt2=timedelta(hours=t2.hour,minutes=t2.minute,seconds=t2.second)
# rez=(ttr2-ttr1)
# print(ttr2-ttr1)


# g1=2024
# g2=2020
#
# print()
# d1= datetime(year=2020,month=1,day=1)
# d2= datetime(year=2024,month=1,day=1)
# print((d2-d1).days)


# start_date=date.fromisoformat('2022-08-01')
# end_date=date.fromisoformat('2023-08-01')
# if start_date.month == end_date.month:
#     print(start_date.day-end_date.day+1)
# else:
#     print(calendar.monthrange(start_date.year,start_date.month)[1]-start_date.day+1)
# print(calendar.calendar(2022))

# from datetime import date; import calendar
# start_date = date.fromisoformat(input())
# end_date = date.fromisoformat(input())
# d1 = date(year=start_date.year,month=start_date.month,day=start_date.day)
# d2 = date(year=end_date.year,month=end_date.month,day=end_date.day)
# if d1.month == d2.month and d1.year==d2.year:
#     print(d2.day-d1.day+1)
# else:
#     month = calendar.monthrange(d1.year,d1.month)[1]
#     print(month-d1.day+1)
#***********************************************************
# a=[]
# while True:
#     n= input().split()
#     if n[0]=='add':
#         a.append(int(n[1]))
#     elif n[0]=='pop':
#         print(a.pop())
#     elif n[0]=='head':
#         print(a[-1])
#     elif n[0]=='close':
#         break

# a=[]
# while (s:=input()) != 'close':
#     match s.split():
#         case "add", n :    a.append(int(n))
#         case "pop" ,  :     print(a.pop())
#         case 'head',  :     print(a[-1])
# *************************************************
# from collections import deque
# queue=deque()
# while (s:=input()) != 'close':
#     match s.split():
#         case "add", n :     queue.appendleft(int(n))
#         case "pop" ,  :     print(queue.pop())
#         case 'head',  :     print(queue[-1])
# *************************************************
# Дан список чисел, записанных через пробел.
# Реализуйте кучу с максимумом в вершине для этого списка.
# import heapq
# from heapq import heappush,heappop
#
# hh = list(map(int,input().split()))
# heap = list(map(lambda x: -x, hh))
# heap = [-int(i) for i in input().split()]
#
# heapq.heapify(heap)
# while (s:=input()) != 'end':
#     match s.split():
#         case "insert", n :  heappush(heap, -int(n))
#         case "pop" ,     :  print(abs(heappop(heap)))
#********************************************************
# import heapq
# from heapq import heappush,heappop
# pq=[]
# heapq.heapify(pq)
# while (s:=input().replace(',',' ')) != 'end':
#
#     match s.split():
#         case "task", task,priority  :
#             heappush(pq, (-int(priority), -int(task)))
#         case "take", :
#             elem = heappop(pq)
#             print(f'Задача {abs(elem[1])} с приоритетом {abs(elem[0])}')




# pq=[('1',6), ('101',5), ('10',3), ('10',5), ('2',2)]
# heapq.heapify(pq)
# print(heappop(pq))
# print(heappop(pq))
# print(f'Задача {abs(heappop(pq)[1])} с приоритетом {abs(heappop(pq)[0])}')

# s='task 101,5'.replace(',',' ')
# task, *priority = s.split()
# heappush(pq,(priority[0],priority[1]))
# s='task 10,5'.replace(',',' ')
# task, *priority = s.split()
# heappush(pq,(priority[0],priority[1]))
# print(pq)
# print(f'Задача {heappop(pq)[0]} с приоритетом {heappop(pq)[1]}')







# ********************************************
# import heapq
# from heapq import heappush,heappop
# heap = []
# heapq.heapify(heap)
#
# heappush(heap,(2,0))
# heappush(heap,(1,15))
# heappush(heap,(1,10))
# heappush(heap,(1,7))
# heappush(heap,(0,20))
# heappush(heap,(0,10))
# heappush(heap,(0,12))
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))

# n=9
# d={}
# for i in range(n):
#     s = input().split()
#     d.setdefault(s[0],[]).append(int(s[1]))
# # d={'Демин': [2, 2, 2],
# #    'Сергеев': [4],
# #    'Золотов': [3, 4],
# #    'Иванов': [3],
# #    'Петров': [2],
# #    'Сидоров': [3]}
# print(d)
# for i,v in d.items():
#     print(i, sum(v)/len(v))
# ******************************************************
# n=4
# d={}
# a=[]
# # for i in range(n):
# #     s = input().replace(',',' ').replace('.',' ').replace(';',' ').lower().split()
# #     a.append(s)
# a=[['she', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shore'],
#    ['the', 'shells', 'that', 'she', 'sells', 'are', 'sea', 'shells', "i'm", 'sure'],
#    ['so', 'if', 'she', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shore'],
#    ["i'm", 'sure', 'that', 'the', 'shells', 'are', 'seaside', 'shore', 'shells']]
# print(a)
# for row in a:
#     for elem in row:
#         d[elem]=d.get(elem,0)+1
# print(*sorted(d.items(),key=lambda x: (-x[1],x[0]))[0])
#


# n=int(input())
# d={}
# a=[]
# for i in range(n):
#     s = input().replace(',',' ').replace('.',' ').replace(';',' ').lower().split()
#     a.append(s)
# for row in a:
#     for elem in row:
#         if elem not in d:
#             d[elem]=1
#         else:
#             d[elem]+=1
# print(*sorted(d.items(),key=lambda x: (-x[1],x[0]))[0])
# ******************************************************
# a=input()
# match a:
#     case 'int':
#         b = int(input())
#         c = int(input())
#         print('Empty Ints' if b==c==0 else b+c)
#     case 'str':
#         st = input()
#         print('Empty String' if st=='' else st)
#     case 'list':
#         lst = input().split()
#         print('Empty List' if len(lst)==0 else lst[-1])
#     case _:
#         print('Unknown type')
# summ=0
# while (n:= input())!='The End':
#     summ += int(n)
# print(summ)

# САМЫЙ МАЛЕНЬКИЙ НОД ЧИСЛА
# n=2589
# i=2
# a=[]
# while i<=n//2:
#     if n%i==0:
#         a.append(i)
#     i+=1
# print(min(a))

# def translate(n,base=2):
#     a = []
#     while n!=0:
#         d,m = divmod(n,base)
#         a.append(m)
#         n=d
#     return ''.join(list(map(str,a))[::-1])
# n=19
# print(translate(n,7))
# ************************
# ФАКТОРИАЛ И СУПЕРФАКТОРИАЛ
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return factorial(n-1)*n
#
# print(factorial(5))
#
# def sf(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return sf(n-1)*factorial(n)
# print(sf(4))
# def convert(L):
#     return list(map(int,L))
# def maxId(L):
#     maxx=max(convert(L))
#     return convert(L).index(maxx)
#
# l=[1, 2, '42', '3', '4', '5', 6, 13]
# print(maxId(l))
# def convert(L):
#     return list(map(int,L))
# with open('d1.txt') as file:
#     summ=0
#     line=file.read().split()
#     print(sum(convert(line)))


# простое число
# n = int(input())
# i = 1
# count = 0
# while i*i <= n:
#     if n % i == 0:
#         if i == n//i:
#             count += 1
#         else:
#             count += 2
#     i += 1
# print('No' if count != 2 else 'Yes')

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# a = ['mix', 'extra', 'x-files', 'xyz', 'xapple', 'apple']
# print(sorted(a, key=lambda x: (x[0] != 'x', x)))
# **************************************************888
# ФИБАНАЧЧИ
# def gen_fibonacci_numbers(n):
#     f1,f2=0,1
#     for i in range(1,n+1):
#         f1,f2=f2,f1+f2
#     return f1
# print(gen_fibonacci_numbers(9))

# *****************************************************************************88
# def luka(L0, L1, n):
#      for i in range(n):
#         L0, L1 = L1, L0 + L1
#         return L0
#
#
#
# from decimal import Decimal,getcontext
# getcontext().prec = 50
# def luka(n):
#     L0 = 2
#     L1 = 1
#     def mygen(n):
#         L0 = 2
#         L1 = 1
#         for i in range(n - 1):
#             L0, L1 = L1, L0 + L1
#             yield L1
#     lu = mygen(n)
#     last = L0
#     for i in lu:
#         last = i
#     return last
#
# print(luka(180))

# def luka(L0, L1, n):
#     def mygen(L0, L1, n):
#         for i in range(n - 1):
#             L0, L1 = L1, L0 + L1
#             yield L1
#     lu = mygen(L0,L1,n)
#     prev = last = L0
#     for i in lu:
#         prev = last
#         last = i
#     return last
#
# print(luka(2, 1, 180))
 # фибаначчи
# def gen_fibonacci_numbers(n):
#     f1,f2=0,1
#     for i in range(1,n+1):
#         f1,f2=f2,f1+f2
#         yield f1
#
# for i in gen_fibonacci_numbers(5):
#     print(i, end = ' ')
# **************************************


# print(kaprekar(n))




# ПЕРЕВОД ЧИСЛА В ЛЮБУЮ СИСТЕМУ СЧИСЛЕНИЯ
# def convert(n,to_base=10,from_base=10):
#     alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     num10 = int(n, from_base) if from_base!=10 else n
#     a = []
#     while num10:
#         num10, m = divmod(num10, to_base)
#         a.append(alphabet[m])
#     return ''.join(a[::-1])
#
# n = 42
# print(convert(n))
 # **********************************

 class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __init__(self):
#         print(' вызов init')
#         self.x = 0
#         self.y = 0
#     def get_coors(self):
#         return (self.x, self.y)
#
# Point.color = 'black'
# pt = Point()
# pt.set_coords(10,20)
# Point.type = 'dict'
#
# pt2 = Point()
# pt2.set_coords(100,300)
# print(pt.get_coors())
# print(pt2.get_coors())
# print(type(pt))

