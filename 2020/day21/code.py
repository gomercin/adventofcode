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
    food.print()
    foods.append(food)

allergen_possibilities_reduced = {}
for allergen, possibilities in allergen_possibilities.items():
    intersection = set.intersection(*possibilities)
    allergen_possibilities_reduced[allergen] = intersection

allergen_possibilities_certain = {}

for i in range(10):
    for allergen, possibilities in allergen_possibilities_reduced.items():
        if len(possibilities) == 1:
            assert allergen not in allergen_possibilities_certain
            allergen_possibilities_certain[allergen] = list(possibilities)[0]
            a = list(possibilities)[0]
            for a2, p2 in allergen_possibilities_reduced.items():
                if a in p2:
                    allergen_possibilities_reduced[a2].remove(a)

print(allergen_possibilities_certain)

cnt = 0

for v in allergen_possibilities_certain.values():
    del ingredient_counts[v]



for k, v in ingredient_counts.items():
    cnt += v

print(cnt)


allergens = sorted(list(allergen_possibilities_certain.keys()))


res = ""

for allergen in allergens:
    res += ","
    res += allergen_possibilities_certain[allergen]

print(res)