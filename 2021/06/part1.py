import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

fishes = list(map(int, input[0].split(',')))

print(fishes)
def part_1():
    new_fish_count = 0
    for _ in range(81): 
        for i in range(new_fish_count):
            fishes.append(8)
        new_fish_count = 0
        for i in range(len(fishes)):
            val = fishes[i]
            if val == 0:
                val = 6
                new_fish_count += 1
            else:
                val -= 1
            fishes[i] = val

    print(len(fishes))

def part_2():
    pass



part_1()
part_2()