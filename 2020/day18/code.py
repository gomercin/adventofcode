import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()


def calcops_p1(oplist):
    """no precedence, calculate as you go"""
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

def getsum(mstr):
    ops = mstr.split('+')

    res = 0
    for op in ops:
        res += int(op)

    return res


def calcops_p2(oplist):
    """split by multiplications, find sum in each section, multiply results"""
    res = 1
    opstr = "".join(list(map(lambda x:str(x),oplist)))
    
    mults = opstr.split('*')

    for m in mults:
        res *= getsum(m)

    return res


def calculate(str, funcref):
    """split terms by paranthesis groups and manage overall calculation"""
    ops = []

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

            res = funcref(subops)
            ops.append(res)

    return funcref(ops)


p1 = 0
p2 = 0
for line in input:
    line = line.strip()
    p1 += calculate(line, calcops_p1)
    p2 += calculate(line, calcops_p2)

print(p1)
print(p2)

