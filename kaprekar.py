#
 # def numerics(n):
#     num = []
#     while n!=0:
#         num.append(n%10)
#         n = n//10
#     return num
# def kaprekar_step(L):
#     # n1 = map(str, sorted(L))
#     # n2 = map(str, sorted(L,reverse=True))
#     return int(''.join(map(str, sorted(L,reverse=True)))) - int(''.join(map(str, sorted(L))))
#
## def kaprekar_loop(n):
#     while n != 6174:
#         print(n)
#         kap = numerics(n)
#         n = kaprekar_step(kap)
#     print(n)
#
# n = 6174
# # print(kaprekar_loop(n))
# kaprekar_loop(n)
# ********************************************************************
# ПОСТОЯННАЯ КАПРЕКАРА
# def numerics(n):
#     num = []
#     while n!=0:
#         num.append(n%10)
#         n = n//10
#     return num
# def kaprekar_check(n):
#     if len(numerics(n))<3 or len(numerics(n)) >6 or (n in [100, 1000, 100_000]) or (len(set(str(n)))<2):
#         return False
#     else: return True
# def kaprekar_step(L):
#     n1 = map(str, sorted(L))
#     n2 = map(str, sorted(L,reverse=True))
#     return int(''.join(n2)) - int(''.join(n1))
#
# def kaprekar_loop(n):
#     p_kap = {495, 6174, 549945, 631764}
#     pp = set()
#     if not kaprekar_check(n):
#         print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
#     else:
#         while n not in p_kap:
#             print(n)
#             kap = numerics(n)
#             n = kaprekar_step(kap)
#             if n not in pp:
#                 pp.add(n)
#             else:
#                 print(f'Следующее число - {n}, кажется процесс зациклился...')
#                 exit(0)
#         print(n)
##
# n = 103303
# kaprekar_loop(n)

#*********************************************************************
# def kaprekar(n):
#     k = n**2
#     i = m = 0
#     while m + k != n:
#         m = k%10 * 10**i + m
#         k = k // 10
#         i += 1
#         if m and m + k == n:
#             return True
#     return False
import math
# def kaprekar(n):
#     nn = n * n
#     print('nn=',nn)
#     for d in range(1, int(len(str(nn)))):
#         m, rem = divmod( nn, 10**d )
#         print('m=',m,'rem=',rem,'d=',10**d)
#         if rem and m + rem == n:
#             return True
#     return False
#
# n = 4879
# print(kaprekar(n))
#
# **********************************************************************
# def numerics(n):
#     num = []
#     while n!=0:
#         num.append(n%10)
#         n = n//10
#     return num
# def convert_to10(n,from_base=16):
#     alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if type(n) == str:
#         a10 = [int    (i) if i.isdigit() else i for i in n][::-1]
#     else:
#         a10 = numerics(n)
#     mm = 0
#     for i, v in enumerate(a10):
#         if type(v) == str:
#             num = alphabet.index(v)
#             mm += from_base ** i * num
#         else:
#             mm += from_base ** i * v
#     return mm
# *******************************************************
# def kaprekar(n):
#     nn = n * n
#     for d in range(1, int(len(str(nn)))):
#         m, rem = divmod( nn, 10**d )
#         if rem and m + rem == n:
#             return True
#     return False
#**************************************************************************
#
# Число Капрекара в произвольной системе счисления
# def convert(n,to_base=10,from_base=16):
#     alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     num10 = int(n, from_base) if from_base!=10 else n
#     a = []
#     while num10:
#         num10, m = divmod(num10, to_base)
#         a.append(alphabet[m])
#     return ''.join(a[::-1])
#
# def kaprekar(n, base=16):
#     num10 = int(n, base) if base!=10 else int(n)
#     num_kap = num10 * num10
#     num_kap_base = convert(num_kap,to_base=base,from_base=10)
#     if True : #base != 10:
#         for i in range(1,len(num_kap_base)):
#             r = num_kap_base[:i]
#             l = num_kap_base[i:]
#             if int(r, base) + int(l,base) == num10 and  int(l,base):
#                 return True
#         return False

# n=10
# print(kaprekar(n))
# тесты:
# test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
# test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
# test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']
# print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10
# print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10
# print([kaprekar(i, base=16) for i in test_3])
# ********************************************************************************8

