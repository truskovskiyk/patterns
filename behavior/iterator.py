class Soldier(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.MAX_HEALTH = 100

    def treat(self):
        self.health = self.MAX_HEALTH
        print(self.name, " now with max health")

    def __str__(self):
        return "Unit {}".format(self.name)

class Hero(Soldier):

    def __init__(self, name, health):
        super(Hero, self).__init__(name, health)
        self.MAX_HEALTH = 500

class Group(object):

    def __init__(self):
        self.units = []

    def add_sold(self, soldier):
        self.units.append(soldier)

class Army(object):

    def __init__(self, hero):
        self.hero = hero
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

class SoldierIterator(object):

    def __init__(self, army):
        self.army = army
        self.hero_iterated = False
        self.current_group = 0
        self.current_sold_group = 0

    def has_next(self):
        if not self.hero_iterated:
            return True
        if self.current_group < len(self.army.groups):
            return True
        if self.current_group == len(self.army.groups) - 1:
            if self.current_sold_group < len(self.army.groups[self.current_sold_group.units]):
                return True
        return False

    def next(self):
        if self.current_group < len(self.army.groups):
            if self.current_sold_group < len(self.army.groups[self.current_group].units):
                next_sold = self.army.groups[self.current_group].units[self.current_sold_group]
                self.current_sold_group += 1
            else:
                self.current_group += 1
                self.current_sold_group = 0
                return self.next()

        elif not self.hero_iterated:
            self.hero_iterated = True
            return self.army.hero
        else:
            raise ValueError("End of collection")
        return next_sold


if __name__ == '__main__':
    hero = Hero("Hero", 100)
    army = Army(hero)

    group1 = Group()
    group2 = Group()
    group3 = Group()

    group1.add_sold(Soldier("1.1", 50))
    group1.add_sold(Soldier("1.2", 50))

    group2.add_sold(Soldier("2", 60))

    group3.add_sold(Soldier("3.1", 40))
    group3.add_sold(Soldier("3.2", 40))

    army.add_group(group1)
    army.add_group(group2)
    army.add_group(group3)

    iterator = SoldierIterator(army)

    while iterator.has_next():
        print(iterator.next())
