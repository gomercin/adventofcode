import os, sys
from collections import defaultdict

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

algo = list(input[0].strip())

image = defaultdict(int)

maxrow = 0
maxcol = 0
for row, line in enumerate(input[2:]):
    line = line.strip()
    maxrow = row + 1
    maxcol = len(line)
    for col, ch in enumerate(list(line)):
        image[(col, row)] = 0 if ch == '.' else 1
       
        

def part_1():
    global image
    enhanced = defaultdict(int)
    primage()

    outside = 0

    for _ in range(2):
        for x in range(-10, maxcol + 10):
            for y in range(-10, maxrow + 10):
                num = 0
                for yi in [y-1, y, y+1]:
                    for xi in [x-1, x, x+1]:
                        px = image.get((xi, yi), outside)
                        num = ((num << 1) | px)

                enhanced[(x,y)] = 0 if algo[num] == '.' else 1

        outside = 0 if outside else 1

        image = enhanced.copy()
        primage()



    res = sum(image.values())
    print(res)


def primage():
    for y in range(-10, maxrow + 10):
        line = ""
        for x in range(-10, maxcol + 10):
            p = image[(x,y)]
            line += ("#" if p else ".")
        print(line)

    print("")
    print("")
    print("")
        

def part_2():
    global image
    enhanced = defaultdict(int)
    primage()

    outside = 0

    for _ in range(50):
        for x in range(-150, maxcol + 150):
            for y in range(-150, maxrow + 150):
                num = 0
                for yi in [y-1, y, y+1]:
                    for xi in [x-1, x, x+1]:
                        px = image.get((xi, yi), outside)
                        num = ((num << 1) | px)

                enhanced[(x,y)] = 0 if algo[num] == '.' else 1

        outside = 0 if outside else 1

        image = enhanced.copy()
        #primage()



    res = sum(image.values())
    print(res)




part_1()
part_2()