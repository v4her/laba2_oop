class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name, age, salary):
        self.__age = age
        self.__name = name
        self.__salary = salary
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary

employee = Employee('john', '20', '2000')
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())