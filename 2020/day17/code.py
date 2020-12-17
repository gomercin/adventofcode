import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

cube = {}

size = len(input)

for y, row in enumerate(input):
    for x, ch in enumerate(row.strip()):
        cube[(x, y, 0, 0)] = ch

new_cube = {}

smin = -1
smax = size

def active_count(x, y, z, w):
    n = [-1, 0 , 1]
    cnt = 0
    for xd  in n:
        xi = x + xd
        for yd in n:
            yi = y + yd
            for zd in n:
                zi = z + zd
                for wd in n:
                    wi = w + wd
                    if xd == 0 and yd == 0 and zd == 0 and wd == 0:
                        continue

                    neigh = cube.get((xi, yi, zi, wi))
                    if neigh == "#":
                        cnt += 1

    return cnt

def pc(c):
    for w in range(smin, smax):
        for z in range(smin, smax):
            print(f"z={z}")
            for y in range(smin, smax):
                row = ""
                for x in range(smin, smax):
                    c = cube.get((x,y,z,w))
                    if c:
                        row += c
                    else:
                        row += "."
                print(row)
            print("")


def cycle():
    global cube
    tmp_cube = {}

    count = 0
    for x in range(smin, smax):
        for y in range(smin, smax):
            for z in range(smin, smax):
                for w in range(smin, smax):
                    active_neighbors = active_count(x, y, z, w)
                    c = cube.get((x, y, z, w))
                    if active_neighbors == 3 or (c == '#' and active_neighbors == 2):
                        tmp_cube[(x, y, z, w)] = '#'
                        count += 1

    cube = tmp_cube
    return count

count = 0
for _ in range(6):
    count = cycle()
    smin -= 1
    smax += 1

print(count)