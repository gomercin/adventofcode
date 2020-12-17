import os, sys

input = []
with open(os.path.join(sys.path[0], 'test'), 'r') as in_file:
    input = in_file.readlines()

cube = {}

size = len(input)

for y, row in enumerate(input):
    for x, ch in enumerate(row.strip()):
        cube[(x,y,0)] = ch

new_cube = {}

LIM = 20


def active_count(x, y, z):
    n = [-1, 0 , 1]
    cnt = 0
    for xd  in n:
        for yd in n:
            for zd in n:
                if xd ==0 and yd ==0 and zd ==0:
                    continue

                neigh = cube.get((x + xd, y + yd, z+zd))
                if neigh and neigh == "#":
                    cnt +=1

    return cnt

def pc(c):
    for z in range(-LIM, LIM):
        print(f"z={z}")
        for y in range(-LIM, LIM):
            row = ""
            for x in range(-LIM, LIM):
                c = cube.get((x,y,z))
                if c:
                    row += c
                else:
                    row += "."
            print(row)
        print("")


cycle_count = 0
def cycle():
    import copy
    global cube, cycle_count
    new_cube = copy.deepcopy(cube)

    for x in range(-LIM, LIM):
        for y in range(-LIM, LIM):
            for z in range(-LIM, LIM):
                active_neighbors = active_count(x, y, z)
                c= cube.get((x, y, z))
                if not c or c == '.':
                    if active_neighbors == 3:
                        new_cube[(x,y,z)] = '#'
                else:
                    if active_neighbors<2 or active_neighbors >3:
                        new_cube[(x,y,z)] = '.'

    cube = copy.deepcopy(new_cube)
    pc(cube)

for _ in range(6):
    cycle()

cnt = 0
for x in range(-LIM, LIM):
    for y in range(-LIM, LIM):
        for z in range(-LIM, LIM):
            c = cube.get((x,y,z))
            if c and c == '#':
                cnt +=1

print(cnt)