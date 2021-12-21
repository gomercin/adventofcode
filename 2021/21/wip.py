import os, sys
from collections import defaultdict

p1 = 4
p2 = 10

dies = [x for x in range(1,101)] * 2
#print(dies)
di = 0

board = [x for x in range(1,10)]

s1 = 0
s2 = 0
rc = 0
def roll():
    global di, rc
    v = dies[di] + dies[di+1 ] + dies[di+2]
    #print(f"    roll: {dies[di]} + {dies[di+1 ]} + {dies[di+2]}")
    #print(f"    v: {v}")
    di += 3
    rc += 3
    if di > 99:
        di = di % 99
        di -=1

    return v

# 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 21

while True:
    v = roll()
    p1 += v
    if p1 %10 ==0: p1 = 10
    elif p1 > 10:
        p1 = p1 % 10

    
    s1 += p1
    #print(f"p1: {p1}, s1: {s1}")

    if s1 > 1000: 
        print(s2 * rc)
        break

    v = roll()
    p2 += v
    if p2 %10 ==0: p2 = 10
    elif p2 > 10:
        p2 = p2 % 10

    
    s2 += p2
    #print(f"p2: {p2}, s2: {s2}")

    if s2 > 1000: 
        print(s1 * rc)
        break


p2dies = [3,4,5,4,5,6,5,6,7,
          4,5,6,5,6,7,6,7,8,
          5,6,7,6,7,8,7,8,9]
p2dies = [3, 4, 4, 4, 5, 5, 5, 5, 5,
          5, 6, 6, 6, 6, 6, 6, 6, 7,
          7, 7, 7, 7, 7, 8, 8, 8, 9]


wincounts = {}
"""
irrespective of round count, player's current position and score
is enough to find in how many possibilities it will win from there
so we need a table for the combination of these 4?
can be max of size 10 * 10 * 21 * 21 (a bit more than 21 actually but whatever)

so keys as: p1, p2, s1, s2

"""

def wincount(op1, op2, os1, os2):
    # print(f"checking: {(op1, op2, os1, os2)}")
    if (op1, op2, os1, os2) in wincounts:
        return wincounts[(op1, op2, os1, os2)]

    current_win_counts = (0, 0)
    
    for v in p2dies:
        p1 = op1 + v
        if p1%10 == 0: p1 = 10
        elif p1 > 10:
            p1 = p1 % 10
        s1 = os1 + p1

        if s1 >= 21:
            current_win_counts = (current_win_counts[0] + 1, current_win_counts[1])
        else:
            for v2 in p2dies:
                p2 = op2 + v2
                if p2 %10 ==0: p2 = 10
                elif p2 > 10:
                    p2 = p2 % 10
                s2 = os2 + p2
                if s2 >= 21:
                    current_win_counts = (current_win_counts[0], current_win_counts[1] + 1)
                else:
                    sub_win_counts = wincount(p1, p2, s1, s2)
                    current_win_counts = (current_win_counts[0] + sub_win_counts[0], current_win_counts[1] + sub_win_counts[1])
    
    wincounts[(op1, op2, os1, os2)] = current_win_counts

    return current_win_counts

print(wincount(4, 10, 0, 0))






"""
3 -> 1
4 -> 3
5 -> 6
6 -> 7
7 -> 6
8 -> 3
9 -> 1
"""

"""
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10
"""


