This repo will be used for my solutions to Advent of Code 2019
```
day3.py
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
```

```
day3 tests
import d3

def test_distance ():
    a = (5,6)
    b = (2,9)
    assert d3.distance (a) (b) == 6

def test_point ():
    assert d3.point ((2,2), "R") (1) == (3,2)
    assert d3.point ((2,2), "L") (1) == (1,2)
    assert d3.point ((2,2), "U") (1) == (2,3)
    assert d3.point ((2,2), "D") (1) == (2,1)
    assert d3.point ((2,2), "R") (3) == (5,2)
    assert d3.point ((2,2), "L") (3) == (-1,2)
    assert d3.point ((2,2), "U") (3) == (2,5)
    assert d3.point ((2,2), "D") (3) == (2,-1)

def test_points ():
    assert d3.points ((2,2), "R3") == [(3, 2), (4, 2), (5, 2)]

def test_steps ():
    assert d3.steps ((2,2)) ("R3,U2") == [
        (3, 2), (4, 2), (5, 2), (5, 3), (5, 4),
    ]

def test_closestCross ():
    tests = [
        ["R8,U5,L5,D3\nU7,R6,D4,L4", 6],
        ["R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83", 159],
        ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135],
    ]
    for test in tests:
        assert d3.closestCross (test [0]) == test [1]

def test_fastestCross ():
    tests = [
        ["R8,U5,L5,D3\nU7,R6,D4,L4", 30],
        ["R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83", 610],
        ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 410],
    ]
    for test in tests:
        assert d3.fastestCross (test [0]) == test [1]

```
