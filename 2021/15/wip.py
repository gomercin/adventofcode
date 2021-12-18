import os, sys
from queue import PriorityQueue
from collections import defaultdict

q = PriorityQueue()

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

maze = {}
for y in range(len(input)):
    row = input[y].strip()

    row = list(map(int, list(row)))

    for x in range(len(row)):
        maze[(x, y)] = row[x]


maxx = len(input[0].strip())
maxy = len(input)
print(maxx, maxy)
import sys
import heapq as heap

def dijkstra(G, startingNode):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heappush(pq, (0, startingNode))
 
    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)
        x = node[0]
        y = node[1]
        ns = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        #print(pq)
        for adjNode in ns:
            if adjNode not in G: continue
            if adjNode in visited:    continue
            weight = G[adjNode]
                
            newCost = nodeCosts[node] + weight
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))
        
    return parentsMap, nodeCosts

risks = {}

def part_1():
    prevs, shortestpath = dijkstra(maze, (0,0))
    print(shortestpath[(maxy - 1, maxy - 1)])


def log(m, mx, my):
    for y in range(my):
        r = ""
        for x in range(mx):
            r += f" {m[(x, y)]}"
        
        print(r)
    
    print("")

def part_2():
    newmaze = {}

    #log(maze, maxx, maxy)

    for j in range(5):
        for x in range(maxx):
            for y in range(maxy):
                val = maze[(x, y)] + j
                if val > 9:
                    val = (val % 9)
                newmaze[(x + (j * maxx),y)] = val

    #log(newmaze, maxx * 5, maxy)

    for j in range(1, 5):
        for x in range(maxx * 5):
            for y in range(maxy):
                val = newmaze[(x, y)] + j
                if val > 9:
                    val = (val % 9)
                newmaze[(x,y + (j * maxy))] = val

    #log(newmaze, maxx * 5, maxy * 5)
    
    prevs, shortestpath = dijkstra(newmaze, (0,0))
    print(shortestpath[(maxy * 5 - 1, maxy * 5 - 1)])

part_1()
part_2()