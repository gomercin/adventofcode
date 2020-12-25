import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

DOOR_PUBKEY = 10604480
CARD_PUBKEY = 4126658

#sample:
#DOOR_PUBKEY = 17807724
#CARD_PUBKEY = 5764801

subject_number = 7
value = 1

i = 0
loopsize_card = 0
loopsize_door = 0

while not loopsize_card or not loopsize_door:
    i += 1
    value *= subject_number
    value %= 20201227

    if value == DOOR_PUBKEY:
        loopsize_door = i
    elif value == CARD_PUBKEY:
        loopsize_card = i

print(loopsize_card)
print(loopsize_door)

subject_number = CARD_PUBKEY
value = 1
for i in range(loopsize_door):
    value *= subject_number
    value %= 20201227

print(value)