class Passenger:
    def __init__(self, name, family, fromx, fromy, tox, toy):
        self.name = name
        self.family = family
        self.fromx = fromx
        self.fromy = fromy
        self.tox = tox
        self.toy = toy

    @property
    def distance(self):
        return ((self.tox - self.fromx) ** 2 + (self.toy - self.fromy) ** 2) ** 0.5
