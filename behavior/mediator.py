class BodyPart(object):

    def __init__(self, brain):
        self.brain = brain

    def changed(self):
        self.brain.something_happened(self)

class Ear(BodyPart):

    def head_something(self):
        print("sound")
        self.sound = "sound"
        self.changed()

    def get_sound(self):
        return self.sound

class Face(BodyPart):

    def smile(self):
        print("smile")

class Brain(object):

    def __init__(self):
        self.ear = Ear(self)
        self.face = Face(self)

    def something_happened(self, body_part):
        if isinstance(body_part, Ear):
            print(self.face.smile())
        elif isinstance(body_part, Face):
            print(self.ear.get_sound())

if __name__ == '__main__':
    b = Brain()
    b.ear.head_something()
