class GameState(object):
    def __init__(self, health, kill_amount):
        self.health = health
        self.kill_amount = kill_amount

    def __str__(self):
        msg = "GameState : {}".format(self.__dict__)
        return msg

class GameOriginator(object):

    def __init__(self):
        self._state = GameState(100, 0)

    def play(self):
        print(self._state)
        self._state = GameState(self._state.health * 0.9, self._state.kill_amount + 2)

    def game_save(self):
        return GameMomento(self._state)

    def load_game(self, momento):
        self._state = momento.get_state()

class GameMomento(object):

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Caretaker(object):

    def __init__(self):
        self._game = GameOriginator()
        self._saves = []

    def do(self):
        self._game.play()

    def f5(self):
        self._saves.append(self._game.game_save())

    def f9(self):
        self._game.load_game(self._saves.pop())

if __name__ == '__main__':
    catetaker = Caretaker()
    catetaker.f5()
    catetaker.do()
    catetaker.f5()
    catetaker.do()
    catetaker.do()
    catetaker.do()
    catetaker.do()
    catetaker.do()
    catetaker.f9()
    catetaker.do()
