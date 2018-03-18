import utils


def filter_possibilities(realities, target, guess, result):
    realities[:] = list(filter(lambda possibility: result == bool(guess & possibility[target]), realities))


print(utils.guess())

