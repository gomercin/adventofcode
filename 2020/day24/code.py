import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

input = []
alltext = ""
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

WHITE = 0
BLACK = 1

grid = {}

move_dict_even_y = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, 1),
    "nw": (0, 1),
    "se": (1, -1),
    "sw": (0, -1)
}

move_dict_odd_y = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (0, 1),
    "nw": (-1, 1),
    "se": (0, -1),
    "sw": (-1, -1)
}


def flip_tile(ref):
    coords = []
    tmp = ""

    for ch in ref:
        if ch == "s" or ch == "n":
            tmp = ch
        elif tmp:
            tmp += ch
            coords.append(tmp)
            tmp = ""
        else:
            coords.append(ch)

    #print(coords)
    x = y = 0

    for c in coords:
        movedict = move_dict_odd_y if y % 2 else move_dict_even_y
        
        step = movedict[c]
        x += step[0]
        y += step[1]

        #print(x, y)
    if (x, y) not in grid:
        grid[(x, y)] = WHITE

    if grid[(x,y)] == WHITE:
        grid[(x,y)] = BLACK
    else:
        grid[(x,y)] = WHITE


for line in input:
    line = line.strip()
    flip_tile(line)


cnt = 0
cur_maxx = cur_maxy = -1000000000
cur_minx = cur_miny = 1000000000
for k, v in grid.items():
    if v == BLACK:
        cnt += 1
        cur_maxx = max(k[0], cur_maxx)
        cur_minx = min(k[0], cur_minx)
        cur_maxy = max(k[1], cur_maxy)
        cur_miny = min(k[1], cur_miny)
#p1
print(cnt)

def flipflop(gr, minx, maxx, miny, maxy):
    dirs = ['e', 'w', 'ne', 'nw', 'se', 'sw']

    new_maxx = new_maxy = -1000000000
    new_minx = new_miny = 1000000000
    tmpgrid = {}
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            movedict = move_dict_odd_y if y % 2 else move_dict_even_y
            current_color = WHITE
            if (x, y) in gr and gr[(x,y)] == BLACK:
                current_color = BLACK
            
            black_neighbor_count = 0
            for dir in dirs:
                step = movedict[dir]
                nx = x + step[0]
                ny = y + step[1]

                if (nx, ny) in gr and gr[(nx, ny)] == BLACK:
                    black_neighbor_count += 1

            next_color = current_color
            if current_color == BLACK and (black_neighbor_count == 0 or black_neighbor_count > 2):
                next_color = WHITE
            elif current_color == WHITE and black_neighbor_count == 2:
                next_color = BLACK

            if next_color == BLACK:
                tmpgrid[(x, y)] = BLACK

                new_minx = min(x, new_minx)
                new_miny = min(y, new_miny)
                new_maxx = max(x, new_maxx)
                new_maxy = max(y, new_maxy)

    return tmpgrid, new_minx, new_maxx, new_miny, new_maxy

for i in range(100):
    grid, cur_minx, cur_maxx, cur_miny, cur_maxy = flipflop(grid, cur_minx - 2, cur_maxx + 2, cur_miny - 2, cur_maxy + 2)

cnt = 0
for v in grid.values():
    if v == BLACK:
        cnt += 1

#p2
print(cnt)