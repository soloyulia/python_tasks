# class Monster:
#     def __init__(self,name, character):
#         self.name = name
#         self.character = character
#     def type(self):
#         return 'Монстр'
#     def show(self):
#         print('Имя: ', self.name)
#         print('Особенность: ', self.character)
#         print('Тип: ', self.type())
#
# class GMonster(Monster):
#     def type(self):
#         return 'Первый сын монстра'
# class SMonster(Monster):
#     def type(self):
#         return 'Второй сын монстра'
#
# Frenk = Monster('Френки','необычный')
# Frenk.show()
# print()
# Albert = GMonster('Альберт','задумчивый')
# Albert.show()
# print()
# Zigmund = SMonster('Зигмунд','веселый')
# Zigmund.show()


# class Animal():
#
#     def __init__(self,name):
#         self.name = name
#         print('Родилось животное ',self.name)
#     def eat(self):
#         print(self.name, 'говорит мяу-мяу')
#     def setname(self,newname):
#         self.name =newname
#     def getname(self):
#         return self.name
#     def makeNoice(self):
#         print(self.name,'говорит Гр-р-р-р')
#
# myAnimal = Animal('Динозавр Рекс ')
# # print(myAnimal.getname())
# # myAnimal.setname('Тиранозавр Рекс')
# # print(myAnimal.getname())
# # myAnimal.makeNoice()
# # myAnimal.eat()
# # myAnimal.makeNoice()
# # print(myAnimal.getname())
#
# class Dog(Animal):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def setname(self,newname):
#         self.name = newname
#     def getname(self):
#         return self.name
#     def bark(self):
#         print(self.name, 'говорит Гаав!')
#
# mydog = Dog('Spoti',5)
# mydog.setname('Sharik')
# mydog.makeNoice()
# # print(mydog.getname())
# # mydog.bark()
#
#
#
# class Cat(Animal):
#
#     def __init__(self,age,weight):
#         self.age =age
#         self.weight =weight
#
#     def meow(self):
#         print(self.name, 'говорит Мяу')
# mycat = Cat(5,25)
# mycat.name='Котэ'
# mycat.makeNoice()
#
# mycat.meow()

# class StringVar():
#     def __init__(self,name):
#         self.name = name
#     def setString(self):
#         self.name =self.name.replace('люди','господа')
#         self.name =self.name.upper()
#
#     def getString(self):
#         dl = len(self.name)
#         print(self.name)
#         print('Количество символов строки: ', dl)
#
# myString = StringVar('Здравствуйте, люди добрые')
# myString.getString()
# myString.setString()
# myString.getString()
# s = 'Здравствуйте, люди добрые'
# s1 = 'Здравствуйте, господа добрые'
# print(len(s1))

# class Person():
#     name =''
#     def __init__(self):
#         print('Создан человек')
#
#
# class Employee(Person):
#     job_title =''
#     def __init__(self):
#         Person.__init__(self)
#         print('Создан работник')
#
# class Customer(Person):
#     email =''
#     def __init__(self):
#         Person.__init__(self)
#         print('Создан покупатель')
#
#
# johnSmith = Person()
# johnSmith.name='Join Smith'
#
# janeEmployee=Employee()
# janeEmployee.name='Jane Employee'
# janeEmployee.job_title='veb developer'
#
# bobCustomer=Customer()
# bobCustomer.name='Bob Customer'
# bobCustomer.email='bob@gmail.com'

class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return "({0.x},{0.y})".format(self)
    def func(self):
        return abs(self.x-self.y)

a=Point()
print(str(a))
b=Point(13,6)
print(str(b))
b.x=-19
print(a.func())
print(str(b))
print(a==b,a!=b)

import math
class Circle(Point):
    def __init__(self,radius,x=0,y=0):
        super().__init__(x,y)
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def circumference(self):
        return 2*math.pi*self.radius
    def __eq__(self, other):
        return self.radius==other.radius and super().__eq__(other)
    def __str__(self):
        return "({0.radius},{0.x},{0.y})".format(self)
circle = Circle(2)
circle.radius=3
circle.x=12
a=Circle(4,5,6)
b=Circle(4,5,6)
print(str(a))
print(str(b))
print(a==b)
print(a==circle)
print(a!=circle)
print(circle.func())





