import itertools
from card import *
import utils
from table import deal_with_pos

players = 3
player1 = (Person.Plum, Person.Scarlett, Weapon.Pipe, Weapon.Revolver, Room.Hall, Room.Conservatory)
valid_card_set = set(all_cards()) - set(player1)

possible_solutions = filter(lambda x: x[0] not in player1 and x[1] not in player1 and x[2] not in player1,
                            all_solutions())

total = []

player2 = []
for solution in possible_solutions:
    valid_card_set = set(all_cards()) - set(player1) - set(solution)
    player2pos = itertools.combinations(valid_card_set, utils.cards_per_player(players, 1))
    for pos in player2pos:
        player3 = set(all_cards()) - set(solution) - set(pos) - set(player1)
        player3 = tuple(player3)
        total.append((player1, solution, pos, player3))

# total = list(filter(lambda x: Weapon.Wrench in x[1], total))
total = list(filter(lambda x: Weapon.Rope in x[2], total))
total = list(filter(lambda x: Person.White not in x[3] and Room.Hall not in x[3] and Weapon.Wrench not in x[3], total))
total = list(filter(lambda x: Room.Kitchen in x[3], total))
total = list(
    filter(lambda x: Person.White not in x[2] and Room.Kitchen not in x[2] and Weapon.Wrench not in x[2], total))
total = list(
    filter(lambda x: Person.Plum not in x[3] and Room.Library not in x[3] and Weapon.Revolver not in x[3], total))
total = list(filter(lambda x: Room.Dining in x[2], total))
total = list(filter(lambda x: Room.Billiard in x[3] or Weapon.Wrench in x[3] or Person.Mustard in x[3], total))
total = list(filter(lambda x: Room.Ballroom in x[2] or Weapon.Knife in x[2] or Person.White in x[2], total))
total = list(filter(lambda x: Room.Ballroom in x[2] or Weapon.Knife in x[2] or Person.White in x[2], total))
total = list(filter(lambda x: Room.Conservatory in x[3] or Weapon.Pipe in x[3] or Person.Mustard in x[3], total))

# 2 has green rope terrace
deal_with_pos(total)
