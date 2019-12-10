import intcodeCPU as cpu

def test_paramcodes ():
    assert cpu.paramcodes (12302, 4) == [3,2,1,0]
    assert cpu.paramcodes (12302, 2) == [3,2]
    assert cpu.paramcodes (2302, 2) == [3,2]

def test_paramVal ():
    code = [1,2,3,4]
    assert cpu.paramVal (code, 0, [0,1]) (2) == 3
    assert cpu.paramVal (code, 0, [1,0]) (2) == 4

def test_addMult ():
    tests = [
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
        {
            "in": [1,9,10,3,2,3,11,0,99,30,40,50],
            "out": [3500,9,10,70,2,3,11,0,99,30,40,50],
        },
    ]
    for test in tests:
        assert cpu.tick (0, test ["in"]) == test ["out"]

# def test_opIn ():
#     assert cpu.tick (0, [3, 2, 6]) == [3, 2, 5]
