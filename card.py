from enum import Enum
from itertools import product, combinations

Room = Enum('Room', 'Hall Lounge Dining Kitchen Ballroom Conservatory Billiard Library Study')
Person = Enum('Person', 'White Plum Scarlett Mustard Green Peacock')
Weapon = Enum('Weapon', 'Knife Candlestick Rope Pipe Wrench Revolver')


def all_cards():
    return set(Room) | set(Person) | set(Weapon)


def possible_solutions(cards):
    r = set()
    w = set()
    p = set()
    for card in cards:
        if type(card) is Room:
            r.add(card)
        if type(card) is Weapon:
            w.add(card)
        if type(card) is Person:
            p.add(card)
    return list(product(r, w, p))


def possible_player_cards(remaining, n):
    return combinations(remaining, n)


def remaining_cards(possibility):
    cards = all_cards()
    for player in possibility:
        cards -= player
    return cards


def all_possibilities():
    pass


