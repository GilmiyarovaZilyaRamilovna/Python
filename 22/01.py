import random


def make_bingo():
    x = random.sample(range(1, 100), 24)
    x.insert(12, 0)
    return tuple(tuple(x[i:i + 5]) for i in [0, 5, 10, 15, 20])


print(make_bingo())