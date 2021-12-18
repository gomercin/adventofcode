import os, sys
import math

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

"""
sn = [num, num]
     [sn, num]
     [num, sn]
"""

class SNumber:
    def __init__(self, s=None, parent=None, left=None, right=None):
        # print(f"parsing {s}")
        self.left = left
        self.right = right
        self.val = None
        self.parent = parent

        if left:
            assert right is not None
            assert parent is None
            self.left.parent = self
            self.right.parent = self
        elif ',' not in s:
            # Note: this is not actually an snumber!
            self.val = int(s)
        else:
            s = s[1:-1]

            # find split point:
            pcount = 0
            leftpart = ""
            rightpart = ""
            for i, ch in enumerate(s):
                if ch == '[':
                    pcount += 1
                elif ch == ']':
                    pcount -= 1
                elif ch == ',':
                    if pcount == 0:
                        # this should be the split point;
                        leftpart = s[:i]
                        rightpart = s[i+1:]
                else:
                    val = int(ch)
                
            self.left = SNumber(s=leftpart, parent=self)
            self.right = SNumber(s=rightpart, parent=self)

    def parent_count(self):
        if self.parent:
            return 1 + self.parent.parent_count()
        else:
            return 0

    def __str__(self):
        res = ""
        if self.val is not None:
            res = str(self.val)
        else:
            res = f"[{self.left}, {self.right}]"

        return res

    def split(self):
        leftval = self.val // 2
        rightval = int(math.ceil(self.val / 2))
        self.val = None
        self.left =SNumber(s=f'{leftval}', parent=self)
        self.right =SNumber(s=f'{rightval}', parent=self)

    def findleftbro(self):
        cur = self

        while True:
            par = cur.parent
            if not par:
                return None
            if cur == par.left:
                cur = par
            else:
                cur = par
                break

        cur = cur.left
        # now find rightmost child
        while cur.val is None:
            cur = cur.right

        return cur

    def findrightbro(self):
        cur = self

        while True:
            par = cur.parent
            if not par:
                return None
            if cur == par.right:
                cur = par
            else:
                cur = par
                break

        cur = cur.right
        # now find rightmost child
        while cur.val is None:
            cur = cur.left

        return cur

    def explode(self):
        leftbro = self.findleftbro()
        rightbro = self.findrightbro()

        if leftbro:
            #print(f"ik: {self} en mijne lieve leftbro: {leftbro}")
            leftbro.val += self.left.val
        if rightbro:
            #print(f"ik: {self} en mijne lieve rightbro: {rightbro}")
            rightbro.val += self.right.val

        self.val = 0
        self.left = None
        self.right = None

    def reduce(self):
        if self.val is not None:
            # can't reduce numbers
            if self.val > 9:
                self.split()
                return True
        else:
            # this should max out at 4
            assert self.parent_count() <= 4
            if self.parent_count() == 4:
                self.explode()
                return True

        leftreduce = False
        rightreduce = False
        if self.left:
            leftreduce = self.left.reduce()
        if self.right:
            rightreduce = self.right.reduce()
        
        return leftreduce or rightreduce

    def mapexplode(self):
        #print(f"ik ben {self}")
        if self.val is None:
            if self.right.val is not None and self.left.val is not None:
                #print(f"en ik heb schattige kinderen")
                if self.parent_count() >= 4:
                    self.explode()
                    return True
                # else:
                    # print(f"maar niet genoeg parents")
            lex = self.left.mapexplode()
            if lex: return True
            rex = self.right.mapexplode()
            if rex: return True

        return False

    def mapsplit(self):
        if self.val is not None:
            if self.val > 9:
                self.split()
                return True
        else:
            ls = self.left.mapsplit()
            if ls: return True
            rs = self.right.mapsplit()
            if rs: return True

        return False

    def magnitude(self):
        if self.val is not None:
            return self.val
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def add(left, right):
    # !! Not reduced
    return SNumber(left=left, right=right)

def reduce(snum):
    reduced = True
    while reduced:
        # print("reducing")
        # print(snum)
        exploded = snum.mapexplode()
        if exploded:
            # print(f"after explode:\t{snum}")
            continue
        splitted = snum.mapsplit()
        # if splitted: print(f"after split:\t{snum}")
        reduced = exploded or splitted


def part_1():
    nums = []
    for line in input:
        nums.append(SNumber(s=line.strip()))
    
    total = nums[0]

    for i in range(1, len(nums)):
        # print(f"adding {i}")
        total = add(total, nums[i])
        # print(total)
        reduce(total)

    print(total)
    print(total.magnitude())

    #x = SNumber(s="[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
    # print(x.magnitude())

def part_2():
    lines = []
    for line in input:
        lines.append(line.strip())
    max = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            if (i != j):
                n1 = SNumber(s=lines[i].strip())
                n2 = SNumber(s=lines[j].strip())
                s = add(n1, n2)
                reduce(s)
                
                #print(s.magnitude())
                if s.magnitude() > max:
                    max = s.magnitude()
    """
    from itertools import permutations
    perms = permutations(nums, 2)

    for p in perms:
        s = add(p[0], p[1])
        print(p[0])
        print(p[1])
        print(s)
        print(f"bef: {s.magnitude()}")
        reduce(s)
        print(s)
        print(f"aft: {s.magnitude()}")
        m = s.magnitude()
        if m > max: max = m
    """
    print(max)


h1 = SNumber(s='[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]')
h2 = SNumber(s='[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')
s = add(h1, h2)
reduce(s)
print(s)

h = SNumber(s='[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]')
print(h.magnitude())

part_1()
part_2()
