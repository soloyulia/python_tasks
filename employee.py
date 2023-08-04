class Employee():
    def __init__(self,first,last,oklad):
        self.first = first
        self.last = last
        self.oklad = oklad
    def give_raise(self):
        self.oklad +=5000
    def get_employee(self):
        print(f"Имя работника: {self.first}, {self.last}")
        print(f"Оклад :{self.oklad}")

my_employee = Employee('Yulia','Solovjeva',1000)
my_employee.give_raise()
my_employee.get_employee()