from card import *

def in_player(acc, player):
    for a in acc:
        if a in player:
            return True
    return False

def cards_per_player(players, player_index):
    if players == 4 and player_index <= 1:
        return 5
    if players == 5 and player_index <= 2:
        return 4
    return 18 // players

def parse(msg, options):
    ret = ""
    while True:
        print(msg)
        for i, opt in enumerate(options):
            print(str(i+1) + ". " + str(opt))
        try:
            ret = int(input(msg + ": "))
            if 1 > ret or ret > len(options):
                continue
        except ValueError:
            continue
        break
    return options[ret-1]


def guess():
    person = Person(parse("Person", Person))
    room = Room(parse("Room", Room))
    weapon = Weapon(parse("Weapon", Weapon))

    user_guess = (person, room, weapon)

    target = parse("Target", [1, 2, 3, 4, 5, 6]) - 1
    results = [True, False, *list(user_guess)]
    result = results[parse("Result", results) - 1]
    return user_guess, target, result

