import os, sys
from itertools import permutations
from copy import deepcopy
import numpy as np

TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3

input = []
with open(os.path.join(sys.path[0], 'input'), 'r') as in_file:
    input = in_file.readlines()

input.append("")
class Tile:
    def __init__(self, lines):
        self.id = int(lines[0].split(" ")[1][:-1])
        self.lines = lines

        self.edge_variations = []
        #(neighbor tile id, variation id)  -> this.variation_id
        self.top_connects = {}
        self.bottom_connects = {}
        self.right_connects = {}
        self.left_connects = {}

        tmpimage = [[] for _ in range(len(lines[1]) -2)]
        self.images = []

        for i in range(1, len(self.lines) - 2):
            tmpimage[i-1] = (list(self.lines[i + 1]))[1:-1]

        self.image = np.array(tmpimage)
        if self.id == 2311 or self.id == 3571: print(self.image)

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

        rotations = [(top, left, bottom, right)]
        self.images.append(self.image)
        tmp_top, tmp_left, tmp_bottom, tmp_right = top, left, bottom, right
        tmpimg = self.image
        for _ in range(3):
            new_var = (tmp_right, self.reverse(tmp_top), tmp_left, self.reverse(tmp_bottom))
            rotations.append(new_var)
            tmp_top, tmp_left, tmp_bottom, tmp_right = new_var

            tmpimg = np.rot90(tmpimg)
            self.images.append(tmpimg)

        self.edge_variations.extend(rotations)

        for i, rot in enumerate(rotations):
            tmp_top, tmp_left, tmp_bottom, tmp_right = rot[0], rot[1], rot[2], rot[3]
            # flip rotation horizontal
            self.edge_variations.append((tmp_bottom, self.reverse(tmp_left), tmp_top, self.reverse(tmp_right)))
            
            self.images.append(np.flip(self.images[i], 0))

            # flip rotation vertical:
            self.edge_variations.append((self.reverse(tmp_bottom), tmp_left, self.reverse(tmp_top), tmp_right))
            self.images.append(np.flip(self.images[i], 1))

        assert len(self.images) == len(self.edge_variations)


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
from copy import deepcopy
SIZE = int(sqrt(len(all_tiles)))
def canbefilled__(grid, index, unused_tiles):
    print("checking grid: " + str(grid), SIZE)
    new_index = None
    if index[1] == SIZE - 1: # rightmost, try next row
        if index[0] == SIZE - 1: # means it is filled:
            return deepcopy(grid)
        new_index = (index[0] + 1, 0)
    else:
        new_index = (index[0], index[1] + 1)

    top_neighbor_index = (new_index[0] - 1, new_index[1])
    left_neighbor_index = (new_index[0], new_index[1] - 1)

    print(left_neighbor_index)
    
    top_neighbor = grid.get(top_neighbor_index)
    left_neighbor = grid.get(left_neighbor_index)

    potentials = []
    if top_neighbor:
        top_tile, variation = all_tiles[top_neighbor[0]], top_neighbor[1]
        for topk, topvs in top_tile.bottom_connects.items():
            if variation in topvs:
                potentials.append(topk)

        if not potentials:
            print("failed due to no match with top")
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
                print("failed due to top matches did not match with left")
                return False

    elif left_neighbor:
        left_tile, variation = all_tiles[left_neighbor[0]], left_neighbor[1]
        for leftk, leftvs in left_tile.right_connects.items():
            if variation in leftvs:
                potentials.append(leftk)

        if not potentials:
            print("failed due to no left match")
            return False

    for potential in potentials:
        newgrid = deepcopy(grid)
        newgrid[new_index] = potential
        res = canbefilled(newgrid, new_index, unused_tiles)
        if res:
            return res

    print("failed due to no match found")
    return False

def canbefilled(grid, index, unused_tiles):
    # print("checking grid: " + str(grid), SIZE)
    new_index = None
    if index[1] == SIZE - 1: # rightmost, try next row
        if index[0] == SIZE - 1: # means it is filled:
            return deepcopy(grid)
        new_index = (index[0] + 1, 0)
    else:
        new_index = (index[0], index[1] + 1)

    top_neighbor_index = (new_index[0] - 1, new_index[1])
    left_neighbor_index = (new_index[0], new_index[1] - 1)

    top_neighbor = grid.get(top_neighbor_index)
    left_neighbor = grid.get(left_neighbor_index)

    potentials = []
    if top_neighbor:
        tops_bottom_edge = all_tiles[top_neighbor[0]].edge_variations[top_neighbor[1]][BOTTOM]
        if tops_bottom_edge in p_tops:
            potentials = p_tops[tops_bottom_edge]
        else:
            return False

        if left_neighbor:
            lefts_right_edge = all_tiles[left_neighbor[0]].edge_variations[left_neighbor[1]][RIGHT]

            if lefts_right_edge in p_lefts:
                left_potentials = p_lefts[lefts_right_edge]
            else:
                return False

            intersection = []

            for lp in left_potentials:
                if lp in potentials:
                    intersection.append(lp)

            potentials = intersection
    elif left_neighbor:
        lefts_right_edge = all_tiles[left_neighbor[0]].edge_variations[left_neighbor[1]][RIGHT]
        if lefts_right_edge in p_lefts:
            potentials = p_lefts[lefts_right_edge]
        else:
            return False

    if not potentials:
        return False

    for p in potentials:
        if p[0] in unused_tiles:
            newgrid = deepcopy(grid)
            newunused = deepcopy(unused_tiles)
            newunused.remove(p[0])
            newgrid[new_index] = p
            res = canbefilled(newgrid, new_index, newunused)
            if res:
                return res

    return False



failed = False
grid = {}
index = (0, 0)

correct_grid = None
monster = ["                  # ", 
           "#    ##    ##    ###", 
           " #  #  #  #  #  #   "]

monster_img = np.array(
    [list(monster[0]), list(monster[1]), list(monster[2])]
)

print(monster_img)

def grid_to_image(grid):
    img = [[] for _ in range(SIZE * 8)]

    for i in range(SIZE):
        for j in range(SIZE):
            tile_id, variant = grid[(i, j)]
            tile = all_tiles[tile_id]
            tile_img = tile.images[variant]
            
            for img_r in range(len(tile_img)):
                for pixel in tile_img[img_r]:
                    img[i * 8 + img_r].append(pixel)

    assert len(img) == len(img[0]) == SIZE * 8

    return img

def process_monsters(img):
    found = False
    tmpimg = deepcopy(img)
    for row in range(len(img) - 3):
        for col in range(len(img[0]) - len(monster_img[0])):
            skip = False
            tmptmpimg = deepcopy(tmpimg)
            for mrow, monsterrow in enumerate(monster_img):
                if skip: break
                for mcol, char in enumerate(monsterrow):
                    if char == "#":
                        if tmptmpimg[row + mrow][col + mcol] != "#":
                            skip = True
                            break
                        else:
                            tmptmpimg[row + mrow][col + mcol] = "O"

            if skip == False:
                found = True
                tmpimg = deepcopy(tmptmpimg)

    return found, tmpimg



def solve_monsters(grid):
    all_pictures = []
    big_picture = grid_to_image(grid)
    
    all_pictures.append(big_picture)
    tmp_picture = big_picture
    for _ in range(3):
        tmp_picture = np.rot90(tmp_picture)
        all_pictures.append(tmp_picture)

    flips = []

    for pic in all_pictures:
        flips.append(np.flip(pic, 0))
        flips.append(np.flip(pic, 1))

    all_pictures.extend(flips)

    for pic in all_pictures:
        res, newimg = process_monsters(pic)

        if res:
            print("found something!")
            print(newimg)

            cnt = 0
            for row in newimg:
                for ch in row:
                    if ch == "#":
                        cnt += 1

            #p2
            print(cnt)



for tile_id in tile_ids:
    unused_tiles = set(tile_ids)
    unused_tiles.remove(tile_id)
    for variation in range(6):
        grid[index] = (tile_id, variation)
        res = canbefilled(grid, index, unused_tiles)
        if res:
            c1 = res.get((0,0))[0]
            c2 = res.get((0,SIZE-1))[0]
            c3 = res.get((SIZE-1,0))[0]
            c4 = res.get((SIZE-1,SIZE-1))[0]

            id1 = all_tiles[c1].id
            id2 = all_tiles[c2].id
            id3 = all_tiles[c3].id
            id4 = all_tiles[c4].id
            # p1
            print(id1, id2, id3, id4 , id1 * id2 * id3 * id4)

            solve_monsters(res)
            exit(0)