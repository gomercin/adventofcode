import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np
from collections import deque

VERBOSE=False
input= "962713854"
#input = "389125467"

buffer = [int(x) for x in input]

def index(i):
    return i % len(input)

def rotate_buffer(buffer):
    return buffer[1:] + [buffer[0]]

def move(buffer, current):
    if VERBOSE: print(f"current: {current}")
    if VERBOSE: print(f"buffer: {buffer}")
    pick = buffer[1:4]

    for p in pick:
        buffer.remove(p)

    if VERBOSE: print(f"pick: {pick}")

    next = current - 1
    nextindex = -1

    while next not in buffer:
        if next == 0:
            next = 10
        next -= 1

    nextindex = index(buffer.index(next) + 1)
    if VERBOSE: print(f"next: {next}")

    for pn in reversed(pick):
        buffer.insert(nextindex, pn)

    return buffer[1], buffer

current = buffer[0]
for i in range(100):
    if VERBOSE: print(f"move: {i + 1}")
    while buffer[0] != current:
        buffer = rotate_buffer(buffer)
    current, buffer = move(buffer, current)
    if VERBOSE: print()

while buffer[0] != 1:
    buffer = rotate_buffer(buffer)


print("".join([str(x) for x in buffer][1:]))