import os, sys, re

lines = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    lines = in_file.readlines()

def partition(segment, min, max, min_ind):
    for ch in segment:
        if ch == min_ind:
            max = int((min + max) / 2)
        else:
            min += int((max - min) / 2) + 1

    return min

def parse_line(line):
    row = partition(line[0:7], 0, 127, 'F')
    col = partition(line[7:10], 0, 7, 'L')
    return 8 * row + col

all_nums = [x for x in range(0, (127 * 8 + 8))]
max_id = 0
for line in lines:
    x = parse_line(line)
    if x > max_id:
        max_id = x
    
    if x in all_nums:
        all_nums.remove(x)

print(max_id)

for i in range(1, len(all_nums) - 1):
    cur = all_nums[i]
    if all_nums[i - 1] != (cur - 1) and all_nums[i + 1] != (cur + 1):
        print(cur)
        exit(0)