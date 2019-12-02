from typing import List
from puzzleInputs import day2Puzzle

Intcode = List [int]

def tick (point: int, intcode: Intcode) -> Intcode:
    """ Reads next 4 ints and makes adjustments """
    opAdd = lambda a, b: intcode [a] + intcode [b]
    opMul = lambda a, b: intcode [a] * intcode [b]
    opcodes = {1: opAdd, 2: opMul}
    # opcode 99 means stop, all others is err, return is same for stop or err

    try:
        op = opcodes [intcode [point]]
    except KeyError:
        return intcode
    
    intcode [intcode [point+3]] = op (intcode [point+1], intcode [point+2])
    return tick (point + 4, intcode)

def resetProg (noun: int, verb: int, intcode: Intcode) -> Intcode:
    prog = intcode.copy ()
    prog [1] = noun
    prog [2] = verb
    return prog

print (tick (0, resetProg (12, 2, day2Puzzle)) [0])


# PART 2


def answer (noun: int, verb: int) -> int:
    return 100 * noun + verb

def nounVerbSearch (goal):
    for x in range (99):
        for y in range (99):
            output = tick (0, resetProg (x, y, day2Puzzle))
            if output [0] == goal:
                return answer (x, y)
    return None

print (nounVerbSearch (19690720))
