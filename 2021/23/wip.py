import os, sys
from itertools import permutations

# perm = permutations([1, 2, 3], 2)


"""
 01234567890
#############
#...........#
###C#A#B#C###
  #D#D#B#A#
  #########

"""
costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

hallway = [0] * 11
stops = [0, 1, 3, 5, 7, 9, 10]
rooms = {
    2: ['D', 'C'], 
    4: ['D', 'A'], 
    6: ['B', 'B'], 
    8: ['A', 'C']
}
"""
Anything in the rooms can only move to one of the stops, or to its correct room.
Anything in the stops can only move to its correct room.
It cannot move into its room, if the room contains some other amphipod.

Brute force, at each step:
All ambitis that can move to their room will move to their room
else: for each ambiti on top of their room, branch into all possibilities they can move
from all these possibilities, get the one that solves with minimum energy

D should probably take the shortcut all the time (instead of left right rooms)
In fact, even in the worst case they can directly move to their room by shuffling things around and it would still cost less
D should also always move towards its room
"""

# A A B B C C D D
# rooms have y as -1, -2, -1 being on top
# hallway y = 0, odd numbers and 0 to 10 are stops

#   2    4   6    8
# AAAA BBBB CCCC DDDD
# 1     2    3    4
room_size = 2
def ambiti_in_place(ambiti_id, ambitipos):
    exp_pos = (ambiti_id + 1) * 2
    return ambitipos[0] == exp_pos

def all_in_place(positions):
    for i, pos in enumerate(positions):
        if not ambiti_in_place(i // room_size, pos):
            return False

    return True

def get_path(start, end):
    path = []
    cur = start

    while cur != end:
        if cur[0] == end[0]:
            if cur[1] < end[1]:
                cur = (cur[0], cur[1] + 1)
            else:
                cur = (cur[0], cur[1] - 1)
        else:
            if cur[1] < 0:
                cur = (cur[0], cur[1] + 1)
            else:
                if cur[0] < end[0]:
                    cur = (cur[0] + 1, cur[1])
                else:
                    cur = (cur[0] - 1, cur[1])

        path.append(cur)

    return path

def can_move(start, end, positions):
    path = get_path(start, end)

    # will be doing unnecessary path creations if it is on bottom of a room with something else on top
    for p in path:
        if p in positions:
            return False

    return len(path)

costs = []

current_min = sys.maxsize
counter = 0
def log(current_positions):
    # print("#############")
    hallway = "#...........#"
    rooms1 = "###.#.#.#.###"
    rooms2 = "  #.#.#.#.#  "
    for i, pos in enumerate(current_positions):
        ch = chr(ord('A') + (i // room_size))
        index = pos[0] + 1
        if pos[1] == 0:
            hallway = hallway[:index] + ch + hallway[index + 1:]
        elif pos[1] == -1:
            rooms1 = rooms1[:index] + ch + rooms1[index + 1:]
        elif pos[1] == -2:
            rooms2 = rooms2[:index] + ch + rooms2[index + 1:]
    # print(hallway)
    # print(rooms1)
    # print(rooms2)
    # print("  #########  ")

costdict = {}
def min_solution_cost(current_cost, current_positions, empties):
    global counter, current_min
    if current_cost > current_min:
        return sys.maxsize
    # print(f"counter: {counter}\n\t{current_positions}\n\t{empties}")
    key = f"{current_positions}"
    if key in costdict:
        return costdict[key]

    counter += 1
    if all_in_place(current_positions):
        # print(f"found baby  {counter}")
        return 0

    # log(current_positions)
    potential_costs = []
    for i, pos in enumerate(current_positions):
        # print("OMER 1")
        ambiti_room = ((i // room_size) + 1) * 2
        if ambiti_in_place(i // room_size, pos):
            # no problem if on bottom
            if pos[1] == -room_size: continue
            # need to check if it is on top of another correct ambiti if pos is -1
            ry = pos[1] - 1
            all_correct = True
            while ry >= -room_size:
                ambiti_below = current_positions.index((pos[0], ry))
                ry -= 1

                if ambiti_below // 4 != i // 4:
                    all_correct = False
                    break
            if all_correct: continue
        # print("OMER 2")
        # if an ambiti has exited the room, it can only go back to its room
        # at each iteration, ambiti can go to its room if it is reachable
        # or stay where it is if it is already outside
        # or move into one of the outer locations
        realistic_goals_for_a_happy_life = []
        if pos[1] == 0:
            # print("OMER 3")
            # this is already in the hallway, check if the goal is empty:
            moveto = None
            # print(f"{ambiti_room}, {pos}, {empties}")
            for y in range(-room_size, 0):
                if (ambiti_room, y) in empties: # eh, we could actualy break here more easily instead of loop below
                    ry = y - 1
                    all_correct = True
                    while ry >= -room_size:
                        try:
                            ambiti_below = current_positions.index((ambiti_room, ry))
                            ry -= 1
                            if ambiti_below // 4 != i // 4:
                                all_correct = False
                                break
                        except:
                            # means that place is empty, i.e. usable
                            break
                    if all_correct:
                        moveto = (ambiti_room, y)
                        break
            # or it doesn't move at all, maybe it is better if the other ambiti takes the first place for ex.
            if moveto:
                # print("OMER 33")
                distance = can_move(pos, moveto, current_positions)
                if distance:
                    # print("OMER 34")
                    realistic_goals_for_a_happy_life.append((moveto, distance))
                # print("OMER 35")
        else:
            # print("OMER 4")
            # this can go to any position
            for goal in empties:
                # print("OMER 5")
                if goal[1] == 0:
                    distance = can_move(pos, goal, current_positions)
                    if distance:
                        realistic_goals_for_a_happy_life.append((goal, distance))

        # print(f"goals to be checked for {i}: {realistic_goals_for_a_happy_life}")
        for goal, distance in realistic_goals_for_a_happy_life:
            print(f"checking {goal} {distance} {i}")
            new_cost = distance * costs[i]
            new_empties = empties.copy()
            new_empties.remove(goal)
            new_empties.append(pos)
            new_positions = current_positions.copy()
            new_positions[i] = goal

            potential_costs.append(new_cost + min_solution_cost(current_cost + new_cost,  new_positions, new_empties))

    res = 0
    if potential_costs:
        res = min(potential_costs)
        current_min = min(res, current_min)
    else:
        res = sys.maxsize

    costdict[key] = res

    return res

sys.setrecursionlimit(10**3)

def part_1():
    global room_size
    room_size = 2
    cost = 0
    positions = [
    (4, -1),
    (8, -2),
    (6, -1),
    (6, -2),
    (2, -1),
    (8, -1),
    (2, -2),
    (4, -2),
    ]


    """
     01234567890
    #############
    #...........#
    ###B#C#B#D###
      #A#D#C#A#
      #########
     01234567890
    """
    sample = [
        (2, -2),
        (8, -2),
        (2, -1),
        (6, -1),
        (4, -1),
        (6, -2),
        (4, -2),
        (8, -1)

    ]

    empties = [(x, 0) for x in stops]

    global costs
    costs = []
    for x in range(4):
        costs += ([10**x] * room_size)

    global current_min
    current_min = sys.maxsize

    print(min_solution_cost(0, positions, empties))


def part_2():

    """
    12345678
    #D#C#B#A#
    #D#B#A#C#
    """
    global room_size
    room_size = 4
    cost = 0
    positions = [
    (4, -1),
    (8, -4),
    (6, -3),
    (8, -2),

    (6, -1),
    (6, -4),
    (4, -3),
    (6, -2),

    (2, -1),
    (8, -1),
    (4, -2),
    (8, -3),

    (2, -4),
    (4, -4),
    (2, -2),
    (2, -3)
    ]


    """
     01234567890
    #############
    #...........#
    ###B#C#B#D###
      #A#D#C#A#
      #########
     01234567890
    """
    sample = [
        (2, -2),
        (8, -2),
        (2, -1),
        (6, -1),
        (4, -1),
        (6, -2),
        (4, -2),
        (8, -1)

    ]

    empties = [(x, 0) for x in stops]

    global current_min
    current_min = sys.maxsize

    global costs
    costs = []
    for x in range(4):
        costs += ([10**x] * room_size)

    print(min_solution_cost(0, positions, empties))


part_1()
part_2()