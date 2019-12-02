from day2 import tick, answer

def test_tick ():
    tests = [
        {
            "in": [1,9,10,3,2,3,11,0,99,30,40,50],
            "out": [3500,9,10,70,2,3,11,0,99,30,40,50],
        },
        {
            "in": [1,0,0,0,99],
            "out": [2,0,0,0,99],
        },
        {
            "in": [2,3,0,3,99],
            "out": [2,3,0,6,99],
        },
        {
            "in": [2,4,4,5,99,0],
            "out": [2,4,4,5,99,9801],
        },
        {
            "in": [1,1,1,4,99,5,6,0,99],
            "out": [30,1,1,4,2,5,6,0,99],
        },
    ]
    for test in tests:
        assert tick (0, test ["in"]) == test ["out"]

def test_answer ():
    assert answer (12, 2) == 1202
