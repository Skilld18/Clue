import itertools
from card import *
import utils
from table import deal_with_pos

players = 3
player1 = (Person.Plum, Weapon.Revolver, Weapon.Wrench, Room.Conservatory, Room.Ballroom, Room.Dining)
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

def in_player(card, player, total):
    return list(filter(lambda x: card in x[player], total))

def not_in_player(cards, player, total):
    return list(filter(lambda x: cards[0] not in x[player] and cards[1] not in x[player] and cards[2] not in x[player], total))

def in_player_blind(cards, player, total):
    return list(filter(lambda x: cards[0] in x[player] or cards[1] in x[player] or cards[2] in x[player], total))

# total = not_in_player((Person.Peacock, Weapon.Revolver, Room.Hall),2, total)
# total = in_player_blind((Person.Peacock, Weapon.Revolver, Room.Hall), 3, total)
# total = in_player(Room.Hall, 2, total)
total = in_player_blind((Person.Plum, Weapon.Revolver, Room.Library), 3, total)
total = in_player(Person.White, 2, total)
total = in_player_blind((Person.Peacock, Weapon.Pipe, Room.Billiard), 3, total)
total = in_player(Room.Lounge, 2, total)
total = in_player_blind((Person.Green, Weapon.Knife, Room.Ballroom), 3, total)
total = in_player(Weapon.Candlestick, 2, total)
total = in_player_blind((Person.Peacock, Weapon.Knife, Room.Dining), 3, total)
total = in_player_blind((Person.Mustard, Weapon.Rope, Room.Lounge), 3, total)
total = in_player(Person.Scarlett , 2, total)
total = in_player_blind((Person.Peacock, Weapon.Pipe, Room.Hall), 3, total)
total = not_in_player((Person.Green, Weapon.Pipe, Room.Billiard), 2, total)
total = in_player(Room.Billiard, 3, total)
total = not_in_player((Person.Green, Weapon.Pipe, Room.Hall), 2, total)
total = in_player(Room.Hall, 3, total)
total = not_in_player((Person.Green, Weapon.Revolver, Room.Study), 3, total)
total = in_player_blind((Person.Green, Weapon.Pipe, Room.Library), 3, total)
total = in_player_blind((Person.Green, Weapon.Candlestick, Room.Lounge), 2, total)
#high percentage and correct










# 2 has green rope terrace
deal_with_pos(total)
