import itertools

import text_interface
from card import *


def player(known_cards, known_constraints):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    for c in known_constraints:
        res = list(filter(lambda x: set(x) & set(c), res))
    return res


def sol(known_cards):
    for p in set(Person) - set(known_cards):
        for w in set(Weapon) - set(known_cards):
            for r in set(Room) - set(known_cards):
                yield p, w, r


def clean(not_list, pos):
    pos = list(map(lambda x: tuple(sorted(set(x), key=str)), pos))
    pos = set(pos)
    pos = list(filter(lambda x: len(x) <= 3, pos))
    pos = list(filter(lambda x: not set(x) & set(not_list), pos))
    return pos


sc = [
    list(Room),
    list(Weapon),
    list(Person)
]

s_not = tuple([])
p2_not = tuple([])
p3_not = tuple([])
p4_not = tuple([])
p5_not = tuple([])
p6_not = tuple([])

p1c = []
p2c = []
p3c = []
p4c = []
p5c = []
p6c = []

pc = [p1c, p2c, p3c, p4c, p5c, p6c]
p_not = [tuple([]), p2_not, p3_not, p4_not, p5_not, p6_not]
s = ()
count = 0

player_index, query, condition = text_interface.construct_query()
if condition == 2:
    p_not[player_index] = (*p_not[player_index], *query)
elif condition == 0:
    pc[player_index] = (*pc[player_index], *query)
else:
    pc[player_index] = (*pc[player_index], condition)

prob = dict()
progress = 0
for s in sol([]):
    total_key = str(sorted([str(s[0]), str(s[1]), str(s[2])]))
    prob[total_key] = 0

p1c = pc[0]
p2c = pc[1]
p3c = pc[2]
p4c = pc[3]
p5c = pc[4]
p6c = pc[5]

p2_not = p_not[1]
p3_not = p_not[2]
p4_not = p_not[3]
p5_not = p_not[4]
p6_not = p_not[5]

for i in all_cards():
    total_key = str(i)
    prob[total_key] = 0
total_solutions = len(list(player(p1c + list(s_not), sc)))
for p1 in player([], p1c):
    for s in sol(p1 + s_not):
        total_key = str(sorted([str(s[0]), str(s[1]), str(s[2])]))
        progress += 1
        print(int((progress / total_solutions) * 100))
        for p2 in player(s + p1 + p2_not, p2c):
            for p3 in player(s + p1 + p2 + p3_not, p3c):
                for p4 in player(s + p1 + p2 + p3 + p4_not, p4c):
                    for p5 in player(s + p1 + p2 + p3 + p4 + p5_not, p5c):
                        # for p6 in player(s + p1 + p2 + p3 + p4 + p5 + p6_not, p6c):
                        prob[str(s[0])] += 1
                        prob[str(s[1])] += 1
                        prob[str(s[2])] += 1
                        prob[total_key] += 1
                        count += 1

# for k in sorted(prob, key=prob.get, reverse=True):
    # print((prob[k] / count).__format__("0.3f"), k)
