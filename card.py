from enum import Enum
from itertools import product

# noinspection PyArgumentList
Room = Enum('Room', 'Hall Lounge Dining Kitchen Ballroom Conservatory Billiard Library Study')
# noinspection PyArgumentList
Person = Enum('Person', 'White Plum Scarlett Mustard Green Peacock')
# noinspection PyArgumentList
Weapon = Enum('Weapon', 'Knife Candlestick Rope Pipe Wrench Revolver')


def all_cards():
    return list(Room) + list(Person) + list(Weapon)


def all_solutions():
    return product(list(Room), list(Person), list(Weapon))





