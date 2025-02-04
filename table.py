from card import all_cards, all_solutions


def trim(s):
    return s.replace("Room.", "").replace("Weapon.", "").replace("Person.", "")

def deal_with_sol(total):
    print("test")

def deal_with_pos(total):
    for card in [''] + all_cards():
        print(trim(str(card)).ljust(14), end="")
    print()
    total_len = len(total)
    data = dict()
    sol_set = dict()
    for sol in all_solutions():
        sol_set[sol] = 0
    
    for player in range(-1, 3):
        for card in all_cards():
            data[player, card] = 0
    for pos in total:
        # player1
        for card in pos[0]:
            data[0, card] += 1
        # solution
        for card in pos[1]:
            data[-1, card] += 1
        # player2
        for card in pos[2]:
            data[1, card] += 1
        # player3
        for card in pos[3]:
            data[2, card] += 1
        sol_set[pos[1]] += 1

    print("Solution".ljust(14), end="")
    for card in all_cards():
        percent = data[-1, card] / total_len
        percent = round(percent, 3)
        print(str(percent).ljust(14), end="")
    print()
    for i in range(3):
        print(("Player" + str(i)).ljust(14), end="")
        for card in all_cards():
            percent = data[i, card] / total_len
            percent = round(percent, 2)
            print(str(percent).ljust(14), end="")
        print()
    print("Current Best solutions")
    canididates = {k: v for k, v in sorted(sol_set.items(), key=lambda item: item[1], reverse=True)}
    for i in range(10):
        key = list(canididates.keys())[i]
        print(str(round(canididates[key]/total_len,2)).ljust(6) +str(list(canididates.keys())[i]).ljust(50))
