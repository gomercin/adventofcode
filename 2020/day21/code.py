import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

input = []
alltext = ""
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()
    in_file.seek(0)
    alltext = in_file.read()

allergen_possibilities = {} # allergen name, to list of sets
ingredient_counts = {} 
foods = [] # list of Food objects

class Food:
    def __init__(self, line):
        self.ingredients = []
        self.allergens = []

        parts = line.split('(')
        assert(len(parts) > 1)

        self.ingredients = parts[0].split()
        self.allergens = parts[1].replace("contains ", "").replace(")", "").split(", ")

        for ing in self.ingredients:
            if ing not in ingredient_counts:
                ingredient_counts[ing] = 0

            ingredient_counts[ing] += 1

        for a in self.allergens:
            if a not in allergen_possibilities:
                allergen_possibilities[a] = []
            allergen_possibilities[a].append(set(self.ingredients))

    def print(self):
        print("Food: ")
        print("   ingredients: " + str(self.ingredients))
        print("   allergens  : " + str(self.allergens))

for line in input:
    line = line.strip()
    food = Food(line)
    # food.print()
    foods.append(food)

allergen_possibilities_reduced = {}
# for each allergen, intersect the ingredients it can possibly be found
# this gives a reduced list of potential ingredients
for allergen, possibilities in allergen_possibilities.items():
    intersection = set.intersection(*possibilities)
    allergen_possibilities_reduced[allergen] = intersection

allergen_possibilities_certain = {}
allergics = set()

# loop "a few" times, normally we should loop until each allergen is mapped to a single ingredient
# but looping 10 times was good and fast enough, and I am too lazy to write the other check :)
for i in range(10):
    for allergen, possibilities in allergen_possibilities_reduced.items():
        if len(possibilities) == 1:
            # this allergen is certainly in this only ingredient
            # so this ingredient can be removed from other allergens
            assert allergen not in allergen_possibilities_certain
            ingredient = list(possibilities)[0]
            allergen_possibilities_certain[allergen] = ingredient
            allergics.add(ingredient)
            a = list(possibilities)[0]
            for a2, p2 in allergen_possibilities_reduced.items():
                if a in p2:
                    allergen_possibilities_reduced[a2].remove(a)

cnt = 0

for k, v in ingredient_counts.items():
    if k not in allergics:
        cnt += v

# p1
print(cnt)

allergens = sorted(list(allergen_possibilities_certain.keys()))

res = ""

for allergen in allergens:
    res += ","
    res += allergen_possibilities_certain[allergen]

# p2
print(res[1:])