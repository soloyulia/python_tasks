# **************************************************************8
# with open('d1.txt',encoding='utf-8') as file:
#     sheet = file.readlines()
#     a=[]
#     for item in sheet:
#         item=item.split()
#         for j in item:
#             if j.isdigit():
#                 a.append(int(j))
#     print(a)
#     average_rating = sum(a)/len(a)
#     print(average_rating)
    # for line in file:
    #     print('line.split[-2]= ',line.split()[-2])
    #     if line.split()[-1] == '(экзамен)' or line.split()[-1] == '(автомат)':
    #         summ += int(line.split()[-2])
    #         count += 1
    # average_rating = summ/count
    # print('OK' if average_rating == float(mean) else 'ERROR')



# with open('d1.txt',encoding='utf-8') as file, open('d1.txt',encoding='utf-8') as m:
#     mean = m.read()
#     summ = count = 0
#     for line in file:
#         print('line.split[-2]= ',line.split()[-2])
#         if line.split()[-1] == '(экзамен)' or line.split()[-1] == '(автомат)':
#             summ += int(line.split()[-2])
#             count += 1
#     average_rating = summ/count
#     print('OK' if average_rating == float(mean) else 'ERROR')
# ******************************************************************
# переделать!!
# import os
# file_name='durdomm.txt'
# event = "git fetch 800"
#
# if os.path.isfile(file_name):
#     with open(file_name,'r+' ) as f:
#         all_f = f.readlines()
#         count = len(all_f) if all_f.count('\n') >= 1 else len(all_f)+1
#         all_f.insert(0,f"event {count} - '{event}'\n")
#         for i in all_f:
#             f.write(i)
# else:
#     with open(file_name,'w') as file:
#         file.write(f"event 1 - '{event}'")

# *************************************************
# МОЙ РАБОЧИЙ КОД
# import os
# file_name='durdom.txt'
# event = "git fetch 800"
#
# if os.path.isfile(file_name):
#     with open(file_name,'r' ) as f:
#         all_f = f.readlines()
#         count = len(all_f) if all_f.count('\n') >= 1 else len(all_f)+1
#         all_f.insert(0,f"event {count} - '{event}'\n")
#     with open(file_name,'w') as file:
#         for i in all_f:
#             file.write(i)
#
# else:
#     with open(file_name,'w') as file:
#         file.write(f"event 1 - '{event}'")
# import os
# file_name='tmp/dir/'
# if os.path.isfile(file_name):
#     with open(file_name) as f:
#         print('CONTENT:', f.read())
# elif os.path.isdir(file_name):
#     print('ERROR:\nЭто каталог, а не файл')
# else:
#     print('ERROR:\nФайл не существует')

# if not os.path.exists(file_name):
#     print('ERROR:', 'Это каталог, а не файл', sep='\n')
# elif not os.path.isfile(file_name):
#     print('ERROR:', 'Файл не существует', sep='\n')
# else:
#     with open(file_name) as f:
#         print('CONTENT:', f.read())
# ***************************************************************
# from collections import Counter
# with open('d1.txt',encoding='utf-8') as f:
#     line=f.readline().replace(',',' ').replace('.',' ').split()
#     print(line)
#     d=Counter(line)
#
#     print(d)
#     # print(*sorted(d.most_common(),key=lambda x:x[1])[-1])
#     word=d.most_common()[0][0]
#     word_count=d.most_common()[0][1]
#     print(word, word_count)
# ************************************************
# import os.path
# if os.path.isfile('data.txt'):
#     with open('data.txt','r',encoding='utf-8') as f:
#         line=f.read()
#         with open('out.txt','w',encoding='utf-8') as f1:
#             f1.write(line)
# else:
#     with open('data.txt','w',encoding='utf-8') as file:
#         file.write('Третий фактор')
# ***********************************************8888
# with open('ex.txt', 'r',encoding='utf-16') as f:
#     answer=f.read()
# with open('ex.txt', 'a',encoding='utf-16') as f:
#     f.write('\nhacked')
# ***************************************************************
# **********************************************
# РАБОТА С ФАЙЛАМИ
# Напишите функцию file_n_lines, которая печатает первые n-строка файла.
# Функция file_n_lines принимает на вход название файла и количество строк
# для прочтения.
#
# def file_n_lines(file_name,n):
#     with open(file_name,'r', encoding='utf-8') as file:
#         for i in range(n):
#             print(file.readline().strip())
#
# file_name='d1.txt'
# n=3
# file_n_lines(file_name,n)
# ******************************************************************88
# def create_file_with_numbers(n):
#     with open(f"range_{n}.txt",'w') as file:
#         for i in range(1,n+1):
#             file.write(str(i)+'\n')
#
# n=5
# create_file_with_numbers(n)
#***************************************************************8
# from string import punctuation
# print()
# def longest_word_in_file(file_name):
#     with open(file_name,'r',encoding='utf-8') as file:
#         max_word=''
#         # print(max_word)
#         for word in file.read().split():
#             for i in word:
#                 if i in punctuation.strip():
#                     word=word.replace(i,'')
#             if len(word)>=len(max_word):
#                 max_word=word
#     return max_word
#
# print(longest_word_in_file('range_5.txt'))

# from string import punctuation
# def longest_word_in_file(file_name: str) -> str:
#     with open(file_name,'r',encoding='utf-8') as file:
#         max_word=file.readline().split()[0]
#         for row in file.readline().split():
#             if len(row)>len(max_word):
#                 max_word=row
#         for i in max_word:
#             if i in punctuation.strip():
#                 max_word=max_word.replace(i,'')
#     return max_word

# *******************************************************
# НАЙТИ КОЛИЧЕСТВО ТРЕХЗНАЧНЫХ И СУММУ ДВУЗНАЧНЫХ ЦИФР
# with open('numbers (1).txt',encoding='utf-8') as file:
#     count_three=0
#     summ_two=0
#     for i in file.read().split():
#         if len(i)==3:
#             count_three+=1
#         elif len(i)==2:
#             summ_two += int(i)
#     print(count_three)
#     print(summ_two)
#********************************************************
# def find_lines_len_more_6(file_name):
#     with open(file_name, encoding='utf-8') as file:
#         count_line=0
#         for i in file.read().splitlines():
#             if len(i)>=6:
#                 count_line+=1
#         print(count_line)
# find_lines_len_more_6('d1.txt')
# **************************************************
# НАЙТИ КОЛИЧЕСТВО УНИКАЛЬНЫХ СЛОВ
# with open('lorem.txt',encoding='utf-8') as file:
#     # d=[]
#     # for i in file.read().lower().split():
#     #     if i not in d:
#     #        d.append(i)
#     dd=[]
#     dd=[i for i in file.read().lower().split() if i not in dd]
#     print(dd)
#     print(len(set(dd)))
# **************************************************************
# ПОСЧИТАТЬ СКОЛЬКО РАЗ ВСТРЕТИЛОСЬ КАЖДОЕ СЛОВО
# with open('lorem.txt',encoding='utf-8') as file:
#     words={}
#     for i in file.read().upper().split():
#        words[i]=words.get(i,0)+1
#     print(words)
# ***********************************************************
# найти слова, заканчивающиеся на 'ея' и отсортировать
# with open('words.txt',encoding='utf-8') as file:
#     d={}
#     for i in file.read().upper().split():
#         if i[-2:]=='ЕЯ':
#             d[i]=d.get(i,len(i))
# for k,v in sorted(d.items(),key=lambda x:x[1]):
#     print(k)
# ************************************************************
# import json
# with open('manager_sales.json',encoding='utf-8') as file:
#     line=file.read()
#     # print(line)
#     d={}
#     json_data=json.loads(line)
#     print(json_data)
#     for i in json_data:
#         d[i['manager']['first_name']]=0
#         for j in ['cars']:
#             d[i['manager']['first_name']+= j['price']