import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

cube = set()

size = len(input)

for y, row in enumerate(input):
    for x, ch in enumerate(row.strip()):
        if ch == "#":
            cube.add((x, y, 0, 0))

smin = -1
smax = size

def active_count(x, y, z, w):
    n = [-1, 0, 1]
    cnt = 0
    for xd in n:
        xi = x + xd
        for yd in n:
            yi = y + yd
            for zd in n:
                zi = z + zd
                for wd in n:
                    wi = w + wd
                    if xd == 0 and yd == 0 and zd == 0 and wd == 0:
                        continue

                    if (xi, yi, zi, wi) in cube:
                        cnt += 1
    return cnt

def pc(c):
    for w in range(smin, smax):
        for z in range(smin, smax):
            print(f"z={z}")
            for y in range(smin, smax):
                row = ""
                for x in range(smin, smax):
                    if (x,y,z,w) in cube:
                        row += "#"
                    else:
                        row += "."
                print(row)
            print("")


def cycle():
    global cube
    tmp_cube = set()

    for x in range(smin, smax):
        for y in range(smin, smax):
            for z in range(smin, smax):
                for w in range(smin, smax):
                    active_neighbors = active_count(x, y, z, w)
                    if active_neighbors == 3: 
                        tmp_cube.add((x, y, z, w))
                    elif active_neighbors == 2:
                        if (x, y, z, w) in cube:
                            tmp_cube.add((x, y, z, w))

    cube = tmp_cube

for _ in range(6):
    cycle()
    smin -= 1
    smax += 1

print(len(cube))