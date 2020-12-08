import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

acc = 0
pos = 0

visited = set()

changed_ins = -1

ins_set = []
def convert():
    for line in input:
        line = line.strip()
        parts = line.split(" ")
        ins = parts[0]
        val = parts[1]

        mul = 1
        if val.startswith('-'):
            mul = -1

        val = mul * int(val[1:])

        ins_set.append([ins, val])

def switch_ins(x):
    print(x)
    if ins_set[x][0] == "jmp":
        ins_set[x][0] = "nop"
    else:
        ins_set[x][0] = "jmp"

convert()
while True:

    if changed_ins >= 0:
        switch_ins(changed_ins)

    changed_ins += 1
    while (changed_ins < len(ins_set)):
        if ins_set[changed_ins][0]         == "jmp" or ins_set[changed_ins][0] == "nop":
            switch_ins(changed_ins)
            break
        changed_ins +=1

    pos = 0
    acc = 0
    visited = set()

    print(ins_set)
    while True:
        if pos == len(ins_set):
            print(acc)
            exit(0)

        if pos > len(ins_set):
            print("too far")
            break

        if pos in visited:
            print("loop")
            break

        ins_t = ins_set[pos]
        ins = ins_t[0]
        val = ins_t[1]
        visited.add(pos)

        # print(f"{ins}, {val}")
        if ins == "acc":
            acc += val
            pos += 1
        elif ins == "jmp":
            pos += val
        else:
            pos += 1
