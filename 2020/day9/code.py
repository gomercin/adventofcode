import os, sys
import collections, itertools
import time



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


start = time.time()

broken=False
for i in range(len(all_nums) - 2):
    cur_sum = all_nums[i]

    for j in range(i + 1, len(all_nums) -1):
        cur_sum += all_nums[j]
        if cur_sum == current_num:
            sub = all_nums[i:j]
            print(min(sub) + max(sub))
            exit(0)

        if cur_sum > current_num:
            break
