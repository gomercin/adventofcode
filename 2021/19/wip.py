import os, sys
from collections import namedtuple
input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

Point = namedtuple('Point', ['x', 'y', 'z'])

"""
if it was in 2d and there was no rotation:


--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1


- for each pair between two scanners,
    align them to match
    apply the difference to all other beacons
    check if there are at least 12 matches
    repeat for all possible rotations?

"""

class Scanner:
    def __init__(self):
        self.points = set()
        self.name = ""
        self.position = None
        self.adjusted_points = None

        self.rots = None

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        # ssshhh, don't tell anyone!
        return self.name == other.name

    def rotations_first_attempt(self):
        """
        total of 24 orientations...
        """
        if self.rots:
            return self.rots

        res = set()
        
        rotated = self.points.copy()
        res.add(tuple(rotated))

        def _rotx(ps):
            rotated = ps
            for _ in range(1, 4):
                new_rotated = set()
                for p in rotated:
                    newpoint = Point(p.x, p.z, -1 * p.y)
                    new_rotated.add(newpoint)
            
                rotated = new_rotated
                res.add(tuple(rotated))

        def _roty(ps):
            rotated = ps
            for _ in range(1, 4):
                new_rotated = set()
                for p in rotated:
                    newpoint = Point(p.z, p.y, -1 * p.x)
                    new_rotated.add(newpoint)
            
                rotated = new_rotated
                res.add(tuple(rotated))

        def _rotz(ps):
            rotated = ps
            for _ in range(1, 4):
                new_rotated = set()
                for p in rotated:
                    newpoint = Point(p.y, -1 * p.x, p.z)
                    new_rotated.add(newpoint)
            
                rotated = new_rotated
                res.add(tuple(rotated))

        face = set()
        for p in self.points:
            face.add(Point(-1 * p.x, p.y, p.z))
        
        res.add(tuple(face))

        face = set()
        for p in self.points:
            face.add(Point(p.x, -1 * p.y, p.z))
        
        res.add(tuple(face))

        face = set()
        for p in self.points:
            face.add(Point(p.x, p.y, -1 * p.z))
        
        res.add(tuple(face))

        initial = res.copy()

        for f in initial:
            _rotx(f)
            _roty(f)
            _rotz(f)

        """
        initial = res.copy()
        for rot in initial:
            _rotx(rot)
            _roty(rot)
            _rotz(rot)
        """
        print(len(res))
        self.rots = res
        return self.rots

    def rotations(self):
        """
        total of 24 orientations...
        """
        if self.rots:
            return self.rots

        res = []

        def _rotx(ps):
            rotated = set()
            for p in ps:
                newpoint = Point(p.x, p.z, -1 * p.y)
                rotated.add(newpoint)
            return tuple(rotated)

        def _roty(ps):
            rotated = set()
            for p in ps:
                newpoint = Point(p.z, p.y, -1 * p.x)
                rotated.add(newpoint)
            return tuple(rotated)

        def _rotz(ps):
            rotated = set()
            for p in ps:
                newpoint = Point(p.y, -1 * p.x, p.z)
                rotated.add(newpoint)
            return tuple(rotated)


        res.append(tuple(self.points))
        # imagine a cube on the desk, rotate it without lifting the bottom
        rotated = self.points.copy()
        for _ in range(3):
            rotated = _roty(rotated)
            res.append(rotated)

        # also bring the bottom and top to front:
        res.append(_rotx(self.points))
        # heh, could add a parameter to these
        res.append(_rotx(_rotx(_rotx(self.points))))

        # know, for each of these 6 faces, rotate on z three times
        # so we are changing what is on the top
        new_rots = []

        for r in res:
            current = r
            for _ in range(3):
                current = _rotz(current)
                new_rots.append(current)

        # set should have a merge operation I guess
        for nr in new_rots:
            res.append(nr)

        # print(len(res))

        #for r in res:
        #    for p in r:
        #        print(*p)
        #    print("")


        self.rots = res
        return self.rots


scanners = []
current_scanner = None
for line in input:
    line = line.strip()
    if not line:
        scanners.append(current_scanner)
    elif line.startswith('---'):
        current_scanner = Scanner()
        current_scanner.name = line.replace('---', "").replace(' ', "")
    else:
        points = list(map(int, line.split(',')))
        current_scanner.points.add(Point(*points))

if not scanners or (current_scanner and scanners[-1] != current_scanner):
    scanners.append(current_scanner)

scanners[0].position = Point(0, 0, 0)

scanners[0].rotations()

print(len(scanners))

def pr(m):
    for p in m:
        print(p.x, p.y, p.z)

def part_1():
    """
    Compare known scanners against unknowns
    for each rotation from each, align them on each point
    and see if the rest fits with that alignment
    """
    # can we assume that the first has the correct orientation and adapt everything else for it?
    scanners[0].adjusted_points = scanners[0].points

    knowns = [scanners[0]]
    unknowns = scanners[1:]

    new_knowns = set()
    while len(unknowns) > 0:
        print(f"remaining: {len(unknowns)}")
        for known in knowns:
            for unknown in unknowns:
                if unknown in new_knowns: continue
                known_rot = known.adjusted_points
                known_pos = known.position
                unknown_rots = unknown.rotations()

                """feels like there can be an extra optimization here 
                as they have a limited range of 1000
                """
                matched = False
                for unknown_rot in unknown_rots:
                    for kn_point in known_rot:
                        for un_point in unknown_rot:
                            # if the current pair was overlapped
                            diff = Point(kn_point.x - un_point.x, kn_point.y - un_point.y, kn_point.z - un_point.z)

                            # shift all points by the diff, check how many of them are in known rot
                            adjusted = set()
                            match_count = 0
                            for ap in unknown_rot:
                                np = Point(ap.x + diff.x, ap.y + diff.y, ap.z + diff.z)
                                if np in known_rot:
                                    match_count += 1
                                adjusted.add(np)

                            if match_count >= 12:
                                unknown.adjusted_points = adjusted
                                unknown.position = diff # Point(known_pos.x + diff.x, known_pos.y + diff.y, known_pos.z + diff.z)
                                matched = True
                                new_knowns.add(unknown)
                                break

                        if matched: break
                    if matched: break

        if new_knowns:
            knowns = []
            for nk in new_knowns:
                knowns.append(nk)
                try:
                    unknowns.remove(nk)
                except:
                    print(nk)
                    print(unknowns)
                    raise 
            new_knowns = set()
        else:
            break

    all_beacons = set()

    for s in scanners:
        print(s.position)
        for p in s.adjusted_points:
            all_beacons.add(p)
            


    print(len(all_beacons))


def part_2():
    from itertools import permutations

    maxdist = 0
    for p in permutations(scanners, 2):
        s1 = p[0].position
        s2 = p[1].position

        dist = abs(s1.x - s2.x) + abs(s1.y - s2.y) + abs(s1.z - s2.z)
        if dist > maxdist:
            maxdist = dist

    print(maxdist)


from time import time

begin = time()

part_1()
print(time() - begin)
part_2()