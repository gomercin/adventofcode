import os, sys, string

lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    lines = in_file.readlines()

ALL_BAGS = {}

class Bag:
    def __init__(self, line):
        self.color = ""
        self.can_contain = {}
        self.line = line
        self.parse(line)
        self.all_bags_count = -1

    def parse(self, line):
        line = line.strip()
        parts = line.split("contain")

        self.color = parts[0].strip()[:-5]

        permissions = parts[1].split(',')
        for p in permissions:
            p = p.strip()
            #print(p)
            if p == "no other bags.":
                continue
            sub_parts = p.split(' ', 1)
            cnt = int(sub_parts[0].strip())
            col = sub_parts[1].replace(" bags", "").replace(" bag", "").replace(".", "")
            self.can_contain[col] = cnt

    def print(self):
        print("bag: " + self.color)
        for k, v in self.can_contain.items():
            print(f"\t{k}:{v}")

    def contains(self, clr):
        #print(f"checking {self.color}")
        if clr in self.can_contain:
            #   print(f"\tdirectly holds")
            return True
        else:
            for sub_clr in self.can_contain.keys():
                if ALL_BAGS[sub_clr].contains(clr):
                    return True
            return False

    def bag_cnt(self):
        if self.all_bags_count < 0:
            total = 0
            for k, v in self.can_contain.items():
                total += v
                total += v * (ALL_BAGS[k].bag_cnt())

            self.all_bags_count = total
        return self.all_bags_count

for line in lines:
    bag = Bag(line)
    ALL_BAGS[bag.color] = bag

cnt = 0
for b in ALL_BAGS.values():
    if b.contains("shiny gold"):
        cnt += 1

print(cnt)

shiny = ALL_BAGS["shiny gold"]
print(shiny.bag_cnt())


