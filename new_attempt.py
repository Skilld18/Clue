import itertools

from card import *



#guess = (Person.White, Weapon.Knife, Room.Library)
def p1(known_cards):
    yield (Room.Ballroom, Room.Study, Weapon.Revolver)

#guess = (Person.Scarlett, Weapon.Rope, Room.Ballroom)
def p2(known_cards):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    res = list(filter(lambda x: Person.White in x, res))
    return res

#guess = (Person.White, Weapon.Pipe, Room.Conservator)
def p3(known_cards):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    res = list(filter(lambda x: Person.Scarlett in x or Weapon.Rope in x or Room.Ballroom in x, res))
    res = list(filter(lambda x: Person.Scarlett not in x and Weapon.Knife not in x and Room.Conservatory not in x, res))
    return res

#guess = (Person.Green, Weapon.Knife, Room.Library)
def p4(known_cards):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    res = list(filter(lambda x: Person.White in x or Weapon.Pipe in x or Room.Conservatory in x, res))
    return res

#guess = (Person.Green, Weapon.Revolver, Room.Library)
def p5(known_cards):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    res = list(filter(lambda x: Person.Green in x or Weapon.Knife in x and Room.Library in x, res))
    return res

def p6(known_cards):
    res = itertools.combinations(set(all_cards()) - set(known_cards), 3)
    res = list(filter(lambda x: Person.Green in x or Weapon.Revolver in x or Room.Library in x, res))
    return res
    
    
def sol(known_cards):
    for p in set(Person) - set(known_cards):
        for w in set(Weapon) - set(known_cards):
            for r in set(Room) - set(known_cards):
                yield (p, w, r)
 
count = 0               
for c1 in p1([]):
    for s1 in sol(c1):
        for c2 in p2(set(c1) | set(s1)):
            for c3 in p3(set(c1) | set(s1) | set(c2)):
                for c4 in p4(set(c1) | set(s1) | set(c2) | set(c3)):
                    for c5 in p5(set(c1) | set(s1) | set(c2) | set(c3) | set(c4)):
                        for c6 in p6(set(c1) | set(s1) | set(c2) | set(c3) | set(c4) | set(c5)):
                            if count % 10000 == 0:
                                print(c1, s1, c2, c3, c4, c5, c6)
                            count += 1
print(count)