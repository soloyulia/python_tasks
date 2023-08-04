import numpy
import numpy as np
# a = list(map(float,input().split(',')))
# a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
# V1 = np.array(a,dtype=float)
# V2 = np.array(a[-2:-1], dtype=float)
# V3 = np.array(a[::-1],dtype=float)
# V4 = np.array(a[::3],dtype=float)
# V5 = np.array(range(len(a)),dtype=int)
# print(V1)
# print(V2)
# print(V3)
# print(V4)
# print(V5)
# *********************************************************
# a = [1,2,3,4,5,6]
# b = [1,2,3,4]
#
# v1 = np.array(a)
# v2 = np.array(b)
# v = np.array([v//b[-2] for i,v in enumerate(a) if v%b[-2] == 0],dtype=float)
# print(v)
# ********************************
# Площадь треугольника по координатам его вершин
# import functools
# A1 = np.array((-1, 1))
# A2 = np.array((2, 5))
# A3 = np.array((5, -3))
#
# rez1 = functools.reduce(lambda a, b : a * b, np.array(A1 - A2))
# rez2 = functools.reduce(lambda a, b : a * b, np.array(A2 - A3))
# print((rez1-rez2)*0.5)


# m = np.array([[11,22,33],[3,5,6],[33,5,7]])
# for elem in m:
#     print(elem)
#     print(elem *2)
#     print()
# v1 = np.array((1,2,3,4))
# v2 = np.array((-6,-3,5,6))
# v3 = np.array((10,20,30,40))
# v4 = np.array((100,200,300,400))
# m1 = np.array((v1,v2))
# m2 = np.array((v3,v4))
# hiper = np.array((m1,m2))
#
# b=v1.dot(v2)
# print(b)

# for matrix in hiper:
#     print('matrix')
#     for j in matrix:
#         print('line')
#         for k in j:
#             print(k)
#     print()
# np.set_printoptions(suppress=True)
# M1 = np.array((
#     (1., 2., 3., 0.),
#     (4., 5., 6., 0.),
#     (0., 1., 1., 6.),
#     (7., 8., 9., 0.)
# ))
# M2 = np.array(M1)
# for i in range(len(M2[-2,:])):
#     M2[-2][i]=np.sin((M2[-2][1]*np.pi)/6)
#
# for i in range(len(M2[:,-2])):
#     M2[i][-2]=np.exp(M2[i][-2])
#
#
# M2[-2,:] = np.sin((M2[-2]*np.pi)/6)
# M2[:,-2]=np.exp(M2[-2])
# print(M2)

# shape = input().split()
# a = [int(i) for i in shape if i.isdigit()]
# dtyp = shape[-1] if shape[-1].isalpha() else float
# Z = np.zeros(shape=(tuple(a)),dtype=dtyp )
# print(Z)

# a = np.zeros((10,10))
# print(a.itemsize*np.prod(a.shape))

# print(numpy.info(np.add))
# print(np.info(np.array))

# n = 10
# m = 50
# Z = np.array(range(n,m,1))
# print(Z)

# a = np.array([1,2,3,4])
# a = a[::-1]
# print(a)

# n = 6
# m = 2
# k = 3
# Z = np.array(range(n)).reshape(m,k)
# print(Z)

# Z = np.array([[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],
#           [0, 0, 9]])
# print(list(Z[Z>3]))

# n = 3
# Z = np.eye(n)
# print(Z)

import random
# n = 2
# m = 2
# l = 2
# np.random.seed(42)
# Z = np.random.sample((n,m,l))
# print(Z)

# n = 3
# m = 4
# np.random.seed(42)
# a = np.random.sample((n,m))
# print(a)
# # b = np.mean(a,axis=0)
# print(np.mean(a,axis=0).min(),np.mean(a,axis=0).max(),sep='\n')

# На границе матрицы будут стоять 1
# n = 10
# m = 10
# Z = np.zeros((n,m))
# Z[0] = Z[-1] = Z[:,-1] = Z[:,0 ] = 1
# print(Z)

# Добавьте вокруг имеющихся значений матрицы "забор" из 0.
# a = np.array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
#
# Z = np.pad(a,pad_width=1,mode='constant', constant_values=0)
# print(Z)

# Создайте диагональную матрицу размера n*n. На главной диагонали должны быть числа от 1 до n.
# n = 3
# a = np.diag((range(1,n+1)))
# print(a)

# x - сдвиг для единственной ненулевой диагонали в матрице.
# x = 1
# k = 2
# Z = np.diag((range(1,k+1)),k=x)
# print(Z)

# n = 8
# m = 8
# x = np.array([[0., 1.],[1., 0.]])
#
# # x[1::2,::2] = 1
# # x[::2,1::2] = 1
# print(Z)

# import numpy as np
# n, m = map(int,input().split())
# Z = np.zeros((n,m),dtype=float)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1
# **************************************************
# Функция numpy.unravel_index проводит обратную операцию - по индексу
# элемента определяет его "координаты" в матрице.
# i = 5
# z = np.array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
# s =z.shape
# x = np.unravel_index(i, s, order='C')
# print(x)

a = np.array([[ 99,11,55],
       [ 33,66,99]])

x = np.shape(a)

Z = np.around((a - np.mean (a)) / (np.std (a)),2)
print(Z)





