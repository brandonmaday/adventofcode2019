import funpy as F
from typing import List, TypedDict, Callable, List
from puzzleInputs import day2Puzzle


# TYPES


Intcode = List [int]

Paramval = Callable [[int], int]

Paramcodes = List [int]


# PARAMCODES


def paramcodes (code: int, arity: int) -> Paramcodes:
    codes = str (code) [:-2] [::-1]
    filling = "".join (["0" for a in  range (arity - len (codes))])
    filled = codes + filling
    return [int (c) for c in filled [:arity]]

def paramVal (intcode: Intcode, point: int, pcodes: Paramcodes) -> Paramval:
    def wrap (loc: int) -> int:
        paramFn = [
            lambda code, loc: code [code [loc]],
            lambda code, loc: code [loc]
        ]
        return paramFn [pcodes [loc-1]] (intcode, point + loc)
    return wrap


# OPCODES


def opcode (code: int):
    return int (str (code) [-2:])

def opfn (arity: int, fn: Callable [[Intcode, int], None]) -> dict:
    return {"arity": arity, "fn": fn}

def opAdd (intcode: Intcode, point: int, param: Paramval) -> Intcode:
    intcode [intcode [point+3]] = param (1) + param (2)
    return intcode

def opMult (intcode: Intcode, point: int, param: Paramval) -> Intcode:
    intcode [intcode [point+3]] =  param (1) * param (2)
    return intcode

def opIn (intcode: Intcode, point: int, param: Paramval) -> Intcode:
    intcode [intcode [point + 1]] = int (input ("Please enter a value: "))
    return intcode

def opOut (intcode: Intcode, point: int, param: Paramval) -> Intcode:
    print (param (1))
    return intcode

opfns = {
    1: opfn (3, opAdd),
    2: opfn (3, opMult),
    3: opfn (1, opIn),
    4: opfn (1, opOut),
}


# CPU


def tick (point: int, intcode: Intcode) -> Intcode:
    """ Reads next 4 ints and makes adjustments """
    # opcode 99 means stop, all others is err, return is same for both

    opIns = intcode [point]

    try:
        op = opfns [opcode (opIns)]
    except KeyError:
        return intcode
    
    param = paramVal (intcode, point, paramcodes (opIns, op ["arity"]))
    intcode = op ["fn"] (intcode, point, param)
    return tick (point + 1 + op ["arity"], intcode)

def resetProg (noun: int, verb: int, intcode: Intcode) -> Intcode:
    prog = intcode.copy ()
    prog [1] = noun
    prog [2] = verb
    return prog
