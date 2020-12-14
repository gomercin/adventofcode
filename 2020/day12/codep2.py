import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


"""
  0, 1
-1, 0  0, 1
  0, -1  

"""

dirs = ["E", "N", "W", "S"]


cur_dir = 0
posx = 0
posy = 0
face = 0

def log():
    print(f"{posx}, {posy}, {cur_dir}")

for line in input:
    print(line)
    log()
    line = line.strip()

    dir = line[0]
    val = int(line[1:])
    dx = 0
    dy = 0

    if dir == "L":
        val = val / 90
        cur_dir += val
        # print(f"L1 : {cur_dir}")
        cur_dir %= 4
        # print(f"L2 : {cur_dir}")
    elif dir =="R":
        val = val / 90
        cur_dir -= val
        # print(f"R1 : {cur_dir}")
        cur_dir %= 4
        print(f"R2 : {cur_dir}")
        
    elif dir == "N":
        dy = val
    elif dir == "S":
        dy = -1 * val
    elif dir == "E":
        dx = val
    elif dir == "W":
        dx = -1 * val
    elif dir == "F":
        c = dirs[int(cur_dir)]
        # print(c)
        # print(val)
        if c == "N":
            dy = val
        elif c == "S":
            dy = -1 * val
        elif c == "E":
            dx = val
        elif c == "W":
            dx = -1 * val

        # print(dx)
        # print(dy)

    elif dir == "R":
        c = dirs[int(cur_dir)]
        if c == "N":
            dy = -1 * val
        elif c == "S":
            dy = val
        elif c == "E":
            dx = -1 *val
        elif c == "W":
            dx = val

    posx += dx
    posy += dy


print(abs(posx) + abs(posy))


