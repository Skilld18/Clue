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

p1c = [
    [Person.Peacock],
    [Room.Conservatory],
    [Room.Hall],
]
p2c = [
    [Person.Peacock, Weapon.Rope, Room.Billiard],
    [Person.Peacock, Weapon.Revolver, Room.Kitchen],
    [Person.Scarlett, Weapon.Knife, Room.Dining],
    [Person.White, Weapon.Wrench, Room.Kitchen],
]

p3c = [
    [Person.White, Weapon.Pipe, Room.Library],
    [Person.White, Weapon.Revolver, Room.Hall],
    [Person.Peacock, Weapon.Rope, Room.Dining],
    [Person.Peacock, Weapon.Rope, Room.Hall],

]
p4c = [
    [Weapon.Revolver],
    [Person.Mustard, Weapon.Knife, Room.Dining],
]
p5c = [
    [Person.Green, Weapon.Pipe, Room.Ballroom],
]
p6c = [
    [Person.Green, Weapon.Candlestick, Room.Library],
    [Person.Plum, Weapon.Pipe, Room.Study],
    [Person.Plum, Weapon.Rope, Room.Study],
]



p2_not = tuple([Person.Peacock, Weapon.Rope, Room.Dining, Person.Peacock, Weapon.Rope, Room.Dining])
p3_not = tuple([Person.Plum, Weapon.Pipe, Room.Study])
p4_not = tuple([Person.Plum, Weapon.Pipe, Room.Study])
p5_not = tuple([Person.Peacock, Weapon.Rope, Room.Billiard, Person.Green, Weapon.Candlestick, Room.Library, Person.Plum, Weapon.Pipe, Room.Study, Person.Plum, Weapon.Rope, Room.Study])
p6_not = tuple([Person.Peacock, Weapon.Rope, Room.Billiard, Person.Peacock, Weapon.Revolver, Room.Kitchen, Person.Green, Weapon.Pipe, Room.Ballroom, Person.Peacock, Weapon.Rope, Room.Dining])

p6 = None
p5 = None
s = () 
count = 0

dex = 0
prob = dict()
print(len(list(player([Person.Peacock, Room.Conservatory, Room.Hall, Weapon.Revolver], sc))))
for p1 in player([], p1c):
    for s in player([Person.Peacock, Room.Conservatory, Room.Hall, Weapon.Revolver], sc):
        dex += 1
        print(dex)
        for p2 in player(s + p1 + p2_not, p2c):
            for p3 in player(s + p1 + p2 + p3_not, p3c):
                for p4 in player(s + p1 + p2 + p3 + p4_not, p4c):
                    for p5 in player(s + p1 + p2 + p3 + p4 + p5_not, p5c):
                        for p6 in player(s + p1 + p2 + p3 + p4 + p5 + p6_not, p6c):
                            if str(s[0]) not in prob:
                                prob[str(s[0])] = 0
                            prob[str(s[0])] += 1
                            if str(s[1]) not in prob:
                                prob[str(s[1])] = 0
                            prob[str(s[1])] += 1
                            if str(s[2]) not in prob:
                                prob[str(s[2])] = 0
                            prob[str(s[2])] += 1
                            total_key = str(sorted([str(s[0]), str(s[1]),str(s[2])]))
                            if total_key not in prob:
                                prob[total_key] = 0
                            prob[total_key] += 1

                            count += 1
                            if count % 1000000 == 0:
                                print(p1, s, p2, p3, p4, p5, p6)
                                # for p6 in player(s + p1 + p2 + p3 + p4 + p5, p6c):

for k in sorted(prob, key=prob.get, reverse=True):
    print((prob[k] / count).__format__("0.3f"), k)

    
                