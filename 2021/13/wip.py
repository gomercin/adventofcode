import os, sys
from collections import defaultdict

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

dots = defaultdict(int)
folds = []
for line in input:
    l = line.strip()
    if l:
        if line.startswith('fold'):
            ps = l.split()[2].split('=')
            folds.append((ps[0], int(ps[1])))
        else:
            print(l)
            x_y= l.split(',')
            x = int(x_y[0])
            y = int(x_y[1])
            dots[(x, y)] = 1

print(dots)
print(folds)



def part_1():
    orig = dots.copy()

    folded = orig.copy()
    for fold in folds:

        tobeadded = []
        toberemoved = []
        for k, v in folded.items():
            if fold[0] == 'x':
                if k[0] >= fold[1]:
                    new_x = fold[1] - (k[0] - fold[1])
                    tobeadded.append((new_x, k[1]))
                    toberemoved.append(k)
                    print(f"{k} becomes {(new_x, k[1])}")
            else:
                if k[1] >= fold[1]:
                    new_y = fold[1] - (k[1] - fold[1])
                    tobeadded.append((k[0], new_y))
                    toberemoved.append(k)
                    print(f"{k} becomes {(k[0], new_y)}")

        for x in tobeadded:
            folded[x] = 1

        for x in toberemoved:
            del folded[x]
        
        # part1:
        # break

    cnt = 0
    maxx = 0 
    maxy = 0
    for k, v in folded.items():
        if v == 1:
            cnt += 1 
        if k[0] > maxx: maxx = k[0]
        if k[1] > maxy: maxy = k[1]

    print(cnt)

    
    for y in range(maxy + 15):
        row = ""
        for x in range(maxx + 15):
            if (x, y) in folded:
                row += "#"
            else:
                row += "."
        
        print(row)



def part_2():
    pass


part_1()
part_2()