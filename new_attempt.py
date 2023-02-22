import itertools

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
    pos= list(map(lambda x: tuple(sorted(set(x), key=str)), pos))
    pos = set(pos)
    pos = list(filter(lambda x: len(x) <= 3, pos))
    pos = list(filter(lambda x: not set(x) & set(not_list), pos))
    return pos


sc = [
    list(Room),
    list(Weapon),
    list(Person)
]

p11 = Person.Mustard
p12 = Weapon.Rope
p13 = Person.Scarlett
p1_list = [p11, p12, p13]

guess1 = [Person.White, Weapon.Revolver, Room.Library]

s_not = tuple([])
p2_not = tuple([])
p3_not = tuple([*guess1])
p4_not = tuple([])
p5_not = tuple([])
p6_not = tuple([])


p1c = [
    [p11],
    [p12],
    [p13],
]
p2c = [
    [Person.Green],
    [Room.Hall],
    [Weapon.Revolver],
]
p3c = [
]
p4c = [
    guess1,
]
p5c = [
]
p6c = [
]


s = () 
count = 0


prob = dict()
progress = 0
total_solutions = len(list(player(p1_list + list(s_not), sc)))
for p1 in player([], p1c):
    for s in player(p1 + s_not, sc):
        progress += 1
        print(int((progress/total_solutions)*100))
        for p2 in player(s + p1 + p2_not, p2c):
            for p3 in player(s + p1 + p2 + p3_not, p3c):
                for p4 in player(s + p1 + p2 + p3 + p4_not, p4c):
                    for p5 in player(s + p1 + p2 + p3 + p4 + p5_not, p5c):
                        for p6 in player(s + p1 + p2 + p3 + p4 + p5 + p6_not, p6c):
                            # if str(s[0]) not in prob:
                            #     prob[str(s[0])] = 0
                            # prob[str(s[0])] += 1
                            # if str(s[1]) not in prob:
                            #     prob[str(s[1])] = 0
                            # prob[str(s[1])] += 1
                            # if str(s[2]) not in prob:
                            #     prob[str(s[2])] = 0
                            # prob[str(s[2])] += 1
                            total_key = str(sorted([str(s[0]), str(s[1]),str(s[2])]))
                            if total_key not in prob:
                                prob[total_key] = 0
                            prob[total_key] += 1
                            count += 1

for k in sorted(prob, key=prob.get, reverse=True):
    print((prob[k] / count).__format__("0.3f"), k)

    
                