import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

class Instruction:
    JMP = "jmp"
    NOP = "nop"
    ACC = "acc"
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
    FINISHED = 0
    LOOP = 1
    OUT_OF_BOUNDS = 2

    def __init__(self, input):
        self.instructions = []
        self.visited = set()
        self.acc_val = 0
        self.pos = 0

        for line in input:
            self.instructions.append(Instruction(line))

    def run(self):
        self.reset()
        while True:
            if self.pos == len(self.instructions):
                return Machine.FINISHED

            if self.pos > len(self.instructions):
                return Machine.OUT_OF_BOUNDS

            if self.pos in self.visited:
                return Machine.LOOP

            ins = self.instructions[self.pos]
            
            self.visited.add(self.pos)

            if ins.opcode == Instruction.ACC:
                self.acc_val += ins.val
                self.pos += 1
            elif ins.opcode == Instruction.JMP:
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
# part1
print(machine.acc_val)

for switch_pos in range(len(input)):
    # print(switch_pos)
    if not machine.switch_ins(switch_pos, Instruction.JMP, Instruction.NOP):
        # no need to run if no switch was made
        continue

    if machine.run() == Machine.FINISHED:
        print(machine.acc_val)
        break
    else:
        # undo the switch
        machine.switch_ins(switch_pos, Instruction.JMP, Instruction.NOP)
