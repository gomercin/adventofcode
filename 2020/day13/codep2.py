import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


dep_time = int(input[0].strip())
parts = input[1].strip().split(',')

diffs = {}
busses = []
nums = []
max_bus = 0
for id in parts:
    if id != 'x':
        busses.append(int(id))    
        bus = int(id)
        nums.append(bus)
        if bus > max_bus:
            max_bus = bus
        diffs[bus] = dep_time % bus

        if diffs[bus] == 0:
            print(0)
            exit(0)

    else:
        busses.append("x")

max_bus = max(nums)
nums.remove(max_bus)
max2_bus = max(nums)
nums.remove(max2_bus)
max3_bus = max(nums)

indexmax3 = busses.index(max3_bus)
indexmax2 = busses.index(max2_bus)
indexmax = busses.index(max_bus)
print(max_bus)
print(max2_bus)

start = max_bus - max2_bus

d= max_bus - max2_bus
it = 0

starti = 0
for i in range(max_bus - indexmax, 100000000000, max_bus):
    if i == 0: continue
    # if (i % max_bus) != indexmax: continue
    if i % max2_bus == (max2_bus - indexmax2) % max2_bus:
        starti = i
        break

print(starti)

def check(timestamp):
    for i in range(len(busses)):
        bus = busses[i]
        if bus == "x":
            continue
        if timestamp % bus != (bus - i) % bus:
            return False

    return True

import signal
import sys

i = starti

def signal_handler(sig, frame):
    print(i)
signal.signal(signal.SIGINT, signal_handler)

mult = max2_bus * max_bus

print(mult)
# this will take a while :)
while True:

    if check(i):
        print(i)
        exit(0)

    i+= mult

