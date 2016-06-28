from sys import getsizeof
import pickle
from abc import ABCMeta, abstractmethod

IMAGE_GOBLIN = 1000
IMAGE_DRAGON = 100000


class AbsUnit(metaclass=ABCMeta):

    def __init__(self, name, health, picture):
        self.name = name
        self.health = health
        self.picture = picture

    def __str__(self):
        msg = "Unit {} {} {}".format(self.name, self.health,
                                        getsizeof(self.picture))
        return msg

class Goblin(AbsUnit):

    def __init__(self):
        some_big_image = list(range(IMAGE_GOBLIN))
        super(Goblin, self).__init__("goblin", 8, some_big_image)

class Dragon(AbsUnit):

    def __init__(self):
        some_big_image = list(range(IMAGE_DRAGON))
        super(Dragon, self).__init__("dragon", 15, some_big_image)

class UnitImageFactory(object):
    images = {}

    @staticmethod
    def get_goblin_image():
        if 'goblin' not in UnitImageFactory.images:
            UnitImageFactory.images['goblin'] = list(range(IMAGE_GOBLIN))
        return UnitImageFactory.images['goblin']

    @staticmethod
    def get_dragon_image():
        if 'dragon' not in UnitImageFactory.images:
            UnitImageFactory.images['dragon'] = list(range(IMAGE_DRAGON))
        return UnitImageFactory.images['dragon']

class GoblinNew(AbsUnit):

    def __init__(self):
        some_big_image = UnitImageFactory.get_goblin_image()
        super(GoblinNew, self).__init__("goblin", 8, some_big_image)

class DragonNew(AbsUnit):

    def __init__(self):
        some_big_image = UnitImageFactory.get_dragon_image()
        super(DragonNew, self).__init__("dragon", 15, some_big_image)


@profile
def old():
    # without flyweight
    units = []
    for _ in range(10000):
        units.append(Goblin())
        units.append(Dragon())


@profile
def new():
    units = []
    for _ in range(10000):
        units.append(GoblinNew())
        units.append(DragonNew())


if __name__ == '__main__':

    new()
    old()

# python3 -m memory_profiler flyweight.py

# Filename: flyweight.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     61   19.707 MiB    0.000 MiB   @profile
#     62                             def old():
#     63                                 # without flyweight
#     64   19.707 MiB    0.000 MiB       units = []
#     65 5505.328 MiB 5485.621 MiB       for _ in range(10000):
#     66 5505.359 MiB    0.031 MiB           units.append(Goblin())
#     67 5505.328 MiB   -0.031 MiB           units.append(Dragon())
#
#
# Filename: flyweight.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     70   12.676 MiB    0.000 MiB   @profile
#     71                             def new():
#     72   12.676 MiB    0.000 MiB       units = []
#     73   19.707 MiB    7.031 MiB       for _ in range(10000):
#     74   19.707 MiB    0.000 MiB           units.append(GoblinNew())
#     75   19.707 MiB    0.000 MiB           units.append(DragonNew())
