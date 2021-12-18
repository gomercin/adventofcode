import os, sys
from itertools import permutations

# perm = permutations([1, 2, 3])

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()


hmap = {}

for y in range(len(input)):
    line = input[y].strip()

    for x in range(len(line)):
        hmap[(x,y)] = int(line[x])




def part_1():
    total = 0


    for key, val in hmap.items():
        x= key[0]
        y = key[1]

        u = hmap.get((x, y-1), 10)
        d = hmap.get((x, y+1), 10)
        l = hmap.get((x - 1, y), 10)
        r = hmap.get((x + 1, y), 10)

        c = val

        if c < u and c < d and c< l and c < r:
            total += (c+1)

    print(total)


def part_2():
    total = 0

    low_points = []

    for key, val in hmap.items():
        x= key[0]
        y = key[1]

        u = hmap.get((x, y-1), 10)
        d = hmap.get((x, y+1), 10)
        l = hmap.get((x - 1, y), 10)
        r = hmap.get((x + 1, y), 10)

        c = val

        if c < u and c < d and c< l and c < r:
            low_points.append(key)


    basin_sizes = []
    for lp in low_points:
        size = 1
        search_q = [lp]
        basin = [lp]

        while len(search_q ) > 0:
            c = search_q.pop(0)
            v = hmap.get(c)

            x= c[0]
            y = c[1]

            u = hmap.get((x, y-1), 10)
            d = hmap.get((x, y+1), 10)
            l = hmap.get((x - 1, y), 10)
            r = hmap.get((x + 1, y), 10)

            def checkappend(x, pos):
                if x <9:
                    if x > v:
                        search_q.append(pos)
                        if pos not in basin:
                            basin.append(pos)

            checkappend(u, (x, y-1))
            checkappend(d, (x, y+1))
            checkappend(l, (x - 1, y))
            checkappend(r, (x+1, y))

        print(basin)
        basin_sizes.append(len(basin))


    
    s = sorted(basin_sizes)
    print(s)
    print(s[-1] * s[-2] * s[-3])








part_1()
part_2()