import re, os, sys

lines = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    lines = in_file.readlines()

def check_line_part1(line):
    parts = re.split(': | |-', line)
    min = int(parts[0])
    max = int(parts[1])
    ch = parts[2]
    password = parts[3]

    char_count = password.count(ch)
    if char_count >= min and char_count <= max:
        return True
    
    return False

def check_line_part2(line):
    parts = re.split(': | |-', line)
    min = int(parts[0]) - 1
    max = int(parts[1]) - 1
    ch = parts[2]
    password = parts[3]

    at_first = password[min] == ch
    at_second = password[max] == ch

    return at_first != at_second

valid_cnt_1 = 0
valid_cnt_2 = 0
for line in lines:
    if check_line_part1(line):
        valid_cnt_1 += 1
    
    if check_line_part2(line):
        valid_cnt_2 += 1

print(valid_cnt_1)
print(valid_cnt_2)
