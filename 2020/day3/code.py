import os, sys

lines = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    lines = in_file.readlines()

def calculate(row_inc, col_inc):
    tree_cnt = 0
    row = 0
    col = 0
    while row < len(lines):
        line = lines[row].strip() # argh; apparently readline also reads the "newline" char
        
        if line[col % len(line)] == '#':
            tree_cnt += 1

        row += row_inc
        col += col_inc

    return tree_cnt

tree_count = calculate(1, 3)
print(tree_count) # part 1

tree_count *= calculate(1, 1)
tree_count *= calculate(1, 5)
tree_count *= calculate(1, 7)
tree_count *= calculate(2, 1)


print(tree_count) # part 2
