
input = [0,14,6,20,1,4]
#input = [0,3,6]

tlist = {x:[] for x in input}

last= -1
for i in range(30000000):
    #print(tlist)
    if i < len(input):
        last = input[i]
        tlist[last].append(i)
    else:
        if len(tlist[last]) == 1:
            last = 0
            tlist[0].append(i)
        else:
            last = tlist[last][-1] - tlist[last][-2]
            if last not in tlist:
                tlist[last] = []
            tlist[last].append(i)

    if i == 2019:
        # p1
        print(last)

# p2
print(last)

"""
when_spoken = {}
last = 0
was_first = True

for i in range(10):
    print(i, last, when_spoken)
    if i < len(input):
        cur = input[i]
        when_spoken[cur] = i
        last = cur
    else:
        if was_first:
            cur = 0
            when_spoken[0] = cur
            was_first = False
        else:
            cur = i - when_spoken[last] - 1
            was_first = cur not in when_spoken
            when_spoken[cur] = i

    last = cur
    print(cur)

"""


"""
prev = input[-1]
del tlist[prev]

turn = len(input)

while turn < 10:
    print(tlist)
    next=  0
    if prev in tlist:
        next = turn - tlist[prev] - 1
    else:
        next = 0

    tlist[prev] = turn 
    prev = next
    turn += 1
    print(prev)
"""