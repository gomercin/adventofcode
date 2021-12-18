import os, sys
from collections import namedtuple

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()


Point = namedtuple("Point", "x,y")
Vent = namedtuple("Vents", "start, end")

vents = []


floor = [[0] * 1000 for i in range(1000)]

for line in input:
    parts = line.strip().split('->')
    beginparts = list(map(int, parts[0].split(',')))
    endparts = list(map(int, parts[1].split(',')))

    start_point = Point(beginparts[0], beginparts[1])
    end_point = Point(endparts[0], endparts[1])

    vent = Vent(start_point, end_point)
    if (vent.start.x == vent.end.x) or (vent.start.y == vent.end.y):
        startx = min(vent.start.x, vent.end.x)
        endx = max(vent.start.x, vent.end.x)
        starty = min(vent.start.y, vent.end.y)
        endy = max(vent.start.y, vent.end.y)
        for x in range(startx, endx + 1):
            for y in range(starty, endy + 1):
                floor[x][y] += 1
    vents.append(vent)


# print(vents)


def part_1():
    count = 0
    for x in range(len(floor)):
        for y in range(len(floor[0])):
            if floor[x][y] >1:
                count+=1

    print(count)



def part_2():
    pass



part_1()
part_2()