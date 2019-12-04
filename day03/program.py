import sys

from pprint import pprint 

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Coordinate:
    x: int
    y: int


class Step:
    def __init__(self, input):
        self.direction = input[0]
        self.num_steps = int(input[1:])

    def __repr__(self):
        return f"direction: {self.direction}, num_steps: {self.num_steps}"

class Locations:
    def __init__(self, mapsize: int=500):
        self.locations = {}
        self.intersections = []
        self.map = [['.' for _ in range(mapsize)] for _ in range(mapsize)]
        self.mapsize = mapsize
        self.map_offset = mapsize // 2
        self.map[self.map_offset][self.map_offset] = "O"

    def add_location(self, new_loc, visitor):
        print(new_loc)
        if not new_loc in self.locations:
            self.locations[new_loc] = {
                'visitors': [visitor]
            }
            self.map[new_loc.x+self.map_offset][new_loc.y+self.map_offset] = visitor
        else:
            if not visitor in self.locations[new_loc]:
                self.locations[new_loc]['visitors'].append(visitor)
                self.intersections.append(new_loc)
                self.map[new_loc.x+self.map_offset][new_loc.y+self.map_offset] = 'X' 
    
    def calc_closest_intersection(self):
        lowest_distance = sys.maxsize

        for intersection in self.intersections:
            current_distance = abs(intersection.x) + abs(intersection.y)
            if current_distance < lowest_distance:
                lowest_distance = current_distance
                self.closest_intersection = intersection
                self.closest_distance = lowest_distance

        return self.closest_intersection, self.closest_distance

    def print_map(self):
        output = ""

        for row in range(self.mapsize):
            for col in range(self.mapsize):
                output += str(self.map[row][col])
            output += '\n'

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
                num_intersections = len(wire_paths.intersections)
                new_loc = step_func(current_loc)
                wire_paths.add_location(new_loc, i)
                if num_intersections < len(wire_paths.intersections):
                    print(f"{step} caused intersection at {new_loc}.")
                current_loc = new_loc

    print(f"Intersections : {wire_paths.intersections}")
    closest_loc, distance = wire_paths.calc_closest_intersection()
    print(f"Closest location : {closest_loc}, Closest distance : {distance}")
    wire_paths.print_map()


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

    input_file = "input.txt"

    input_lines = []

    with open(input_file) as f:
        for line in f:
            input_lines.append(line.strip())
        # pprint(input_lines)

    # evaluate_steps(input_lines)

if __name__ == "__main__":
    solve_day03()