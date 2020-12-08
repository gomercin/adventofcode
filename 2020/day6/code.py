import os, sys, string

lines = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    lines = in_file.readlines()

def parse(acc):
    inp = "".join(acc).replace("\n", "").replace(" ", "")
    anss = set([x for x in inp])
    return len(anss)

def parse2(acc):
    counts = {x:0 for x in string.ascii_lowercase}
    num_lines = len(acc)
    inp = "".join(acc).replace("\n", "").replace(" ", "")
    for ch in inp:
        counts[ch] += 1

    res = 0
    for v in counts.values():
        if v == num_lines:
            res += 1

    return res

num_yes = 0
num_yes2 = 0
acc_lines = []
for line in lines:
    line = line.strip()
    if not line:
        num_yes += parse(acc_lines)
        num_yes2 += parse2(acc_lines)
        acc_lines = []
    else:
        acc_lines.append(line)

num_yes += parse(acc_lines)
num_yes2 += parse2(acc_lines)
print(num_yes)
print(num_yes2)
