from collections.abc import MutableSet
import itertools
from card import *
from text_interface import construct_query, player_cards
import utils
from table import deal_with_pos

players = 3
player1 = player_cards()
print(player1)
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
#1

while True:
    player, query, card = construct_query()
    if card == 0:
        total = in_player_blind(query, player, total)
    elif card == 2:
        total = not_in_player(query, player, total)
    else:
        total = in_player(card, player, total)
    deal_with_pos(total)
