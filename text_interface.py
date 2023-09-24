#!/usr/bin/python

import card


def get_card(card_type):
    for i, c, in enumerate(card_type):
        print(i + 1, c)
    return card_type(int(input("Card: ")))


def get_room():
    return get_card(card.Room)


def get_person():
    return get_card(card.Person)


def get_weapon():
    return get_card(card.Weapon)


def get_player():
    return int(input("Player: "))


def get_condition(query):
    ans = int(input("0.Has\n1.Has specific\n2.Doesn't have"))
    if ans == 1:
        for i, c in enumerate(query):
            print(i, c)
        card_index = int(input("Which card: "))
        return query[card_index]
    return int(ans)


def construct_query():
    person = get_person()
    room = get_room()
    weapon = get_weapon()
    player = get_player()
    cond = get_condition((person, weapon, room))
    return player, (person, room, weapon), cond

# player_index, query, condition = text_interface.construct_query()
# if condition == 2:
#     p_not[player_index] = (*p_not[player_index], *query)
# elif condition == 0:
#     pc[player_index] = (*pc[player_index], *query)
# else:
#     pc[player_index] = (*pc[player_index], condition)
