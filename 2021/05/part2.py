import os, sys
from collections import namedtuple

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()


Point = namedtuple("Point", "x,y")
Vent = namedtuple("Vents", "start, end")

vents = []

size = 10 if len(input) < 100 else 1000
floor = [[0] * size for i in range(size)]

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
    else:
        diffx = vent.end.x - vent.start.x
        diffy = vent.end.y - vent.start.y
        if (diffx < 0 and diffy < 0) or (diffx > 0 and diffy > 0):
            startx = min(vent.start.x, vent.end.x)
            endx = max(vent.start.x, vent.end.x)
            starty = min(vent.start.y, vent.end.y)
            endy = max(vent.start.y, vent.end.y)
            for x in range(0, abs(diffx) + 1):
                floor[startx + x][starty + x] += 1
        else:
            startx = min(vent.start.x, vent.end.x)
            endx = max(vent.start.x, vent.end.x)
            starty = min(vent.start.y, vent.end.y)
            endy = max(vent.start.y, vent.end.y)
            for x in range(0, abs(diffx) + 1):
                #print(vent)
                #print(startx + x, endy - x)
                floor[startx + x][endy - x] += 1
    vents.append(vent)


# print(vents)

def print_floor():
    for i in range(len(floor)):
        print(" ".join(list(map(str, floor[i]))))


def part_1():
    count = 0
    for x in range(len(floor)):
        for y in range(len(floor[0])):
            if floor[x][y] >1:
                count+=1

    print(count)
    # print_floor()


def part_2():
    pass



part_1()
part_2()