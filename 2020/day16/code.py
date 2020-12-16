import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

constraints = {}

i = 0
while True:
    valids = [0] * 1001
    line = input[i].strip()
    if not line:
        break

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

    constraints[parts[0].strip()] = valids
    i += 1


tickets = []
i += 2
while True:
    line = input[i].strip()
    if not line:
        break

    tickets.append(list(map(lambda x: int(x), line.split(','))))
    i += 1

result = 0
i += 2
while True:
    if i >= len(input):
        break
    line = input[i].strip()
    if not line:
        break

    tickets.append(list(map(lambda x: int(x), line.split(','))))
    
    i += 1

matches = []
to_remove = []

failed = False
for ticket in tickets:
    current_matches = [[] for _ in range(len(constraints))]
    failed = False
    for i,num in enumerate(ticket):
        for k,v in constraints.items():
            if v[num]:
                current_matches[i].append(k)

        if not current_matches[i]:
            result += num
            to_remove.append(ticket)
            failed = True
    
    if not failed:
        matches.append(current_matches) 

# part1
print(result)

for t in to_remove:
    tickets.remove(t)

correct = []
indexes = {k:-1 for k in constraints.keys()}
possibilities = {k:[] for k in constraints.keys()}
for i in range(len(constraints)):
    counts = {k:0 for k in constraints.keys()}
    for m in matches:
        for cs in m[i]:
            counts[cs] += 1

    for k, v in counts.items():
        if v == len(matches):
            possibilities[k].append(i)

while True:
    continue_checking = False
    for k, v in possibilities.items():
        if v:
            continue_checking = True
            break
    
    if not continue_checking: break

    #print(possibilities)
    from copy import deepcopy
    tmp = deepcopy(possibilities)
    for k, v in tmp.items():
        if len(v) == 1:
            indexes[k] = v[0]
            for k in possibilities.keys():
                if v[0] in possibilities[k]:
                    possibilities[k].remove(v[0])

res = 1

for k, v in indexes.items():
    if k.startswith("departure"):
        res *= tickets[0][v]

print(res)