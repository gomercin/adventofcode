import os, sys
from collections import defaultdict
from itertools import permutations

# input_set = list(map(lambda x:int(x), input))

input = "target area: x=70..96, y=-179..-124"
# input = "target area: x=20..30, y=-10..-5"

parts = input.strip().split()
xs = parts[2]
ys = parts[3]

xs = xs[2:-1].split('..')
x0 = int(xs[0])
x1 = int(xs[1])

ys = ys[2:].split('..')
y0 = int(ys[0])
y1 = int(ys[1])

print(x0, x1, y0, y1)

def shoot(vx, vy):
    px = 0
    py = 0
    maxy = -9999999999999999
    hit = False
    while px < x1 and py > y0:
        # print(px, py)
        px += vx
        py += vy

        if py > maxy:
            maxy = py

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        
        vy -= 1
        if px >= x0 and px <= x1 and py <= y1 and py >= y0:
            break

    if px >= x0 and px <= x1 and py <= y1 and py >= y0:
        # print(f"hit at: {px}, {py}")
        hit = True
            


    return hit, maxy


def part_1():
    #print(shoot(7, -1))
    # return
    mmaxy = -999999999999999
    hits = set()
    for x in range(1000):
        for y in range(-1000, 1000):
            # print(f"shooting with {(x,y)}")
            hit, maxy = shoot(x, y)
            if hit:
                hits.add((x, y))
                if maxy > mmaxy:
                    mmaxy = maxy
    print(mmaxy)

    print(hits)
    print(len(hits))

    with open(os.path.join(sys.path[0], 'output'), 'r') as in_file:
        input = in_file.readlines()
        refset = set()
        for line in input:
            line = line.strip()
            if line:
                parts = line.split(',')
                x= int(parts[0])
                y = int(parts[1])
                refset.add((x,y))

    
        # print(refset.difference(hits))
    


def part_2():
    pass



part_1()
part_2()