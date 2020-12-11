import os, sys, copy

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
        grid[(i,j)] = line[j]
        grid2[(i,j)] = line[j]





def is_occ(i, j):
    cell =  grid.get((i, j))
    #print(cell)
    if cell and cell == "#":
        return 1
    else:
        return 0

def log(gr):
    for i in range(imax):
        str = ""
        for j in range(jmax):
            str += gr[(i,j)]

        print(str)

    print("\n\n")

    
def occ_count(i, j):
    occ = 0
    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix -= 1
        cell = grid.get((ix,jx))

        if is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix += 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        jx -= 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        jx += 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break



    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix -= 1
        jx -= 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix -= 1
        jx += 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix += 1
        jx += 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break


        if cell and grid.get((ix, jx)) == "L":
            break

    ix = i
    jx = j
    cell = grid.get((ix, jx))
    while cell:
        ix += 1
        jx -= 1
        cell = grid.get((ix,jx))

        if cell and is_occ(ix, jx):
            occ += 1
            break

        if cell and grid.get((ix, jx)) == "L":
            break



    return occ

def occ_count_(i, j):
    return is_occ(i-1, j-1) + is_occ(i-1, j) + is_occ(i-1, j+1) + \
           is_occ(i, j-1) + is_occ(i, j+1) +\
           is_occ(i+ 1, j-1) + is_occ(i+ 1, j)  + is_occ(i+ 1, j+1) 

def move():
    for k, v in grid2.items():
        grid[k] = v

    log(grid)
    changed = False
    for i in range(imax):
        for j in range(jmax):
            cur = grid[(i, j)]
            occ = occ_count(i, j)
            #print(occ)
            if cur == "L" and occ == 0:
                grid2[(i,j)] = "#"
                changed = True
            elif cur == "#" and occ >= 5:
                grid2[(i, j)] = "L"
                changed = True
            else:
                grid2[(i,j)] = grid[(i,j)]

    return changed


x = 0
while move():
    #print("rolling")
    continue


cnt = 0
for i in range(imax):
    for j in range(jmax):
        if grid[(i, j)] == "#":
            cnt +=1


print(cnt)