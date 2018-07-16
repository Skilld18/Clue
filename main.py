import time
from card import *
import utils


def filter_possibilities(realities, tar, user_guess, res):
    if not type(res) is bool:
        return list(filter(lambda x: res & set(x[tar]), realities))
    return list(filter(lambda x: result == bool(user_guess & set(x[tar])), realities))


all_pos = list(all_possibilities([[utils.sample_player6()]], 3, 0))

while True:
    count = 0
    for a in all_pos:
        print(count, end=" ")
        print(a)
        count += 1
    # debug_print(all_pos)
    target = utils.parse("Target ", range(1,4))
    room = utils.parse("Room ", list(Room))
    weapon = utils.parse("Weapon ", list(Weapon))
    person = utils.parse("Person ", list(Person))
    result = utils.parse("Result", [{room}, {person}, {weapon}, False, True])

    all_pos = list(filter_possibilities(all_pos,
                                   target, {room, weapon, person},result))




