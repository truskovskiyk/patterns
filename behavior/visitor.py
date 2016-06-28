from abc import ABCMeta, abstractmethod

class IVisitor(metaclass=ABCMeta):
    def visit(self, element):
        if isinstance(element, Building):
            self._visit_building(element)
        elif isinstance(element, Floor):
            self._visit_floor(element)
        elif  isinstance(element, Room):
            self._visit_room(element)
        else:
            raise ValueError("Only [Building, Floor, Room]")

    @abstractmethod
    def _visit_building(self, building):
        pass

    @abstractmethod
    def _visit_floor(self, floor):
        pass

    @abstractmethod
    def _visit_room(self, room):
        pass


class ElectricitySystemValidation(IVisitor):

    def _visit_building(self, building):
        print("Electricity: visit_building {} adress".format(
                                                    building, building.address))

    def _visit_floor(self, floor):
        print("Electricity: visit_floor {} number {}".format(
                                                    floor, floor.floor_number))

    def _visit_room(self, room):
        print("Electricity: visit_room {} room number {}".format(
                                                            room, room.number))

class IElement(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass

class Room(IElement):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        visitor.visit(self)


class Floor(IElement):
    def __init__(self, floor_number):
        self.rooms = []
        self.floor_number = floor_number

    def add_room(self, room):
        self.rooms.append(room)

    def accept(self, visitor):
        visitor.visit(self)
        for x in self.rooms:
            x.accept(visitor)

class Building(IElement):
    def __init__(self, address):
        self.floor = []
        self.address = address

    def add_floor(self, floor):
        self.floor.append(floor)

    def accept(self, visitor):
        visitor.visit(self)
        for x in self.floor:
            x.accept(visitor)


if __name__ == "__main__":
    floor1 = Floor(1)
    floor1.add_room(Room(1))
    floor1.add_room(Room(2))
    floor1.add_room(Room(3))

    floor2 = Floor(2)
    floor2.add_room(Room(4))
    floor2.add_room(Room(5))
    floor2.add_room(Room(6))

    floor3 = Floor(3)
    floor3.add_room(Room(7))
    floor3.add_room(Room(8))
    floor3.add_room(Room(9))

    building = Building("some adress")
    building.add_floor(floor1)
    building.add_floor(floor2)
    building.add_floor(floor3)

    building.accept(ElectricitySystemValidation())
