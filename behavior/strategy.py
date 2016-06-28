from abc import ABCMeta, abstractmethod

class IWearingStrategy(metaclass=ABCMeta):

    @abstractmethod
    def get_clothes(self):
        pass

    @abstractmethod
    def get_accessories(self):
        pass

class DefaultWearingStrategy(IWearingStrategy):
    def get_clothes(self):
        return "jacket"

    def get_accessories(self):
        return ""


class SunshiWearingStrategy(IWearingStrategy):
    def get_clothes(self):
        return "T-Shirt"

    def get_accessories(self):
        return "sunglasses"


class Myself(object):

    def __init__(self):
        self.strategy = DefaultWearingStrategy()

    def change_strategy(self, strategy):
        self.strategy = strategy

    def go_outside(self):
        clothes = self.strategy.get_clothes()
        accessories = self.strategy.get_accessories()
        print("I wore {} and {}".format(clothes, accessories))


if __name__ == "__main__":
    m = Myself()
    m.go_outside()
    m.change_strategy(SunshiWearingStrategy())
    m.go_outside()
