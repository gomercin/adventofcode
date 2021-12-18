import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

# input_set = list(map(lambda x:int(x), input))

def part_1():
    bit_size = len(input[0].strip())
    gamma=""
    epsilon=""
 
    print(bit_size)
    
    for i in range(bit_size):
        onecount = 0
        zerocount = 0
        for line in input:
            line = line.strip()
            if line[bit_size - i -1] == "0":
                zerocount+= 1
            else:
                onecount+=1

        if onecount > zerocount:
            gamma = "1" + gamma
            epsilon = "0" + epsilon
        else:
            gamma = "0" + gamma
            epsilon = "1" + epsilon


    gi = int(gamma, 2)
    ei = int(epsilon, 2)

    print(gamma)
    print(epsilon)
    print(ei * gi)


 
def part_2():
    pass

part_1()
part_2()