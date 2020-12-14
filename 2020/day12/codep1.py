import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

dirs = ["E", "N", "W", "S"]


cur_dir = 0
posx = 0
posy = 0
face = 0


mulx = 10
muly = 1


i_pos_x = 10
i_pos_y = 1

i_dir_x = 0
i_dir_y = 1

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
    iy = 0
    ix = 0

    if dir == "L":
        val = val / 90
        for i in range(int(val)):
            tmp = i_pos_x
            i_pos_x = -1 * i_pos_y
            i_pos_y = tmp

    elif dir =="R":
        val = val / 90
        for i in range(int(val)):
            tmp = i_pos_y
            i_pos_y = -1 * i_pos_x
            i_pos_x = tmp
        
    elif dir == "N":
        iy = val
    elif dir == "S":
        iy = -1 * val
    elif dir == "E":
        ix = val
    elif dir == "W":
        ix = -1 * val
    elif dir == "F":
        dx = val
        dy = val

        
    i_pos_x += ix
    i_pos_y += iy
    dx *= i_pos_x
    dy *= i_pos_y
    posx += dx
    posy += dy
    log()
    print("****")


print(abs(posx) + abs(posy))


