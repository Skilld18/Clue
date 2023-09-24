from enum import Enum, auto
from itertools import product


class Room(Enum):
    Hall = auto()
    Lounge = auto()
    Dining = auto()
    Kitchen = auto()
    Ballroom = auto()
    Conservatory = auto()
    Billiard = auto()
    Library = auto()
    Study = auto()


class Person(Enum):
    White = auto()
    Scarlett = auto()
    Plum = auto()
    Green = auto()
    Mustard = auto()
    Peacock = auto()


class Weapon(Enum):
    Knife = auto()
    Rope = auto()
    Wrench = auto()
    Revolver = auto()
    Candlestick = auto()
    Pipe = auto()


def all_cards():
    return list(Room) + list(Person) + list(Weapon)


def all_solutions():
    return product(list(Room), list(Person), list(Weapon))
