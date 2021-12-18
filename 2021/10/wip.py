import os, sys
from itertools import permutations

# perm = permutations([1, 2, 3], 2)

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

m = {}
m['['] = ']'
m['{'] = '}'
m['('] = ')'
m['<'] = '>'

points = {}

points[']'] = 57
points['}'] = 1197
points['>'] = 25137
points[')'] = 3



p2 = {}

p2[']'] = 2
p2['}'] = 3
p2['>'] = 4
p2[')'] = 1


def part_1():
    total = 0

    for chunk in input:
        s= []
        for ch in chunk.strip():
            if ch in m:
                s.append(ch)
            else:
                n = s.pop()
                if m[n] == ch:
                    continue
                else:
                    # unmatching close char:
                    total += points[ch]
                    break

    print(total)



def part_2():
    
    totals = []
    incompletes = []
    for chunk in input:
        s= []
        corrupt = False
        for ch in chunk.strip():
            if ch in m:
                s.append(ch)
            else:
                n = s.pop()
                if m[n] == ch:
                    continue
                else:
                    print(f"breaking: {ch}, {n}, {s}")
                    # unmatching close char:
                    #total += points[ch]
                    corrupt = True
                    break

        print(corrupt, s)
        point = 0
        if not corrupt:
            while len(s) > 0:
                print("je")
                ch = s.pop()
                point *= 5
                point += p2[m[ch]]
            totals.append(point)

    print(totals)
    totals = sorted(totals)
    print(totals[len(totals)//2])


part_1()
part_2()