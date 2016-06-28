from abc import ABCMeta, abstractmethod

# realization
class WallCreator(metaclass=ABCMeta):

    @abstractmethod
    def build_wall_with_door(self):
        pass

    @abstractmethod
    def build_wall(self):
        pass

    @abstractmethod
    def build_wall_with_window(self):
        pass


class SomeWallCreator(object):

    def build_wall_with_door(self):
        print("build_wall_with_door")

    def build_wall(self):
        print("build_wall")

    def build_wall_with_window(self):
        print("build_wall_with_window")

# interface
class IBuildCompany(metaclass=ABCMeta):

    wall_creator = None

    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_room(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

class BuildCompany(IBuildCompany):

    def build_foundation(self):
        print("BuildCompany build_foundation done")

    def build_room(self):
        self.wall_creator.build_wall_with_door()
        self.wall_creator.build_wall()
        self.wall_creator.build_wall_with_window()
        self.wall_creator.build_wall()
        print("BuildCompany build_room done")

    def build_roof(self):
        print("BuildCompany buil_roof done")

if __name__ == '__main__':
    some_wall_creator = SomeWallCreator()

    build_company = BuildCompany()
    build_company.build_foundation()
    build_company.wall_creator = some_wall_creator
    build_company.build_room()
    build_company.build_room()
    build_company.build_roof()
