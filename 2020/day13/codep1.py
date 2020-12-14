import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


dep_time = int(input[0].strip())
parts = input[1].strip().split(',')

diffs = {}
busses = []
for id in parts:
    busses.append(int(id))
    if id != 'x':
        bus = int(id)
        diffs[bus] = dep_time % bus

        if diffs[bus] == 0:
            print(0)
            exit(0)

next_times = []

current_min = 1000000000

mink = 0
minw = 0
for k,v in diffs.items():
    if k - v < current_min:
        current_min = k - v
        mink = k
        minw = v

print(mink * current_min)

