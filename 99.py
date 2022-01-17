class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details: ', self.name,self.color,self.price)

    def maxspeed(self):
        print("Vehicle max Speed : 120kmph")

    def changegear(self):
        print('Can change upto 6 gears.')

class Car(Vehicle):
    def maxspeed(self):
        print("Max Speed : 125kmph")

    def changegear(self):
        print("Can change upto 7 gears")

car = Car('HI: ','orange: ',564321)
car.show()
car.maxspeed()
car.changegear()

print('\n')
v = Vehicle('Abc','red',898481)
v.show()
v.maxspeed()
v.changegear()
