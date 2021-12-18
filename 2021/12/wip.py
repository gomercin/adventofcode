import os, sys
from itertools import permutations

# perm = permutations([1, 2, 3], 2)

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

# input_set = list(map(lambda x:int(x), input))

nodes = {}
for line in input:
    line = line.strip()
    ps = line.split('-')
    left = ps[0]
    right = ps[1]

    if left not in nodes:
        nodes[left] = []
    if right not in nodes:
        nodes[right] = []

    nodes[left].append(right)
    nodes[right].append(left)

memo = {}

"""
start

visited = start iken
findfrom(A, [start])
    finrfrom(b, [start])
        findfrom(A, [start, b])
        findfrom(d, [start, b])
        findfrom(end, [start, b])
    finrfrom(c, [start])
        findfrom(A, [start, c])
    findfrom(end, [start])

findfrom(b, v)
 findfrom(A, [start, b])

"""

def find_all_paths_p1(begin, visited):
    if begin[0].islower():
        if begin == 'end':
            return [['end']]
        else:
            if begin in memo:
                return memo[begin]
            else:
                visited.add(begin)

    # print(begin, visited)
    all_paths = []
    neighbors = nodes[begin]

    for n in neighbors:
        # print(f"searching for paths from {n}")
        # if n[0].islower():
        #     if n in visited:
        #         continue
        #     c_visited.add(n)
        if n not in visited:
            # if n[0].islower():
            #    visited.add(n)
            subpaths = find_all_paths_p1(n, visited.copy())

            for sp in subpaths:
                if sp:
                    sp.insert(0, begin)
                    all_paths.append(sp)

    #if begin[0].islower():
    #    memo[begin] = all_paths
    return all_paths


def part_1():

    visited = set()
    # visited.add('start')
    all_paths = find_all_paths_p1('start', visited)
    print(all_paths)
    print(len(all_paths))


def can_be_visited(node, visited):
    if not node[0].islower():
        return True
    if node not in visited:
        return True


    if node == 'start':
        return False

    if visited[node] > 1:
        return False

    
    thereistwo = False
    for v in visited.values():
        if v > 1:
            thereistwo = True
            break

    if not thereistwo:
        return True
    else:
        return False



def find_all_paths(begin, visited):
    if begin[0].islower():
        if begin == 'end':
            return [['end']]
        else:
            if begin in memo:
                return memo[begin]
            else:
                if begin not in visited:
                    visited[begin] = 0
                visited[begin] += 1

    # print(begin, visited)
    all_paths = []
    neighbors = nodes[begin]

    for n in neighbors:
        # print(f"searching for paths from {n}")
        # if n[0].islower():
        #     if n in visited:
        #         continue
        #     c_visited.add(n)
        if can_be_visited(n, visited):
            # if n[0].islower():
            #    visited.add(n)
            subpaths = find_all_paths(n, visited.copy())

            for sp in subpaths:
                if sp:
                    sp.insert(0, begin)
                    all_paths.append(sp)

    #if begin[0].islower():
    #    memo[begin] = all_paths
    return all_paths

def part_2():
    visited = dict()
    # visited.add('start')
    all_paths = find_all_paths('start', visited)
    print(all_paths)
    print(len(all_paths))
    



part_1()
part_2()