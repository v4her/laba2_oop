class Car:
    color = None
    height = None
    weight = None
    fuel = None

    def turn(self):
        pass

    def go(self):
        pass

    def stop(self):
        pass
    pass

myCar = Car()
myCar.color = 'white'
myCar.fuel = 100
myCar.weight = 'heavy'
myCar.height = 'medium'

def info(self):
    print(self.color)
    print(self.fuel)
    print(self.weight)
    print(self.height)

info(myCar)