import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


def calcops(oplist):
    res =0 
    lastop = "+"
    for op in oplist:
        if op == "+":
            lastop = "+"
        elif op == "*":
            lastop = "*"
        else:
            if lastop == "*":
                res *= op
            else:
                res += op

    return res



def calculate(str):
    ops = []
    lastnum = 0

    for ch in str:
        if ch in "0123456789":
            ops.append(int(ch))
        elif ch == "*" or ch == "+" or ch == "(":
            ops.append(ch)
        elif ch == ")":
            subops = []
            prev = ops.pop()
            while prev != '(':
                subops.insert(0, prev)
                prev= ops.pop()

            res = calcops(subops)
            ops.append(res)

    return calcops(ops)


p1 = 0
for line in input:
    line = line.strip()
    res = calculate(line)
    print(res)
    p1 += res

print(p1)

