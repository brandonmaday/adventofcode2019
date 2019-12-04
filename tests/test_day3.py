import day3 as d3

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
