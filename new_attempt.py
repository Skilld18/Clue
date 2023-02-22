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

guess1 = [Person.Green, Weapon.Pipe, Room.Hall]
guess2 = [Person.Scarlett, Weapon.Pipe, Room.Kitchen]
guess3 = [Person.Plum, Weapon.Knife, Room.Dining]
guess4 = [Person.Green, Weapon.Wrench, Room.Lounge]
guess5 = [Person.Green, Weapon.Pipe, Room.Study]
guess6 = [Person.Plum, Weapon.Candlestick, Room.Library]
guess7 = [Person.White, Weapon.Rope, Room.Kitchen]
guess8 = [Person.Peacock, Weapon.Rope, Room.Hall]
guess9 = [Person.White, Weapon.Wrench, Room.Library]
guess10 = [Person.Green, Weapon.Pipe, Room.Billiard]
guess11 = [Person.Green, Weapon.Candlestick, Room.Billiard]
guess12 = [Person.Mustard, Weapon.Candlestick, Room.Dining]
guess13 = [Person.Green, Weapon.Knife, Room.Ballroom]
guess14 = [Person.Peacock, Weapon.Rope, Room.Study]
guess15 = [Person.Green, Weapon.Pipe, Room.Conservatory]


sc = [
    list(Room),
    list(Weapon),
    list(Person)
]

p11 = Person.Mustard
p12 = Room.Hall
p13 = Weapon.Candlestick
p1_list = [p11, p12, p13]

p1c = [
    [p11],
    [p12],
    [p13],
]
p2c = [
    [Room.Study],
    guess14,
    [Room.Conservatory],
]

p3c = [
    guess4,
    guess6,
    guess9,
]
p4c = [
    guess2,
]
p5c = [
    guess3,
    guess7,
    guess13,
]
p6c = [
    [Room.Billiard],
    guess11,
]

s_not = tuple([])
p2_not = tuple([*guess4, *guess9, *guess10])
p3_not = tuple([*guess1, *guess10, *guess11])
p4_not = tuple([*guess1, *guess10, *guess11, *guess12])
p5_not = tuple([*guess1, *guess10, *guess11, *guess12])
p6_not = tuple([*guess1, *guess8, *guess12, *guess14])

p6 = None
p5 = None
s = () 
count = 0

dex = 0
prob = dict()
print(len(list(player(p1_list + list(s_not), sc))))
for p1 in player([], p1c):
    for s in player(p1 + s_not, sc):
        dex += 1
        print(dex)
        for p2 in player(s + p1 + p2_not, p2c):
            for p3 in player(s + p1 + p2 + p3_not, p3c):
                for p4 in player(s + p1 + p2 + p3 + p4_not, p4c):
                    for p5 in player(s + p1 + p2 + p3 + p4 + p5_not, p5c):
                        for p6 in player(s + p1 + p2 + p3 + p4 + p5 + p6_not, p6c):
                            pass
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
                            if count % 1000000 == 0:
                                print(p1, s, p2, p3, p4, p5, p6)

for k in sorted(prob, key=prob.get, reverse=True):
    print((prob[k] / count).__format__("0.3f"), k)

    
                