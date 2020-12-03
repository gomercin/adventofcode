import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

input_set = set(map(lambda x:int(x), input))

def part_1():
    for x in input_set:
        rem = 2020 - x
        if rem in input_set:
            print(rem * x)
            return


def part_2():
    ref_set = set(input_set)

    for x in input_set:
        ref_set.remove(x)
        rem = 2020 - x

        for y in ref_set:
            rem_2 = rem - y
            if rem_2 in ref_set:
                print(x * y * rem_2)
                return

part_1()
part_2()