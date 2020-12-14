import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

mem = {}
def process1(mask, addr, val):
    zeromask = int(mask.replace("X", "1"), 2)
    onemask = int(mask.replace("X", "0"), 2)

    w = val & zeromask
    w = w | onemask

    mem[addr] = w

current_mask = ""
for line in input:
    line = line.strip()
    parts = line.split('=')
    left= parts[0].strip()
    right = parts[1].strip()

    if left == "mask":
        current_mask = right
    else:
        process1(current_mask, int(left[4:-1]), int(right))

s = 0
for v in mem.values():
    s+=v

print(s)


mem2= {}
def process2(mask, addr, val):
    addresses = []
    x_count = mask.count('X')

    masks = [i for i in range(2 ** x_count)]

    for m in masks:
        a = format(addr, 'b')
        a = a.zfill(36)

        xi = 0
        for i in range(len(a)):
            if mask[i] == "1":
                a = a[:i] + "1" + a[i + 1:]
            elif mask[i] == "X":
                mi = m
                mi = mi >> (x_count - xi - 1)
                mi = mi & 1

                a = a[:i] + str(mi) + a[i + 1:]
                xi += 1

        mem2[a] = val


current_mask = ""
for line in input:
    line = line.strip()
    parts = line.split('=')
    left= parts[0].strip()
    right = parts[1].strip()

    if left == "mask":
        current_mask = right
    else:
        process2(current_mask, int(left[4:-1]), int(right))

s = 0
for v in mem2.values():
    s+=v

print(s)