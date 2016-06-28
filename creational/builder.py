from abc import ABCMeta, abstractmethod

class Laptop(object):
    def __init__(self):
        self.monitor = None
        self.memory = None
        self.hdd = None
        self.battery = None
        self.processor = None

    def is_ready(self):
        if all(self.__dict__.values()):
            return True
        else:
            return False

    def __str__(self):
        statys = "ready" if self.is_ready() else "not ready"
        msg = ("hello. I'm laptop. \n"
                "I'm %s \n"
                "My configs are %s"
                % (statys, self.__dict__))
        return msg


class LaptopBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.laptop = Laptop()

    def get_my_laptop(self):
        return self.laptop

    @abstractmethod
    def set_monitor(self):
        pass

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def set_hdd(self):
        pass

    @abstractmethod
    def set_battery(self):
        pass

    @abstractmethod
    def set_processor(self):
        pass

class GamingLaptopBuilder(LaptopBuilder):

    def set_monitor(self):
        self.laptop.monitor = "game monitor"

    def set_memory(self):
        self.laptop.memory = "game memory"

    def set_hdd(self):
        self.laptop.hdd = "game hdd"

    def set_battery(self):
        self.laptop.battery = "game battery"

    def set_processor(self):
        self.laptop.processor = "game processor"

class TripLaptopBuilder(LaptopBuilder):

    def set_monitor(self):
        self.laptop.monitor = "trip monitor"

    def set_memory(self):
        self.laptop.memory = "trip memory"

    def set_hdd(self):
        self.laptop.hdd = "trip hdd"

    def set_battery(self):
        self.laptop.battery = "trip battery"

    def set_processor(self):
        self.laptop.processor = "trip processor"


class BuyLaptop(object):

    def set_builder(self, builder):
        self.builder = builder

    def get_laptop(self):
        return self.builder.get_my_laptop()

    def construct_laptop(self):
        self.builder.set_monitor()
        self.builder.set_memory()
        self.builder.set_hdd()
        self.builder.set_battery()
        self.builder.set_processor()

if __name__ == '__main__':
    trip_b = TripLaptopBuilder()
    game_b = GamingLaptopBuilder()

    direct = BuyLaptop()

    direct.set_builder(trip_b)
    direct.construct_laptop()
    print(direct.get_laptop())

    direct.set_builder(game_b)
    direct.construct_laptop()
    print(direct.get_laptop())
