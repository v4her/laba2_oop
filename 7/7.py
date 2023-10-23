class Employee:
    name = None
    salary = None
    def show(self):
        print(self.name)
        print(self.salary)
employee = Employee()
employee.name = 'john'
employee.salary = 25000
employee.show()
