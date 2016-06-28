from abc import ABCMeta, abstractmethod

class OldElectricitySystem(object):

    def mathc_thin_socker(self):
        return "220V [old]"

class INewElecricitySystem(metaclass=ABCMeta):

    @abstractmethod
    def match_with_socket(self):
        pass

class NewElectricitySystem(INewElecricitySystem):

    def match_with_socket(self):
        return "220V [new]"

class Adapter(INewElecricitySystem):

    def __init__(self, adaptee):
        self._adaptee = adaptee

    def match_with_socket(self):
        return self._adaptee.mathc_thin_socker()


def charge_notebook(electricity_system):
    print(electricity_system.match_with_socket())

if __name__ == '__main__':
    new = NewElectricitySystem()
    charge_notebook(new)

    old = OldElectricitySystem()
    adapter = Adapter(old)
    charge_notebook(adapter)
