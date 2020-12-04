import os, sys, re

lines = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    lines = in_file.readlines()

class Passport:
    def __init__(self, lines):
        all_lines = " ".join(lines)
        all_lines = all_lines.replace("\n", " ")

        self.all_lines = all_lines
        parts = all_lines.split(" ")

        self.mapping = {}
        for part in parts:
            hed = part.split(':')
            self.mapping[hed[0]] = hed[1]

    def validate(self):
        if not self.mapping:
            return False
        keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

        for key in keys:
            if key not in self.mapping or not self.mapping[key].strip():
                return False

        return True

    def validate2(self):
        if not self.mapping:
            return False
        keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

        for key in keys:
            if key not in self.mapping or not self.mapping[key].strip():
                return False
        try:
            byr = int(self.mapping['byr'])
            iyr = int(self.mapping['iyr'])
            eyr = int(self.mapping['eyr'])
            pid = int(self.mapping['pid'])
        except:
            return False


        if byr < 1920 or byr > 2002:
            return False

        if iyr < 2010 or iyr > 2020:
            return False

        if eyr < 2020 or eyr > 2030:
            return False

        hgt = self.mapping['hgt']
        if hgt.endswith('cm') or hgt.endswith('in'):
            istrhgt = hgt[:-2]
            try:
                ihgt = int(istrhgt)
            except:
                return False

            if hgt.endswith('cm'):
                if ihgt < 150 or ihgt > 193:
                    return False
            else:
                if ihgt < 59 or ihgt > 76:
                    return False
        else:
            return False

        match = re.search(r'^#[0-9a-fA-F]{6}$', self.mapping['hcl'])
        if not match:
            return False

        if self.mapping['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        if len(self.mapping['pid']) != 9:
            return False

        return True

    def print(self):
        print(f"{self.mapping.get('byr', 'none')}\t{self.mapping.get('iyr', 'none')}\t{self.mapping.get('eyr', 'none')}\t{self.mapping.get('hgt', 'none')}\t{self.mapping.get('hcl', 'none')}\t{self.mapping.get('ecl', 'none')}\t{self.mapping.get('pid', 'none')}\t{self.mapping.get('cid', 'none')}")


current_lines=[]
valid1_count = 0
valid2_count = 0
for line in lines:
    line = line.replace('\n', "")
    if not line:
        pp = Passport(current_lines)
        if pp.validate():
            valid1_count += 1
        if pp.validate2():
            valid2_count += 1
        
        current_lines = []
    else:
        current_lines.append(line)

pp = Passport(current_lines)
if pp.validate2():
    valid2_count += 1
if pp.validate():
    valid1_count += 1
    
print(valid1_count)
print(valid2_count)