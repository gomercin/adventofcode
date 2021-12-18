import os, sys
from itertools import permutations

# perm = permutations([1, 2, 3], 2)

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

# input_set = list(map(lambda x:int(x), input))

grid = {}

for y in range(len(input)):
    row = input[y].strip()

    for x in range(len(row)):
        n = int(row[x])
        grid[(x,y)] = n


def log():
    for y in range(len(input)):
        row = input[y].strip()
        r = ""
        for x in range(len(row)):
            r += f" {grid[(x, y)]}"
        
        print(r)

log()

def get_neighbors(k):
    n = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0: continue
            if (k[0] + x, k[1] + y) in grid:
                n.append((k[0] + x, k[1] + y))
    return n

def part_1():
    # parlayanlari eksi yap
    count = 0
    for i in range(100):
        flash_q = []

        for k, v in grid.items():
            grid[k] = v + 1

        
        while True:
            one_exploded = False
            for k, v in grid.items():
                if v > 9:
                    neighbors = get_neighbors(k)
                    grid[k] = -1
                    count += 1
                    one_exploded = True
                    for n in neighbors:
                        if grid[n] > 0:
                            grid[n] += 1

            if not one_exploded:
                break



        
        for k, v in grid.items():
            if v < 0:
                grid[k] = 0

        print("")
        log()
    
    print(count)



def part_2():
    # parlayanlari eksi yap
    count = 0
    day = 0
    while True:
        day += 1
        flash_q = []

        for k, v in grid.items():
            grid[k] = v + 1

        explosions = set()
        while True:
            one_exploded = False
            for k, v in grid.items():
                if v > 9:
                    neighbors = get_neighbors(k)
                    grid[k] = -1
                    count += 1
                    explosions.add(k)
                    one_exploded = True
                    for n in neighbors:
                        if grid[n] > 0:
                            grid[n] += 1

            if not one_exploded:
                break


        if len(explosions) == 100:
            print(day)
            return(0)
        
        for k, v in grid.items():
            if v < 0:
                grid[k] = 0

        print(f"day: {day}")
        log()
    
    print(count)



# part_1()
part_2()