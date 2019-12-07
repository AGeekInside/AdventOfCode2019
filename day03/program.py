import sys

from pprint import pprint 

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Coordinate:
    x: int
    y: int

@dataclass(unsafe_hash=True)
class Visit:
    loc: Coordinate
    steps: int
    visitor: int

class Step:
    def __init__(self, input):
        self.direction = input[0]
        self.num_steps = int(input[1:])

    def __repr__(self):
        return f"direction: {self.direction}, num_steps: {self.num_steps}"

class Locations:
    def __init__(self, mapsize: int=10, update_map = False):
        self.locations = {}
        self.intersections = []
        self.update_map = update_map
        self.visitor_visits = {}

        if self.update_map:
            self.map = [['.' for _ in range(mapsize)] for _ in range(mapsize)]
            self.mapsize = mapsize
            self.map_offset = mapsize // 2
            self.map[self.map_offset][self.map_offset] = "O"

    def new_visitor(self, visitor):
        return not visitor in self.visitor_visits

    def check_new_visit(self, loc, visitor):
        if self.new_visitor(visitor):
            return True
        elif not visitor in self.visitor_visits:
            return True
        elif loc in self.visitor_visits[visitor]:
            return False
        else:
            return True

    def is_intersection(self, loc, visitor):
        #print(f"Checking if intersection: {visitor} @ {loc}")
        #pprint(f"{self.locations}")
        if self.new_visitor(visitor):
            return False
        elif len(self.visitor_visits) < 2:
            return False
        elif loc in self.locations:
            #print(f"Found an intersection at {loc} with {visitor}")
            #print(f"self.locations[loc]")
            return True
        else:
            return False

    def add_location(self, new_loc, visitor, steps):
        new_visitor = self.new_visitor(visitor)
        new_visit = self.check_new_visit(new_loc, visitor) 
        is_intersection = self.is_intersection(new_loc, visitor)

        new_visit = Visit(new_loc, steps, visitor)
        if new_visitor:
            self.visitor_visits[visitor] = {}
        if new_visit:
            self.visitor_visits[visitor][new_loc] = [new_visit]
        else:
            self.visitor_visits[visitor][new_loc].append(new_visit)
        if new_loc in self.locations:
            self.locations[new_loc].append(new_visit)
        else:
            self.locations[new_loc] = [new_visit]

        if is_intersection:
            self.intersections.append(self.locations[new_loc])
    
    def calc_closest_intersection(self):
        lowest_distance = sys.maxsize

        for intersection in self.intersections:
            pprint(intersection)
            current_distance = intersection[0].steps + intersection[1].steps
            if current_distance < lowest_distance:
                lowest_distance = current_distance
                self.closest_intersection = intersection
                self.closest_distance = lowest_distance

        return self.closest_intersection, self.closest_distance

    def print_map(self):
        output = ""

        if self.update_map:
            for row in range(self.mapsize):
                for col in range(self.mapsize):
                    output += str(self.map[row][col])
                output += '\n'
        else:
            output = "No map generated."
        print(output)

def find_steps(raw_input):

    steps = []
    for step in raw_input.split(','):
        steps.append(Step(step.strip()))

    return steps

def step_right(current_loc):
    return Coordinate(current_loc.x+1, current_loc.y)

def step_left(current_loc):
    return Coordinate(current_loc.x-1, current_loc.y)

def step_up(current_loc):
    return Coordinate(current_loc.x, current_loc.y+1)

def step_down(current_loc):
    return Coordinate(current_loc.x, current_loc.y-1)

def traverse_steps(step_lists):

    wire_paths = Locations()
    print(f"Processing {len(step_lists)} lists of steps.")

    for i, step_list in enumerate(step_lists):
        current_loc = Coordinate(x=0,y=0)
        total_steps = 0
        print(f"Traversing {len(step_list)} steps.")
        for step in step_list:
            if step.direction == 'R':
                step_func = step_right
            elif step.direction == 'L':
                step_func = step_left
            elif step.direction == 'U':
                step_func = step_up
            elif step.direction == 'D':
                step_func = step_down
            for _ in range(step.num_steps):
                new_loc = step_func(current_loc)
                total_steps += 1
                wire_paths.add_location(new_loc, i, total_steps)
                current_loc = new_loc

    #pprint(wire_paths.visitor_visits)
    pprint(wire_paths.intersections)
    closest_loc, distance = wire_paths.calc_closest_intersection()
    print(f"Closest location : {closest_loc}, Closest distance : {distance}")


def evaluate_steps(input):
    step_lists = []
    for line in input:
        wire_steps = find_steps(line)
        step_lists.append(wire_steps)
    traverse_steps(step_lists)

def solve_day03():

    test_inputs = [
        ( "R8,U5,L5,D3",
          "U7,R6,D4,L4"),
        ( "R75,D30,R83,U83,L12,D49,R71,U7,L72",
          "U62,R66,U55,R34,D71,R55,D58,R83"),
        ( "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
          "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    ]

    for test_input in test_inputs:
        evaluate_steps(test_input)

    input_file = "day03/input.txt"

    input_lines = []

    with open(input_file) as f:
        for line in f:
            input_lines.append(line.strip())
        # pprint(input_lines)

    evaluate_steps(input_lines)

if __name__ == "__main__":
    solve_day03()