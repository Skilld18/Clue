from enum import Enum
from itertools import product, combinations, chain
import math

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

def player_recurse(remaining, num_players):
    pass

def flatten(data):
    return chain(*data)


def all_possibilities(realities, remaining, num_players):
    # player_cards = math.ceil(len(remaining) / num_players)
    realities = product(realities, possible_solutions(remaining))
    newList = []
    for a in list(realities):
        used = set(chain(*a))
        player_cards = list(possible_player_cards(all_cards()-used, 6))
        for b in player_cards:
            sublist = list(a)
            sublist.append(b)
            sublist.append(tuple(all_cards() - used -set(b)))
            newList.append(sublist)
    return newList

def solution_sets(realities):
    solution_sets = set()
    for a in realities:
        solution_sets.add(frozenset(a[1]))
    return solution_sets

