class Employee:
    name = None
    salary = None
    def __init__(self,name,salary):
        print(name + ' ' + salary)

u = Employee('john', '25000')