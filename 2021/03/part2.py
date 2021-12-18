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
    bit_size = len(input[0].strip())
    gamma=""
    epsilon=""

    ox_rating = 0
    co_rating = 0    
 
    print(bit_size)
    
    ox_list = list(input)
    co_list = list(input)


    for i in range(bit_size):
        ones_list = []
        zeros_list = []
        onecount = 0
        zerocount = 0
        for line in ox_list:
            line = line.strip()
            if line[i] == "0":
                zerocount+= 1
                zeros_list.append(line)
            else:
                onecount+=1
                ones_list.append(line)

        if onecount >= zerocount: 
            ox_list = list(ones_list)
        else: 
            ox_list = list(zeros_list)

        print(ox_list)

        if len(ox_list) == 1: break

    for i in range(bit_size):
        ones_list = []
        zeros_list = []
        onecount = 0
        zerocount = 0
        for line in co_list:
            line = line.strip()
            if line[i] == "0":
                zerocount+= 1
                zeros_list.append(line)
            else:
                onecount+=1
                ones_list.append(line)

        if zerocount <= onecount:
            co_list = list(zeros_list)
        else:
            co_list = list(ones_list)

        if len(co_list) == 1: break

    print(ox_list)
    print(co_list)
    gi = int(ox_list[0], 2)
    ei = int(co_list[0], 2) 

    print(gamma)
    print(epsilon)
    print(ei * gi)


part_1()
part_2()