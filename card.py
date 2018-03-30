from enum import Enum
import utils
from itertools import product, combinations, chain
import math

Room = Enum('Room', 'Hall Lounge Dining Kitchen Ballroom Conservatory Billiard Library Study')
Person = Enum('Person', 'White Plum Scarlett Mustard Green Peacock')
Weapon = Enum('Weapon', 'Knife Candlestick Rope Pipe Wrench Revolver')

def all_cards():
    return list(Room) + list(Person) + list(Weapon)


def possible_solutions(cards):
    r = []
    w = []
    p = []
    for card in cards:
        if type(card) is Room:
            r.append(card)
        if type(card) is Weapon:
            w.append(card)
        if type(card) is Person:
            p.append(card)
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
        used = list(chain(*a))
        rem = utils.remove_list(all_cards(), used)
        player_cards = list(possible_player_cards(rem, 6))
        for b in player_cards:
            sublist = list(a)
            sublist.append(b)
            rem = utils.remove_list(all_cards(), used)
            rem = utils.remove_list(rem, b)
            sublist.append(tuple(rem))
            newList.append(sublist)
    return newList

def solution_sets(realities):
    solution_sets = set()
    for a in realities:
        solution_sets.add(frozenset(a[1]))
    return solution_sets

def debug_print(realities):
    chances = dict()
    for pos in realities:
        for i, player in enumerate(pos):
            for card in player:
                if not str(i) + str(card) in chances:
                    chances[str(i) + str(card)] = 0
                chances[str(i) + str(card)] += 1
                if not str(i) in chances:
                    chances[str(i)] = 0
                chances[str(i)] += 1
    for i,player in enumerate(realities[0]):
        for card in all_cards():
            if str(i) + str(card) in chances:
                print("Player " + str(i) + " has " + str(card) + " " + str(chances[str(i) + str(card)]/chances[str(i)] * len(realities[0][i])))









