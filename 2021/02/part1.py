import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

# input_set = list(map(lambda x:int(x), input))

def part_1():
    x = 0
    d = 0

    for line in input:
        parts = line.split(        )
        if parts[0] == 'forward':
            x += int(parts[1])
        elif parts[0] == 'down':
            d += int(parts[1])
        else:
            d -= int(parts[1])

    print(x * d)

def part_2():
    pass



part_1()
part_2()