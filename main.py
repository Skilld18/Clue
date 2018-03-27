import utils
from card import *

def filter_possibilities(realities, target, guess, result):
    if not type(result) is bool:
        guess &= result
    return list(filter(lambda possibility: bool(result) == bool(guess & set(possibility[target])), realities))




all = all_possibilities([utils.sample_player()], all_cards()-set(utils.sample_player()),3)
s = solution_sets(all)
print(s)
print(len(s))

guess = {Weapon.Revolver, Person.Plum, Room.Ballroom}
result = False
target = 2
all = filter_possibilities(all, target, guess, result)
s = solution_sets(all)
print(s)
print(len(s))


target = 3
all = filter_possibilities(all, target, guess, result)
s = solution_sets(all)
print(s)
print(len(s))

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
