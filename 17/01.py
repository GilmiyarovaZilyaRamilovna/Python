import re

l = set()


def parrot(phrase):
    assert type(phrase) == str
    tempo = re.split(' |,|\?|\!', phrase)
    global l
    for i in tempo:
        if i in l:
            print(i)
        else:
            l.add(i)


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")

