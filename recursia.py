# из многомерного списка сделать список
# def get_line_list (d,a=[]):   # объявляем функцию, которая принимает список и пустой список
#     for i in d:               # проходимся по заданному списку
#         if type(i) != list:   # если тип элемента не список
#             a.append(i)       # добавляем его в пустой список
#         elif type(i) == list: # если это список
#             get_line_list(i)  # то вызываем функцию передавая этот список
#     return a
# # d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# d = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
# print(get_line_list(d))

# def list_pull(L):
#   res = []
#   for elem in L:
#     res += list_pull(elem) if isinstance(elem, list) else [elem]
#   return res
# *****************************************************
# вычислить сумму списка
# def get_rec_sum(a):
#     return a[0] if len(a)==1 else a.pop()+ get_rec_sum(a)
#
# a=list(map(int,input().split()))
# print(get_rec_sum(a))
# *****************************************************
# сформировать последовательность чисел Фибоначчи по правилу:
# первые два числа равны 1 и 1, а каждое следующе значение равно
# сумме двух предыдущих. Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ..
# N = int(input())
# def fib_rec(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# data = list(fib_rec(N))
# ****************************************************************
# Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n.
# n = int(input())
# def fact_rec(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fact_rec(n-1)*n
# ************************************************************************
# Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два.
# get_path(N) = get_path(N-1) + get_path(N-2)
# def get_path(n):
#     if n == 1: return 1
#     elif n == 2: return 2
#     else:
#         return get_path(n-1) + get_path(n-2)
#
# n = int(input())
# print(get_path(n))
# *********************************************************
#  Скопировать многомерный список без deepcopy
# def list_deepcopy(l):
#     return [elem if not isinstance(elem, list) else list_deepcopy(elem) for elem in l]
#
# s = []
# out = [42,73, s]
# copy_l = list_deepcopy(out)
# s.append(999)
# print(s)
# print(out)
# print(copy_l)
# **********************************************************
# КОРОТКИЙ ВАРИАНТ
# def verbing(s):
#     return s + 'ly' if 'ing' in s else s + 'ing' if len(s) > 3 else s
#
# # ДЛИННЫЙ ВАРИАНТ
# def verbing(s):
#     new_s = ''
#     if 'ing' in s:
#         new_s = s + 'ly'
#         return new_s
#     elif len(s) >= 3:
#         new_s = s + 'ing'
#         return new_s
#     elif len(s) < 3:
#         return s
# s = 'swiming'
# print(verbing(s))
# **********************************************************
# сли длина четная, 1я и 2я части имеют одинаковую длину
# Если длина нечетная, мы скажем, что дополнительный символ идет в передней половине
# a-front + b-front + a-back + b-back
# def front_back(a,b):
#     a_ser = (len(a)+1)//2
#     b_ser = (len(b)+1) // 2
#     return a[:a_ser] + b[:b_ser] + a[a_ser:] + b[b_ser:]
#
# a='Kitten'
# b='Donut'
# print(front_back(a,b))
#**********************************************************
# СЛОВАРЬ
# ИЗ 'Uno dos tres cuatro cinco' --> {"": ["Uno"], "Uno": ["dos"], "dos": ["tres"], "tres": ["cuatro"], "cuatro": ["cinco"]}
# def mimic_dict(string):
#     d = {}
#     key = ''
#     for i in string.split():
#         d.setdefault(key,[]).append(i)
#         key = i
#     return d
#
# s = 'Uno dos tres cuatro cinco'
# print(mimic_dict(s))

# import random
# random.seed(42, version=2)
# def mimic_dict(string):
#     d = {}
#     key = ''
#     for i in string.split():
#         d.setdefault(key,[]).append(i)
#         key = i
#     return d
#
# def print_mimic(mimic_dict, word):
#     new_word = []
#     i = word[0]
#     new_word.append(word[0])
#     n = 200
#     for i in range(n):
#         new_word += random.choice(mimic_dict.get(i,mimic_dict['']))
#
#     return ' '.join(new_word)
#
#
#
# d = {"": ["a"], "a": ["cat", "dog", "fly"], "cat": ["and"], "and": ["a"], "dog": ["a"]}
# s = '''We are not what we should be
#         We are not what we need to be
#         But at least we are not what we used to be'''
# print((print_mimic(mimic_dict, s)))
#
#
#
# import random
#
# def print_mimic(mimic_dict, word):
#     word = word.split()
#     new_word = []
#     i = word[0]
#     new_word.append(i)
#     j = 1
#     while j != 200:
#         if i in mimic_dict:
#             i = random.choice(mimic_dict[i])
#             new_word.append(i)
#             j += 1
#         else:
#             i = random.choice(mimic_dict[''])
#             new_word.append(i)
#             j +=1
#
#     s = ''
#     for i in new_word:
#         s += i + ' '
#     return s + ''






