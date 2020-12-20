import os, sys
from itertools import permutations

TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3

input = []
with open(os.path.join(sys.path[0], 'sample'), 'r') as in_file:
    input = in_file.readlines()

input.append("")
class Tile:
    def __init__(self, lines):
        self.id = int(lines[0].split(" ")[1][:-1])
        self.lines = lines

        self.edge_variations = set()
        #(neighbor tile id, variation id)  -> this.variation_id
        self.top_connects = {}
        self.bottom_connects = {}
        self.right_connects = {}
        self.left_connects = {}

        self.parse()
        
    def parse(self):
        top = left = bottom = right = 0
        for i in range(len(self.lines[1])):
            top <<= 1
            bottom <<= 1
            if self.lines[1][i] == "#":
                top |= 0x1

            if self.lines[-1][i] == "#":
                bottom |= 0x1

        for i in range(1, len(self.lines)):
            left <<= 1
            right <<= 1

            if self.lines[i][0] == "#":
                left |= 0x1

            if self.lines[i][-1] == "#":
                right |= 0x1

        # normal
        self.edge_variations.add((top, left, bottom, right))
        # flipped horizontal
        self.edge_variations.add((bottom, self.reverse(left), top, self.reverse(right)))
        # flipped vertical
        self.edge_variations.add((self.reverse(bottom), left, self.reverse(top), right))

        tmp_top, tmp_left, tmp_bottom, tmp_right = top, left, bottom, right
        for _ in range(3):
            new_var = (tmp_right, self.reverse(tmp_top), tmp_left, self.reverse(tmp_bottom))
            self.edge_variations.add(new_var)
            tmp_top, tmp_left, tmp_bottom, tmp_right = new_var



    def reverse(self, num):
        new_num = 0

        for i in range(10):
            new_num <<= 1
            new_num |= (num & 0x1)
            num >>= 1

        return new_num



all_tiles = {}

current_tile_lines = []
for line in input:
    line = line.strip()
    if not line and current_tile_lines:
        tile = Tile(current_tile_lines)
        current_tile_lines = []
        all_tiles[tile.id] = tile
    else:
        current_tile_lines.append(line)



p_lefts = {}
p_rights = {}
p_tops = {}
p_bottoms = {}

p_left_nums = set()
p_right_nums = set()
p_top_nums = set()
p_bottom_nums = set()

for tile_id, tile in all_tiles.items():
    for i, ev in enumerate(tile.edge_variations):
        if ev[LEFT] not in p_lefts:
            p_lefts[ev[LEFT]] = set()

        p_lefts[ev[LEFT]].add((tile_id, i))
        p_left_nums.add(ev[LEFT])

        if ev[RIGHT] not in p_rights:
            p_rights[ev[RIGHT]] = set()

        p_rights[ev[RIGHT]].add((tile_id, i))
        p_right_nums.add(ev[RIGHT])

        if ev[TOP] not in p_tops:
            p_tops[ev[TOP]] = set()

        p_tops[ev[TOP]].add((tile_id, i))
        p_top_nums.add(ev[TOP])

        if ev[BOTTOM] not in p_bottoms:
            p_bottoms[ev[BOTTOM]] = set()

        p_bottoms[ev[BOTTOM]].add((tile_id, i))
        p_bottom_nums.add(ev[BOTTOM])


for tile_id, tile in all_tiles.items():
    for ei, ev in enumerate(tile.edge_variations):
        if ev[TOP] in p_bottom_nums:
            ps = p_bottoms[ev[TOP]]

            for p in ps:
                if p[0] != tile_id:
                    if p not in tile.top_connects:
                        tile.top_connects[p] = []
                    tile.top_connects[p].append(ei)

        if ev[BOTTOM] in p_top_nums:
            ps = p_tops[ev[BOTTOM]]

            for p in ps:
                if p[0] != tile_id:
                    if p not in tile.bottom_connects:
                        tile.bottom_connects[p] = []
                    tile.bottom_connects[p].append(ei)

        if ev[LEFT] in p_right_nums:
            ps = p_rights[ev[LEFT]]

            for p in ps:
                if p[0] != tile_id:
                    if p not in tile.left_connects:
                        tile.left_connects[p] = []
                    tile.left_connects[p].append(ei) 

        if ev[RIGHT] in p_left_nums:
            ps = p_lefts[ev[RIGHT]]

            for p in ps:
                if p[0] != tile_id:
                    if p not in tile.right_connects:
                        tile.right_connects[p] = []
                    tile.right_connects[p].append(ei)                             


tile_ids = all_tiles.keys()
# all_tile_permutations = list(permutations(tile_ids, len(tile_ids)))
# print(all_tile_permutations)

from math import sqrt
SIZE = sqrt(len(all_tiles))
def canbefilled(grid, index, unused_tiles):
    new_index = None
    if index[1] == SIZE - 1: # rightmost, try next row
        if index[0] == SIZE - 1: # means it is filled:
            return grid
        new_index = (index[0] + 1, 0)
    else:
        new_index = (index[0], index[1] + 1)

    top_neighbor_index = (new_index[0] - 1, new_index[1])
    left_neighbor_index = (new_index[0], new_index[1] - 1)

    
    top_neighbor = grid.get(top_neighbor_index)
    left_neighbor = grid.get(left_neighbor_index)

    potentials = []
    if top_neighbor:
        top_tile, variation = all_tiles[top_neighbor[0]], top_neighbor[1]
        for topk, topvs in top_tile.bottom_connects.items():
            if variation in topvs:
                potentials.append(topk)

        if not potentials:
            return False

        if left_neighbor:
            bothmatches = []
            for lp in potentials:
                # check if this variation can match with the left neighbor as well
                left_tile, variation = all_tiles[left_neighbor[0]], left_neighbor[1]

                for leftk, leftvs in left_tile.right_connects.items():
                    if variation in leftvs:
                        bothmatches.append(lp)
            potentials = bothmatches
        if not potentials:
            return False

    elif left_neighbor:
        left_tile, variation = all_tiles[left_neighbor[0]], left_neighbor[1]
        for leftk, leftvs in left_tile.right_connects.items():
            if variation in leftvs:
                potentials.append(leftk)

        if not potentials:
            return False

    for potential in potentials:
        from copy import deepcopy
        newgrid = deepcopy(grid)
        grid[new_index] = potential
        res = canbefilled(grid, new_index, unused_tiles)
        if res:
            return True

    return False



failed = False
grid = {}
index = (0, 0)

for tile_id in tile_ids:
    unused_tiles = set(tile_ids)
    unused_tiles.remove(tile_id)
    for variation in range(6):
        grid[index] = (tile_id, variation)
        res = canbefilled(grid, index, unused_tiles)
        if res:
            c1 = grid.get((0,0))[0]
            c2 = grid.get((0,SIZE-1))[0]
            c3 = grid.get((SIZE-1,0))[0]
            c4 = grid.get((SIZE-1,SIZE-1))[0]

            id1 = all_tiles[c1].id
            id2 = all_tiles[c2].id
            id3 = all_tiles[c3].id
            id4 = all_tiles[c4].id
            print(id1, id2, id3, id4 , id1 * id2 * id3 * id4)
            exit(0)
        else:
            print("failed grid: " + str(grid))
            print("**************")
            pass