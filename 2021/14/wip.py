import os, sys
from collections import defaultdict

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

start = list(input[0].strip())
M = {}
M2 = {}
print(start)
for i in range(2, len(input)):
    parts = input[i].strip().split('->')
    k = tuple(list(parts[0].strip()))
    v = parts[1].strip()
    print(k, v)
    M[k] = v


def part_1():
    orig = start[:]
    tmp = orig[:]

    ins_count = 0
    for i in range(4):
        print(i)
        orig = tmp[:]
        tmp = []

        for x in range(len(orig) - 1):
            tmp.append(orig[x])
            k = (orig[x], orig[x+1])
            if k in M:
                tmp.append(M[k])
                ins_count += 1
                print(f"inserting {M[k]} because {k}")

        
        tmp.append(orig[-1])

    orig = tmp[:]
    char_counts = defaultdict(int)

    for ch in orig:
        char_counts[ch] += 1

    max_count = 0
    min_count = 999999999999999999999999999
    for k,v in char_counts.items():
        if v > max_count:
            max_count = v
        elif v < min_count:
            min_count = v

    print(f"ins count {ins_count}")
    print(max_count - min_count)



def part_2():

    pair_counts = defaultdict(int)
    ins_count = 0
    for x in range(len(start) - 1):
        pair_counts[(start[x], start[x+1])] += 1
        #print((start[x], start[x+1]))

    #print(pair_counts)
    for i in range(40):
        print(i)
        new_items = defaultdict(int)
        olds = defaultdict(int)
        for p, v in pair_counts.items():
            if pair_counts[p] > 0:
                #print("icinde")
                # print(f"inserting {M[p]} because {p}")

                new_items[(p[0], M[p])] += v
                new_items[(M[p], p[1])] += v
                olds[p] += v
                ins_count += 1

        for x, v in new_items.items():
            pair_counts[x] += v

        for x, v in olds.items():
            pair_counts[x] -= v

        
    #print(f"ins count {ins_count}")


    char_counts = defaultdict(int)

    for k, v in pair_counts.items():
        char_counts[k[0]] += v
        char_counts[k[1]] += v

    counts = defaultdict(int)
    for c, v in char_counts.items():

        count = v
        if c == start[0] or c == start[-1]:
            count += 1

        count = count // 2
        counts[c] = count

    max_count = 0
    min_count = 999999999999999999999999999
    for k,v in counts.items():
        if v > max_count:
            max_count = v
        elif v < min_count:
            min_count = v

    print(max_count - min_count)

part_1()
from time import time
begin = time()
part_2()
end = time()
print(end-begin)