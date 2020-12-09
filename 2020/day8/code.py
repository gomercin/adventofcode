import os, sys
from copy import deepcopy

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

JMP = "jmp"
NOP = "nop"
ACC = "acc"
FINISHED = 0
LOOP = 1
OUT_OF_BOUNDS = 2
class Instruction:
    def __init__(self, inp):
        parts = inp.strip().split(" ")
        self.opcode = parts[0]
        val = parts[1]

        mul = 1
        if val.startswith('-'):
            mul = -1

        val = mul * int(val[1:])
        self.val = val

    def __str__(self):
        return f"{self.opcode} {self.val}"

class Machine:
    def __init__(self, input):
        self.instructions = []
        self.visited = set()
        self.acc_val = 0
        self.pos = 0

        for line in input:
            self.instructions.append(Instruction(line))

    def run(self, start_pos=0, start_val=0):
        self.reset()
        self.pos = start_pos
        self.acc_val = start_val
        while True:
            if self.pos == len(self.instructions):
                return FINISHED

            if self.pos > len(self.instructions):
                return OUT_OF_BOUNDS

            if self.pos in self.visited:
                return LOOP

            ins = self.instructions[self.pos]
            
            self.visited.add(self.pos)

            if ins.opcode == ACC:
                self.acc_val += ins.val
                self.pos += 1
            elif ins.opcode == JMP:
                self.pos += ins.val
            else:
                self.pos += 1

    def switch_ins(self, switch_pos, ins1, ins2):
        switched = False
        if self.instructions[switch_pos].opcode == ins1:
            self.instructions[switch_pos].opcode = ins2
            switched = True
        elif self.instructions[switch_pos].opcode == ins2:
            self.instructions[switch_pos].opcode = ins1
            switched = True
        
        return switched

    def reset(self):
        self.visited = set()
        self.acc_val = 0
        self.pos = 0

machine = Machine(input)
machine.run()
print("day 8/1:")
print(machine.acc_val)

for switch_pos in range(len(input)):
    # print(switch_pos)
    if not machine.switch_ins(switch_pos, JMP, NOP):
        # no need to run if no switch was made
        continue

    if machine.run() == FINISHED:
        print("day 8/2:")
        print(machine.acc_val)
        machine.switch_ins(switch_pos, JMP, NOP) # not needed, just for demos below
        break
    else:
        # undo the switch
        machine.switch_ins(switch_pos, JMP, NOP)


# from which instruction it should start to reach value 50000
for i in range(len(input)):
    res = machine.run(i)
    if res == FINISHED and machine.acc_val == 50000:
        print("day 9/1:")
        print(res)
        break

# which instruction to remove to make it halt
for i in range(len(input)):
    copymac = deepcopy(machine)

    copymac.instructions.pop(i)
    if copymac.run() == FINISHED:
        print("day 9/2:")
        print(i)
        print(copymac.acc_val)
        