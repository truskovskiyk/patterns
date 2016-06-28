class Car(object):

    def __init__(self, brand_name):
        self.brand_name = brand_name

    def go(self):
        print("I'm " + self.brand_name + " rrrr")

class Mercedes(Car):

    def __init__(self):
        super(Mercedes, self).__init__('Mercedes')

class DecoratorCar(Car):

    def __init__(self, decorated_car):
        self.decorated_car = decorated_car

    def go(self):
        self.decorated_car.go()

class AmbuldanceCar(DecoratorCar):

    def go(self):
        self.decorated_car.go()
        print("beep-beep-beeeeep")

if __name__ == '__main__':
    car = Mercedes()
    car.go()

    dc = AmbuldanceCar(Mercedes())
    dc.go()
