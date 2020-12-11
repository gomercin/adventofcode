import os, sys, itertools

grid = {}
grid2 = {}
input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

imax = len(input)
jmax = 0
for i in range(imax):
    line = input[i].strip()

    jmax = len(line)
    for j in range(jmax):
        grid2[(i,j)] = grid[(i,j)] = line[j]

def is_occ(i, j):
    cell =  grid.get((i, j))
    if cell and cell == "#":
        return 1
    else:
        return 0

def is_occ_towards(i, j, di, dj):
    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix += di
        jx += dj
        cell = grid.get((ix,jx))

        if is_occ(ix, jx):
            return 1

        if cell and grid.get((ix, jx)) == "L":
            break
    
    return 0

def log(gr):
    for i in range(imax):
        str = ""
        for j in range(jmax):
            str += gr[(i,j)]
        print(str)
    print("\n\n")

dir_perms = [x for x in itertools.product([-1, 0, 1], [-1, 0, 1]) if x[0] or x[1]]

def occ_count_part2(i, j):
    occ = 0

    for p in dir_perms:
        occ += is_occ_towards(i, j, p[0], p[1])

    return occ

def occ_count_part1(i, j):
    perms = [x for x in itertools.product([i - 1, i, i + 1], [j - 1, j, j + 1])]
    perms.remove((i, j))
    return sum(list(map(lambda x: is_occ(x[0], x[1]), perms)))
    
def move(max_neighbors, check_func):
    for k, v in grid2.items():
        grid[k] = v

    # log(grid)
    changed = False
    for i in range(imax):
        for j in range(jmax):
            cur = grid[(i, j)]
            occ = check_func(i, j)

            if cur == "L" and occ == 0:
                grid2[(i, j)] = "#"
                changed = True
            elif cur == "#" and occ >= max_neighbors:
                grid2[(i, j)] = "L"
                changed = True
            else:
                grid2[(i, j)] = grid[(i, j)]

    return changed

def solve(max_neighbors, check_func):
    while move(max_neighbors, check_func):
        continue

    cnt = 0
    for i in range(imax):
        for j in range(jmax):
            if grid[(i, j)] == "#":
                cnt +=1

    print(cnt)

solve(4, occ_count_part1)
solve(5, occ_count_part2)