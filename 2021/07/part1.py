import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

ps = list(map(int, input[0].split(',')))

costs = [0] * len(ps)
print(costs)

distances = {}

def part_1():
    m = 9999999999999999999
    for i in range(max(ps)+1):
        total = 0
        for j in range(len(ps)):
            # hepsini ps[i]'ye goturmeye calisirsak ne olur
            c= abs(ps[j] - i)

            total += ((c * (c+1)) // 2)

        if total < m:
            m = total

        # print(total)

    print(m)




def part_2():
    pass



part_1()
part_2()


