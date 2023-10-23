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
    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def setSalary(self,salary):
        self.__salary = salary
employee = Employee('jack', '123', '990')
employee.setName('john')
employee.setAge('20')
employee.setSalary('4000')
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())