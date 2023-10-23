class Employee:
    __name = None
    __age = None
    __salary = None
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    def show(self):
        return self.__name, self.__age, self.__salary
employee = Employee('john', 20, 2000)
print(employee.show())