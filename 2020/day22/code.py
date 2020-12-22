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
print(len(deck_1))
print(len(deck_2))

PLAYER1 = 1
PLAYER2 = 2
played_decks = [] # stack of  set() of gameids
lastd1 = None
lastd2 = None


lastc1 = 0
lastc2 = 0
firstsubcombat = False
verbose = False

def rec_combat(d1, d2):
    global firstsubcombat, lastc1, lastc2
    played_decs_in_current = set()
    winner = None
    while d1  and d2:
        d1key = ".".join(list(map(str, d1)))
        d2key = ".".join(list(map(str, d2)))
        key = d1key + "-" + d2key

        if verbose: print(d1)
        if verbose: print(d2)

        if key in played_decs_in_current:
            if verbose: print("duplicate game, player1 wins")
            return PLAYER1, True, d1, d2

        played_decs_in_current.add(key)

        card1 = d1.pop(0)
        card2 = d2.pop(0)

        if verbose: print(f"player1 plays {card1}, 2 plays {card2}")

        assert card1 != card2

        if card1 <= len(d1) and card2 <= len(d2):
            if verbose: print("starting subcombat")
            if firstsubcombat == False:
                    lastc1 = card1
                    lastc2 = card2
                    firstsubcombat = True
            subwinner, subinstakill, sd1, sd2 = rec_combat(d1[:card1], d2[:card2])
            #if subinstakill:
            #    print(f"player{subwinner} wins by instakill")
            #    d1.append(card1)
            #    d1.append(card2)
            #    return subwinner, True, d1, d2
            #else:
            if subwinner == PLAYER1:
                d1.append(card1)
                d1.append(card2)        
            else:
                d2.append(card2)
                d2.append(card1)
        else:
            if card1 > card2:
                d1.append(card1)
                d1.append(card2)
            else:
                d2.append(card2)
                d2.append(card1)

    if d1:
        if verbose: print("player1 wins the round")
    else:
        if verbose: print("player2 wins the round")
    return (PLAYER1, False, d1, d2) if d1 else (PLAYER2, False, d1, d2)

winner, _, c1, c2 = rec_combat(deck_1, deck_2)

res = deck_1 if winner == PLAYER1 else deck_2
#if c1 != -1:
#    res.append(c1)
#    res.append(c2)
print(res)
print(len(res))
print(deck_1)
print(deck_2)
print(len(deck_1))
print(len(deck_2))
print(lastc1, lastc2)

missings = []
for i in range(50):
    if (i+1) not in deck_1 and i+1 not in deck_2:
        print(f"doesn't exist: {i+1}")
        missings.append(i+1)
points = 0

print(res)
for i in range(len(res)):
    points += res[i] * (len(res) - i)

print(points)