import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

input_set = list(map(lambda x:int(x), input))

def part_1():
    prev_x = 999999999999999999
    inc = 0
    for x in input_set:
        if x > prev_x:
            inc +=1

        prev_x = x

    print(inc)


def part_2():
    prev = 99999999999999999999999999
    prevs = []

    i = 0
    inc = 0
    for x in input_set:
        prevs.append(x)
        if len(prevs) == 4:
            del prevs[0]

        if len(prevs) < 3: continue
        c = sum(prevs)

        if c > prev:
            inc += 1

        prev = c
    print(inc)



part_1()
part_2()