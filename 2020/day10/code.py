import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

num_combs = {}

all_nums = []
for line in input:
    line = line.strip()
    all_nums.append(int(line))

all_nums.append(max(all_nums) + 3)
all_nums.sort()

current_jolt = 0
ones = 0
threes = 0
for num in all_nums:
    diff = num - current_jolt
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
    else:
        print(f"diff is {diff}")
    
    current_jolt = num

# part 1
print(ones * threes)    

def count(jolt, inp):
    cnt = 0

    if len(inp) == 1:
        return 1
    for i in range(3):
        if i == len(inp):
            break
        if inp[i] - jolt < 4:
            next= inp[i]
            if not num_combs.get(inp[i+1]):
                num_combs[inp[i+1]] = count(next, inp[i + 1: ])

            cnt += num_combs[inp[i+1]]
        else:
            break

    return cnt

x = count(0, all_nums)
# part 2
print(x)