#!/user/bin/env python

import sys
from typing import Set, NamedTuple, Dict, Tuple

class XY(NamedTuple):
    x: int
    y: int

    def __hash__(self):
        return hash(str(self.x) + "__" + str(self.y))


def update_location(x:int, y:int, dir1: str, num1: int, dict_1: Dict, current_1:int):
    locations = set()
    for _ in range(num1):
        if dir1 == 'R':
            x = x + 1
        elif dir1 == 'L':
            x = x - 1
        elif dir1 == 'U':
            y = y + 1
        elif dir1 == 'D':
            y = y - 1
        current = XY(x,y)
        current_1 += 1
        locations.add(current)
        if not hash(current) in dict_1:
            dict_1[hash(current)] = current_1
            #print("Inserting ", current, current_1)
    return locations,x,y, dict_1, current_1

def manhattan(i):
    return  abs(i.x) + abs(i.y)

def find_wire_crossing(wire1:str , wire2:str) -> Tuple[Set, int]:
    wire1_list = wire1.strip().split(',')
    wire2_list = wire2.strip().split(',')
    loc1:Set[XY] = set()
    loc2:Set[XY] = set()
    distance_w1:Dict[XY, int] = dict()
    distance_w2:Dict[XY, int] = dict()
    w1_x = w1_y = w2_x = w2_y = 0
    dist_1 = dist_2 = 0
    for w1,w2 in zip(wire1_list, wire2_list):
        dir1 = w1[0]
        dir2 = w2[0]
        num1 = int(w1[1:])
        num2 = int(w2[1:])
        #print(dir1, dir1, num1, num2)
        w1_loc, w1_x, w1_y, distance_w1, dist_1 = update_location(w1_x, w1_y, dir1, num1, distance_w1, dist_1)
        w2_loc, w2_x, w2_y, distance_w2, dist_2  = update_location(w2_x, w2_y, dir2, num2, distance_w2, dist_2)
        loc1 = loc1.union(w1_loc)
        loc2 = loc2.union(w2_loc)
    all_inter  = loc1.intersection(loc2)
    #[ print(point, hash(point), distance_w1[hash(point)], distance_w2[hash(point)]) for point in all_inter]
    dist_total = min([ distance_w1[hash(point)] + distance_w2[hash(point)] for point in all_inter])
    return all_inter, dist_total

def find_minimum_crossing(wire1:str, wire2:str) -> int:
    """TODO: Docstring for find_minimum_crossing.
    :returns: TODO

    """
    all_inter,_ = find_wire_crossing(wire1, wire2)
    return min([ manhattan(i) for i in all_inter])

def find_sum_distance(wire1:str, wire2: str) -> int:
    """TODO: Docstring for find_sum_distance.
    :returns: TODO

    """
    #all_inter:Set[XY], d1:Dict[XY, int], d2:Dict[XY, int]
    _, dist_total = find_wire_crossing(wire1, wire2)
    return dist_total

assert find_minimum_crossing("R8,U5,L5,D3","U7,R6,D4,L4") == 6
assert find_minimum_crossing("R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83") == 159
assert find_minimum_crossing("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135

assert find_sum_distance("R8,U5,L5,D3","U7,R6,D4,L4") == 30
assert find_sum_distance("R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83") == 610
assert find_sum_distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        wire1 = f.readline()
        wire2 = f.readline()
        print("Answer Part 1", find_minimum_crossing(wire1, wire2))
        print("Answe Part 2 ", find_sum_distance(wire1, wire2))
