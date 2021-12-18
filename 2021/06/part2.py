import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

all_fishes = list(map(int, input[0].split(',')))

#print(fishes)

counts = {}
for fish in all_fishes:
    if fish not in counts:
        counts[fish] = 0

    counts[fish] += 1

print(counts)
def part_1():

    total = 0
    for key, value in counts.items():
        fishes = [5]
        print(fishes)
        new_fish_count = 0

        for day in range(257):
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

            print(f"{day}, {len(fishes)}")

        total += (len(fishes) * value)
        print(f"total for key {key}: {total}")
    print(total)

def part_2():
    pass



part_1()
part_2()