import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

input = []
alltext = ""
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

deck_1 = []
deck_2 = []
input.append("")
second = False
for line in input:
    line = line.strip()
    if "Player" in line:
        continue

    if not line:
        second=True
    else:
        if not second:
            deck_1.append(int(line))
        else:
            deck_2.append(int(line))

print(deck_1)
print(deck_2)
i = 0


while deck_1  and deck_2:
    i+=1
    card1 = deck_1.pop(0)
    card2 = deck_2.pop(0)

    assert card1 != card2
    print(card1, card2)
    if card1 > card2:
        deck_1.append(card1)
        deck_1.append(card2)
    else:
        deck_2.append(card2)
        deck_2.append(card1)

print(deck_1)
print(deck_2)

res = deck_1 if deck_1 else deck_2

points = 0

for i in range(len(res)):
    points += res[i] * (len(res) - i)

print(points)