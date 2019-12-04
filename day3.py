import funpy as F
from typing import List, Union


# PART 1


def distance (a):
    """ Manhattan distance between two points """
    def wrap (b):
        return abs (a [0] - b [0]) + abs (a [1] - b [1])
    return wrap

changes = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def point (p, direction: str):
    """ Take some point and walk a direction some magnitude """
    def wrap (magnitude: int):
        change = changes [direction]
        return (
            p [0] + (change [0] * magnitude),
            p [1] + (change [1] * magnitude),
        )
    return wrap

def points (p, line: str) -> list:
    """
    Take some point and make a list of points along a line
    line : ((2, 2), R3) -> [(3, 2), (4, 2), (5, 2)]
    """
    direction = line [0]
    steps = list (range (1, 1 + int (F.tail (line))))
    return F.map (point (p, direction)) (steps)

def step (result: list, line: str):
    """ Reducer that passes last point to next step and flattens points """
    return result + points (result [-1], line)

def steps (p):
    def wrap (lines: str):
        """ Parses puzzle input and drops start point from possible corsses """
        return F.reduce (step) ([p]) (lines.split (",")) [1:]
    return wrap

def closestCross (puzzle: str):
    """ Parse puzzle with 2 wires and returns closes cross from start """
    init = (0, 0)
    return F.compose (
        min,
        F.map (distance (init)),
        list,
        lambda sets: sets [0] & sets [1],
        F.map (set),
        F.map (steps (init))
    ) (puzzle.split ("\n"))


# PART 2


def crossIdx (i: int, p, wire):
    """ Returns index of the first time a wire crosses a point """
    try:
        if wire [i] == p:
            return i
        return F.tailR (crossIdx) (i + 1, p, wire)
    except IndexError:
        return None

def firstCrossIdx (i: int, wire1, wire2) -> Union [int, None]:
    """ Returns index of the first time a point crosses another wire """
    try:
        if wire1 [i] in wire2:
            return i
        return F.tailR (firstCrossIdx) (i + 1, wire1, wire2)
    except IndexError:
        return None

def fastestCross (puzzle: str):
    """
    Checks which wire crossed the other first
    Time to cross is calculated by the sum of steps each wire had to take
    Uses Tail Recursion Optimization on recursion
    """

    init = (0, 0)
    crossSteps = lambda idx1, idx2: idx1 + idx2 + 2

    wire1, wire2 = F.map (steps (init)) (puzzle.split ("\n"))

    # TRO
    firstCross = F.bounce (firstCrossIdx)
    crossedOn = F.bounce (crossIdx)

    # Checking speed the first wire crossed the second
    wire1Cross = firstCross (0, wire1, wire2)
    wire2Connect = crossedOn (0, wire1 [wire1Cross], wire2)

    # Checking speed the second wire crossed the first
    wire2Cross = firstCross (0, wire2, wire1)
    wire1Connect = crossedOn (0, wire2 [wire2Cross], wire1)

    # Getting the fastest of the two
    return min ([crossSteps (wire1Cross, wire2Connect), crossSteps (wire2Cross, wire1Connect)])

if __name__ == "__main__":
    from puzzleInputs import puzzle3


    # PART 1


    print (closestCross (puzzle3)) # 709


    # PART 2


    print (fastestCross (puzzle3)) # 13836
