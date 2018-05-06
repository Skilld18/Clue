import time
from card import *
import utils


def filter_possibilities(realities, tar, user_guess, res):
    if not type(res) is bool:
        user_guess &= res
    return list(filter(lambda possibility: bool(res) == bool(user_guess & set(possibility[tar])), realities))


print("hello")
start = time.time()
all_pos = all_possibilities([[utils.sample_player6()]], 3, 0)
count = 0
for a in all_pos:
    print(a)
    count += 1
    print(count)
end = time.time()
print(end - start)
print("bye")

s = solution_sets(all_pos)
print(s)
print(len(s))
debug_print(all_pos)

guess = {Weapon.Revolver, Person.Plum, Room.Ballroom}
result = False
target = 2
all_pos = filter_possibilities(all_pos, target, guess, result)
debug_print(all_pos)


target = 3
result = {Room.Ballroom}
all_pos = filter_possibilities(all_pos, target, guess, result)
debug_print(all_pos)

