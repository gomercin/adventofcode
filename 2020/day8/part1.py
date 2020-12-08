import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

acc = 0
pos = 0

visited = set()

while True:
    line = input[pos].strip()
    parts = line.split(" ")
    ins = parts[0]
    val = parts[1]

    mul = 1
    if val.startswith('-'):
        mul = -1

    val = mul * int(val[1:])

    if pos in visited:
        print(acc)
        exit(0)
    visited.add(pos)

    print(f"{ins}, {val}")
    if ins == "acc":
        acc += val
        pos += 1
    elif ins == "jmp":
        pos += val
    else:
        pos += 1
