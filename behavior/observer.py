import random
from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self, subject):
        pass

class RiskyPlayer(IObserver):

    def __init__(self, boxer_to_put_money_on):
        self.boxer_to_put_money_on = boxer_to_put_money_on

    def update(self, subject):
        if subject.boxer_a_score < subject.boxer_b_score:
            decision = "I put on boxer B, if he win I get more!"
        else:
            decision = "I put on boxer A, if he win I get more!"
        print("RiskyPlayer {}".format(decision))

class ConservativePlayer(IObserver):

    def __init__(self, boxer_to_put_money_on):
        self.boxer_to_put_money_on = boxer_to_put_money_on

    def update(self, subject):
        if subject.boxer_a_score < subject.boxer_b_score:
            decision = "I put on boxer A, be save"
        else:
            decision = "I put on boxer B, be save"
        print("ConservativePlayer {}".format(decision))


class ISubject(metaclass=ABCMeta):

    @abstractmethod
    def attach_observer(self, observer):
        pass

    @abstractmethod
    def detach_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class BoxFight(ISubject):

    def __init__(self):
        self.observers = []
        self.round_number = 0
        self.boxer_a_score = 0
        self.boxer_b_score = 0

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def next_round(self):
        self.round_number += 1
        self.boxer_a_score += random.randint(0, 5)
        self.boxer_b_score += random.randint(0, 5)

        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self)


if __name__ == '__main__':
    box_fight = BoxFight()

    risk_player = RiskyPlayer("Boxer A")
    conservative_player = ConservativePlayer("Boxer B")

    box_fight.attach_observer(risk_player)
    box_fight.attach_observer(conservative_player)

    for _ in range(12):
        box_fight.next_round()
