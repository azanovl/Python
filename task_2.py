from abc import ABC, abstractmethod

class Apparel(ABC):
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return round((self.consumption + other.consumption), 2)

class Suit(Apparel):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return round((2 * self.h + 0.3), 2)

class Coat(Apparel):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return round((self.v / 6.5 + 0.3), 2)

suit = Suit(1.85)
coat = Coat(48)
print(suit.consumption)
print(coat.consumption)
print(suit + coat)