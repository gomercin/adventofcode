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


rule_map = {}

class Rule:
    def __init__(self, id, char=None, ruledef=None):
        self.id = id
        self.char = char
        self.ruledef = ruledef
        self.rules = []
        if self.ruledef:
            self.parse()

    def __str__(self):
        return f"{self.id}, {self.char}, {self.rules}"

    def parse(self):
        if self.id == 8:
            for i in range(1, 10):
                self.rules.append([42] * i)
        elif self.id == 11:
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

    def get_variations(self):
        if self.char:
            return [self.char]
        
        subvars = []

        for subrule in self.rules:
            for id in subrule:
                subvars.append(rule_map[id].get_variations())
            
        from itertools import product
        return list(product(*subvars))

    def isvalid(self, msg, potential_is, depth):
        depth += 1
        indent = '  ' * depth
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
                current_i = i
                
                hoypots = []
                # i'den baslarsak, senin kurallardan tutan var mi?
                for ruleset in self.rules:

                    subpotentials = [i]
                    newpotentials = []
                    # print(ruleset)
                    for rule in ruleset:
                        # print(f"{indent} subpotentials " + str(subpotentials))
                        for si in subpotentials:
                            res, rule_is = rule_map[rule].isvalid(msg, [si], depth)
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
    
    rule = None
    if '"' in ruledef:
        rule = Rule(int(id.strip()), char = ruledef.strip().replace('"', ""))
    else:
        rule = Rule(int(id.strip()), ruledef=ruledef)

    rule_map[rule.id] = rule

# print(rule_map[0].isvalid("abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa", [0], 0))
# exit(0)
cnt = 0
for msg in messages:
    res, i = rule_map[0].isvalid(msg, [0], 0)
    if res and i[0] == len(msg):
        cnt += 1


print(cnt)