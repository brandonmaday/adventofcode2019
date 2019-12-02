from typing import List, TypedDict
from c1Stdin import puzzleInput


# CHALLENGE ONE


def parsePuzzleIn (modules: str) -> List [int]:
    """ Gets puzzle input data in a usable type """
    return [int (m) for m in modules.split ("\n")]

def moduleFule (mass: int) -> int:
    """ Calculates the Fuel of a mass """
    fuel = (mass // 3) - 2
    return 0 if fuel < 0 else fuel

def totalFule (tot, mass) -> int:
    """ Reducer that recursivley calculates fuel of fuel """
    fuel = moduleFule (mass)
    if fuel == 0:
        return tot
    return totalFule (tot + fuel, fuel)


# SOLUTION - PART 1


print (sum([moduleFule (m) for m in parsePuzzleIn (puzzleInput)]))


# SOLUTION - PART 2


print (sum([totalFule (0, m) for m in parsePuzzleIn (puzzleInput)]))
