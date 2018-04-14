from enum import Enum
import utils
from itertools import product, combinations, chain
import math

Room = Enum('Room', 'Hall Lounge Dining Kitchen Ballroom Conservatory Billiard Library Study')
Person = Enum('Person', 'White Plum Scarlett Mustard Green Peacock')
Weapon = Enum('Weapon', 'Knife Candlestick Rope Pipe Wrench Revolver')

know_have = []
know_doesnt_have = []

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
        for card in player:
            cards.remove(card)
    return cards

def player_recurse(remaining, num_players):
    pass

def flatten(data):
    return chain(*data)


def all_possibilities(realities, num_players, current_player):
    if num_players == current_player:
        return

    used_card_count = 0
    for player in realities[0]:
        used_card_count += len(player)

    num_cards_for_player = math.ceil((21-used_card_count)/(num_players -current_player))
    new_realities = []

    for r in realities:
        remaining = remaining_cards(r)
        if not current_player:
            current_cards = possible_solutions(remaining)
        else:
            current_cards = list(possible_player_cards(remaining, num_cards_for_player))
        for i in current_cards:
            if current_player + 1 == num_players:
                test = [*r, i]
                yield test
            else:
                new_realities.append([*r, i])


    yield from all_possibilities(new_realities, num_players, current_player + 1)



def new_pos(player, totalPlayers):
    if player == 0:
        remaing = utils.remove_list(all_cards(), realities[0])
        realities = product(realities, possible_solutions(remaining))




def solution_sets(realities):
    solution_sets = set()
    for a in realities:
        solution_sets.add(frozenset(a[1]))
    return solution_sets

def debug_print(realities):
    chances = dict()
    totalSol = 0
    for pos in realities:
        for i, player in enumerate(pos):
            for card in player:
                if not str(i) + str(card) in chances:
                    chances[str(i) + str(card)] = 0
                chances[str(i) + str(card)] += 1
                if not str(i) in chances:
                    chances[str(i)] = 0
                chances[str(i)] += 1

    for pos in realities:
        if not str(1) + str(pos[1]) in chances:
            chances[str(1) + str(pos[1])] = 0
        chances[str(1) + str(pos[1])] += 1
        totalSol += 1

    for i,player in enumerate(realities[0]):
        for card in all_cards():
            if str(i) + str(card) in chances:
                print("Player " + str(i) + " has " + str(card) + " " + str(chances[str(i) + str(card)]/chances[str(i)] * len(realities[0][i])))
    
    room = None
    roomMax = 0
    weapon = None
    weaponMax = 0
    person = None
    personMax = 0
    for card in all_cards():
        if str(1) + str(card) in chances:
            cardCount = chances[str(1) + str(card)]
            if type(card) is Room and cardCount > roomMax:
                room = card
                roomMax = cardCount
            if type(card) is Weapon and cardCount > weaponMax:
                weapon = card
                weaponMax = cardCount
            if type(card) is Person and cardCount > personMax:
                person = card
                personMax = cardCount
    print("The most likely cards in the solution are")
    print(str(room) + " at " + str(chances[str(1) + str(room)]/chances[str(1)] * len(realities[0][1])))
    print(str(weapon) + " at " + str(chances[str(1) + str(weapon)]/chances[str(1)] * len(realities[0][1])))
    print(str(person) + " at " + str(chances[str(1) + str(person)]/chances[str(1)] * len(realities[0][1])))

    sol = None
    solMax = 0
    count = 0
    for pos in possible_solutions(all_cards()):
        if str(1) + str(pos) in chances:
            tmp = chances[str(1) + str(pos)]
            if tmp > solMax:
                solMax = tmp
                sol = pos


    print("The most likely solution set is: " + str(sol) + " at " + str(solMax/totalSol))




