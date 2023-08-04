# ШИФР ЦЕЗАРЯ

# Реализуйте функцию caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
# функция должна корректно работать с любым переданным алфавитом
# from string import ascii_uppercase, punctuation,ascii_lowercase
#
# def caesar(text, key,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
#     my_punct = punctuation + ' '
#     text1 = ['' if i in my_punct else i.upper() for i in text ]
#     res = ''
#     for i in ''.join(text1):
#         res += alphabet[(alphabet.index(i) + key) % len(alphabet)]
#     return res

# Реализуйте функцию caesar(text, key), возвращающую зашифрованный текст, работающую только с латинским алфавитом.
# def caesar(text, key):
#     my_punct = punctuation + ' '
#     text1 = ['' if i in my_punct else i.upper() for i in text ]
#     res = ''
#     for i in ''.join(text1):
#             res += ascii_uppercase[(ascii_uppercase.index(i) + key) % len(ascii_uppercase)]
#     return res
# key = 13
# text='А что, если это будет смесь, Runglish? Let me speak from my heart!'
# print(caesar(text,key))
#***********************************************************************************8
# выводит на печать все возможные "расшифровки" исходного текста.
# def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     res = ''
#     for k in range(len(alphabet)-1,0,-1):
#         res = ''
#         for i in text:
#             res += alphabet[(alphabet.index(i) + k) % len(alphabet)]
#         print(res)
#
# text = 'BQQMF'
# bruteforce(text)
# *********************************************************************************8888
# Реализуйте функцию jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False),
# возвращающую зашифрованный текст, по алгоритму описанному на предыдущем шаге.
# from string import ascii_uppercase, punctuation
#
# def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=True):
#     key = str(key)
#     my_punct = punctuation + ' '
#     text1 = ['' if i in my_punct else i.upper() for i in text ]
#     res = ''
#     current_ind = 0
#     current_key = key[current_ind]
#     rever = 1 if not reverse else -1
#     for i in ''.join(text1):
#         res += alphabet[(alphabet.index(i) + int(current_key)*rever) % len(alphabet)]
#         if current_ind < len(key)-1:
#             current_ind += 1
#         else:
#             current_ind = 0
#         current_key = key[current_ind]
#     return res
#
#
# text = 'ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР'
# key=423
# alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# print(jarriquez_encryption(text,key,alphabet))
# ******************************************************************
# ВИЖЕНЕР. НАДО ДОДЕЛАТЬ!
# from string import ascii_uppercase, punctuation
# def jarriquez_encryption(text, key, alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', reverse=True):
#
#     key = str(key)
#     my_punct = punctuation + ' '
#     text1 = ['' if i in my_punct else i.upper() for i in text ]
#     # print (text1)
#     # key =''
#     res = ''
#     current_ind = 0
#     current_key = key[current_ind]
#     rever = 1 if not reverse else -1
#     for i in ''.join(text1):
#         res += alphabet[(alphabet.index(i) + int(current_key)*rever) % len(alphabet)]
#         if current_ind < len(key)-1:
#             current_ind += 1
#         else:
#             current_ind = 0
#         current_key = key[current_ind]
#     return res
#
# text = 'я люблю алмаз раджи'
#
# # print(jarriquez_encryption(text, 123))
# # ЮЮИЭЯИЭЮЭККЭЖЮНЯВГЗ
#
# # print(jarriquez_encryption('ЮЙЫАЙЫЯЙЙЯЕНЯВГЗ', 123, 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', False))
# def decrypt1(shifr, keywords):
#     alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#
#     current_key = 200000
#
#     while current_key < 261090:
#         decrypted = crypt(shifr, str(current_key), direct=-1)
#         print(current_key, decrypted)
#         found = 0
#         for word in keywords:
#             if word in decrypted:
#                 found += 1
#         # print(found)
#         if found:
#             print("\n" + str(current_key) + "\n" + decrypted+"\n")
#             if found == len(keywords):
#                 break
#         current_key += 1
#         if current_key%100 == 0:
#             print ("\r"+str(current_key), end='')
#
#     return current_key
#
# import string
# def crypt(s, key, direct=1):
#     alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     # s.translate(None, string.punctuation+' ')
#     s.translate(str.maketrans('', '', string.punctuation+' '))
#     current_ind = 0
#     current_k = key[current_ind]
#     ret = ''
#     for symbol in s:
#         offset = alphabet.index(symbol) + int(current_k)*direct
#         if offset > len(alphabet):
#             offset -= len(alphabet)
#         ret += alphabet[offset]
#         if current_ind < (len(key)-1):
#             current_ind +=1
#         else:
#             current_ind = 0
#         current_k = key[current_ind]
#     return ret
# import time
# start_time = time.time()
# big = 'ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС'
# # decrypt1('ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР', ['АЛМАЗ','ЖАРР'])
# # decrypt1('ЮЮИЭЯИЭЮЭККЭЖЮНЯВГЗ', ['АЛМАЗ','ЛЮБЛЮ'])
# decrypt1(big, ['ПРЕСТУПЛЕНИЕ','АЛМАЗ','ДАКОСТА'])
# print("--- %s seconds ---" % (time.time() - start_time))
# *************************************************************************
# import random
# from string import ascii_uppercase, punctuation
# random.seed(42)
# def disc_generator(alphabet):
#
#     a = list(alphabet)
#     random.shuffle(a)
#     return ''.join(a)
#
# def caesar(text, key,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
#     my_punct = punctuation + ' '
#     text1 = ['' if i in my_punct else i.upper() for i in text ]
#     res = ''
#     for i in ''.join(text1):
#         res += alphabet[(alphabet.index(i) + key) % len(alphabet)]
#     return res
#
# discs = ['QMJZTGFKPWLSBOXNCRYEVHIADU',
#     'CVMHTPQXZJLWORBDUGEYKNFAIS',
#     'AMPKIXVFQEWODNZYHBCGSLTUJR',
#     'NMPJZSBAQDILKEGOYHRFXTCUVW',
#     'JHANFBRXVQYTLDCIEOMPUZKWSG',
#     'ZHJLSWGXQBKAPYIORMCTNVFUED' ]
#
#
# def jefferson_encryption(text, discs, step, reverse=False):
#     pass
# text = 'Some encripted text'
# print(len('NUXHUEVGQBIJJZNVI'))
# n = 6
#
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# discs = []
# for i in range(n):
#     discs.append(disc_generator(alphabet))
# print(discs)

# ШИФР ЦЕЗАРЯ
# from string import ascii_uppercase, punctuation
# import string
# def caesar(text, key,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     my_punct = punctuation + ' '
#     text_no_punct = text.translate(str.maketrans('', '', string.punctuation+' ')).upper()
#     print(text_no_punct)
#     res = ''
#     for i in text_no_punct:
#         res += alphabet[(alphabet.index(i) + key) % 26]
#         print('i=',i,'res',res)
#     return res
#
# text = 'Ave, Caesar'
# key = 3
# print(caesar(text,key))


