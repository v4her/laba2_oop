class Employee:
    pass

employee1 = Employee()
employee2 = Employee()

employee1.name = 'john'
employee2.name = 'eric'

employee1.salary = 10000
employee2.salary = 25000

print(employee1.name)
print(employee2.name)
print(employee1.salary + employee2.salary)