import os, sys

input = []
with open(os.path.join(sys.path[0], 'test1'), 'r') as in_file:
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

    def isvalid(self, msg, i):
        # print(f"checking {msg[i:]}, for rule{self.id}")
        # ababbb, 0
        if self.char:
            if msg[i] == self.char:
                # print("it held : " + self.char)
                return True, i + 1
            else:
                # print("failed1 : "  + self.char)
                return False, i + 1
        else:
            current_i = i
            potential_is = []
            
            failed = False
            for ruleset in self.rules:
                failed = False
                # print(ruleset)
                current_i = i
                failedrule = -1
                for rule in ruleset:
                    res, current_i = rule_map[rule].isvalid(msg, current_i)
                    if not res:
                        failedrule = rule
                        failed = True
                        break

                if current_i < len(msg):
                    potential_is.append(current_i)
                

            print(potential_is)
            # print(f"{'failed' if failed else 'success'} {msg[i:]}, for rule{self.id}, rem: {msg[current_i:]}")
            return len(potential_is) > 0, potential_is


for r in rules:
    id, ruledef = r.split(":")
    
    rule = None
    if '"' in ruledef:
        rule = Rule(int(id.strip()), char = ruledef.strip().replace('"', ""))
    else:
        rule = Rule(int(id.strip()), ruledef=ruledef)

    rule_map[rule.id] = rule

print(rule_map[0].isvalid("aaaaab", 0))
exit(0)
cnt = 0
for msg in messages:
    res, i = rule_map[0].isvalid(msg, 0)
    if res and i == len(msg):
       cnt += 1


print(cnt)