import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

input = []
alltext = ""
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

deck1 = []
deck2 = []
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
            deck1.append(int(line))
        else:
            deck2.append(int(line))

PLAYER1 = 1
PLAYER2 = 2
verbose = False

def combat(d1, d2, recursive):
    played_decs_in_current = set()
    while d1  and d2:
        d1key = ".".join(list(map(str, d1)))
        d2key = ".".join(list(map(str, d2)))
        key = d1key + "-" + d2key

        if verbose: print(d1)
        if verbose: print(d2)

        if key in played_decs_in_current:
            if verbose: print("duplicate game, player1 wins")
            return PLAYER1

        played_decs_in_current.add(key)

        card1 = d1.pop(0)
        card2 = d2.pop(0)

        if verbose: print(f"player1 plays {card1}, 2 plays {card2}")

        assert card1 != card2

        if recursive and card1 <= len(d1) and card2 <= len(d2):
            if verbose: print("starting subcombat")
            
            subwinner = combat(d1[:card1], d2[:card2], recursive)
            
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
    return PLAYER1 if d1 else PLAYER2

def play(d1, d2, recursive):
    winner = combat(d1, d2, recursive)
    res = d1 if winner == PLAYER1 else d2

    points = 0

    for i in range(len(res)):
        points += res[i] * (len(res) - i)

    print(points)

play(deck1[:], deck2[:], False) # p1
play(deck1[:], deck2[:], True) # p2