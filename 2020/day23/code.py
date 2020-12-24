import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np
from collections import deque

VERBOSE=False
input= "962713854"
#input = "389125467"
P1= True

buffer = [int(x) for x in input]

bufferdict = {}
# store the buffer in a dictionary, like a linked list
# key current val, value: next val
for i in range(len(buffer) - 1):
    bufferdict[buffer[i]] = buffer[i + 1]

# assign the last one to first
bufferdict[buffer[-1]] = buffer[0]


def index(i):
    return i % len(input)

def rotate_buffer(buffer):
    return buffer[1:] + [buffer[0]]

def move(current):

    if VERBOSE: print(f"current: {current}")
    if VERBOSE: print(f"buffer: {bufferdict}")

    pick = [bufferdict[current]]
    for i in range(2):
        pick.append(bufferdict[pick[-1]])
        
    if VERBOSE: print(f"pick: {pick}")

    next = bufferdict[pick[-1]]
    bufferdict[current] = next

    destination = current - 1

    while destination in pick or destination < 1:
        destination -= 1
        if destination < 1:
            destination = 9 if P1 else 1000000

    if VERBOSE: print(f"next: {next}")

    nextnext = bufferdict[destination]
    bufferdict[destination] = pick[0]
    bufferdict[pick[2]] = nextnext

    return bufferdict[current]

current = buffer[0]
for i in range(100):
    if VERBOSE: print(f"move: {i + 1}")
    current = move(current)
    if VERBOSE: print()

while buffer[0] != 1:
    buffer = rotate_buffer(buffer)

print(bufferdict)
res = ""
start = bufferdict[1]
while start != 1:
    res += str(start)
    start = bufferdict[start]
    print(res)

print(res)

P1= False
input= "962713854"
# input = "389125467"

buffer = [int(x) for x in input]
for i in range(10, 1000001):
    buffer.append(i)

bufferdict = {}
# store the buffer in a dictionary, like a linked list
# key current val, value: next val
for i in range(len(buffer) - 1):
    bufferdict[buffer[i]] = buffer[i + 1]

# assign the last one to first
bufferdict[buffer[-1]] = buffer[0]

import signal
import sys

current_i = 0

def signal_handler(sig, frame):
    print(current_i)
signal.signal(signal.SIGINT, signal_handler)

current = buffer[0]
for i in range(10000000):
    current_i = i
    if VERBOSE: print(f"move: {i + 1}")
    current = move(current)
    if VERBOSE: print()


first = bufferdict[1]
second = bufferdict[first]

print(first, second)
print(first * second)