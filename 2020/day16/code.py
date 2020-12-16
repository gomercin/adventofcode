import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


valids = [0] * 1000

i = 0
while True:
    line = input[i].strip()
    if not line:
        break

    print(line)
    parts = line.split(':')
    cs = parts[1].split('or')

    c1 = cs[0].split('-')
    c1_min = int(c1[0].strip())
    c1_max = int(c1[1].strip())

    c2 = cs[1].split('-')
    c2_min = int(c2[0].strip())
    c2_max = int(c2[1].strip())

    for x in range(c1_min, c1_max + 1):
        valids[x] = 1

    for x in range(c2_min, c2_max + 1):
        valids[x] = 1
    i += 1

i += 2
while True:
    line = input[i].strip()
    if not line:
        break
    
    print(line)
    i += 1

result = 0
i += 2
print(i)
while True:
    if i >= len(input):
        break
    line = input[i].strip()
    print(line)
    if not line:
        break
    print(line)
    parts = line.split(',')
    for p in parts:
        num = int(p.strip())
        if num >= len(valids):
            result += num
        else:
            if valids[num] != 1:
                result+=num
    i += 1


print(result)