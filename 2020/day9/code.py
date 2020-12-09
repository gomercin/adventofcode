import os, sys
import collections, itertools

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

numbers = collections.deque(maxlen=25)

def check(cur, q):
    perms = list(itertools.combinations(q, 2))
    for p in perms:
        if p[0] + p[1] == cur:
            return True
    return False

cnt = 0
all_nums = []
current_num=0
for line in input:
    line = line.strip()
    current_num = int(line.strip())
        
    if cnt > 25:
        if not check(current_num, numbers):
            print(current_num)
            break

    numbers.append(current_num)
    cnt += 1


all_nums = []
for line in input:
    line = line.strip()
    all_nums.append(int(line))


for i in range(len(all_nums) - 2):
    for j in range(i + 2, len(all_nums) -1):
        sub = all_nums[i:j]

        sum = 0
        for x in sub:
            sum+=x

        if sum == current_num:
            print(min(sub) + max(sub))
            exit(0)