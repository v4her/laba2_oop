class Employee:
    name = None
    salary = None
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        return (self.name)
    def show(self):
        return (self.salary)
    def show(self):
        return (self.salary / 10 + self.salary)

employee = Employee('john', 2500)
print(employee.name)
print(employee.salary)
print(employee.show())
