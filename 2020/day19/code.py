import os, sys

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

rules = []
messages = []

reading_rules = True


for line in input:
    line = line.strip()

    if not line:
        reading_rules = False
        continue

    if reading_rules:
        rules.append(line)
    else:
        messages.append(line)


rule_map_p1 = {}
rule_map_p2 = {}

class Rule:
    def __init__(self, id, char=None, ruledef=None, part=1):
        self.id = id
        self.char = char
        self.ruledef = ruledef
        self.rules = []
        self.part = part
        if self.ruledef:
            self.parse()

    def __str__(self):
        return f"{self.id}, {self.char}, {self.rules}"

    def parse(self):
        if self.part == 2 and self.id == 8:
            for i in range(1, 10):
                self.rules.append([42] * i)
        elif self.part == 2 and self.id == 11:
            # 11: 42 31 | 42 11 31
            for i in range(1, 10):
                self.rules.append([42] * i + [31] * i)
        else:
            subrules_str = self.ruledef.split('|')

            for sub_str in subrules_str:
                nexts_str = sub_str.split()
                subrules = []
                for n in nexts_str:
                    n = n.strip()
                    subrules.append(int(n))

                self.rules.append(subrules)

    def isvalid(self, msg, potential_is, depth):
        depth += 1
        current_map = rule_map_p1 if self.part == 1 else rule_map_p2
        # indent = '  ' * depth
        # print(f"{indent}checking {msg}, for rule{self.id}, for potentials: {potential_is}")
        all_potentials = []
        for i in potential_is:
            if i >= len(msg):
                continue
            # ababbb, 0
            if self.char:
                if msg[i] == self.char:
                    # print("it held : " + self.char)
                    all_potentials.append(i + 1)
            else:
                for ruleset in self.rules:

                    subpotentials = [i]
                    newpotentials = []
                    # print(ruleset)
                    for rule in ruleset:
                        # print(f"{indent} subpotentials " + str(subpotentials))
                        for si in subpotentials:
                            res, rule_is = current_map[rule].isvalid(msg, [si], depth)
                            # print(f"{indent} rules_is : {rule_is}")
                            if res:
                                newpotentials.extend(rule_is)

                        subpotentials = newpotentials
                        newpotentials = []

                    all_potentials.extend(subpotentials)
                    

        # print(f"{indent} {all_potentials}")
            # print(f"{'failed' if failed else 'success'} {msg[i:]}, for rule{self.id}, rem: {msg[current_i:]}")
        return len(all_potentials) > 0, all_potentials


for r in rules:
    id, ruledef = r.split(":")
    
    rule1 = None
    rule2 = None
    if '"' in ruledef:
        rule1 = Rule(int(id.strip()), char = ruledef.strip().replace('"', ""), part=1)
        rule2 = Rule(int(id.strip()), char = ruledef.strip().replace('"', ""), part=2)
    else:
        rule1 = Rule(int(id.strip()), ruledef=ruledef, part=1)
        rule2 = Rule(int(id.strip()), ruledef=ruledef, part=2)

    rule_map_p1[rule1.id] = rule1
    rule_map_p2[rule2.id] = rule2

cnt_p1 = 0
cnt_p2 = 0
for msg in messages:
    res, i = rule_map_p1[0].isvalid(msg, [0], 0)
    if res and i[0] == len(msg):
        cnt_p1 += 1

    res, i = rule_map_p2[0].isvalid(msg, [0], 0)
    if res and i[0] == len(msg):
        cnt_p2 += 1


print(cnt_p1)
print(cnt_p2)