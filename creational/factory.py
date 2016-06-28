from abc import ABCMeta, abstractmethod

# toys module

class AnimalToy(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        msg =  ("hello: my type %s my name %s" %
                (type(self), self.name))
        return msg

class Cat(AnimalToy):
    pass

class Bear(AnimalToy):
    pass

class TeddyCat(Cat):
    def __init__(self):
        super(Cat, self).__init__("teddt cat")

class WoodenCat(Cat):
    def __init__(self):
        super(Cat, self).__init__("wooden cat")

class TeddyBear(Bear):
    def __init__(self):
        super(Bear, self).__init__("teddt bear")

class WoodenBear(Bear):
    def __init__(self):
        super(Bear, self).__init__("wooden bear")

# factory module

class ToyFactory(metaclass=ABCMeta):

    @abstractmethod
    def get_bear(self):
        pass

    @abstractmethod
    def get_cat(self):
        pass

class TeddyToyFactory(ToyFactory):

    def get_bear(self):
        return TeddyBear()

    def get_cat(self):
        return TeddyCat()

class WoodenToyFactory(ToyFactory):

    def get_bear(self):
        return WoodenBear()

    def get_cat(self):
        return WoodenCat()


if __name__ == '__main__':
    tf = TeddyToyFactory()

    print(tf.get_bear())
    print(tf.get_cat())

    wf = WoodenToyFactory()
    print(wf.get_bear())
    print(wf.get_cat())
