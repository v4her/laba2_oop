class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return self.__addSign(self.salary)
    def __addSign(self,salary):
        return salary + '$'

employee = Employee('john', '2000')
print(employee.getSalary())