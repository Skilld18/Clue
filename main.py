import utils
from card import *

def filter_possibilities(realities, target, guess, result):
    if not type(result) is bool:
        guess &= result
    return list(filter(lambda possibility: bool(result) == bool(guess & set(possibility[target])), realities))



startcards = utils.remove_list(all_cards(), utils.sample_player())
all = all_possibilities([utils.sample_player()], startcards, 3)

s = solution_sets(all)
print(s)
print(len(s))
debug_print(all)

guess = {Weapon.Revolver, Person.Plum, Room.Ballroom}
result = False
target = 2
all = filter_possibilities(all, target, guess, result)
s = solution_sets(all)
print(s)
print(len(s))
debug_print(all)


target = 3
all = filter_possibilities(all, target, guess, result)
s = solution_sets(all)
print(s)
print(len(s))
debug_print(all)

x = 23


# for a in all:
# if not Room.Ballroom in a[2]:
#     print("fail")
#     exit(1)
# if guess & set(a[2]):
#     print("fail")
#     exit(1)
# if not guess & set(a[2]):
#     print("fail")
#     exit(1)
