from card import *


def parse(msg, options):
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


def sample_player6():
    return Person.White, Person.Green, Room.Hall, Room.Library, Weapon.Knife, Weapon.Rope


def sample_player5():
    return Person.White, Person.Green, Room.Hall, Room.Library, Weapon.Knife


def sample_player4():
    return Person.White, Person.Green, Room.Hall, Room.Library


def sample_player3():
    return Person.White, Person.Green, Room.Hall


def remove_list(orig, rem):
    return [x for x in orig if x not in rem]


