class Employee:
    name = None
    surname = None
    def __init__(self):
        print('+++')
employee = Employee()
employee.name = 'john'
employee.surname = 'doe'
print(employee.name, employee.surname)