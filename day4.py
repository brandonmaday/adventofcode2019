import funpy as F
from puzzleInputs import puzzle4
from typing import Callable


# PART 1 FILTERS


def doubles (p: str) -> bool:
    """ password has at least two repeated numbers """
    for i, l in enumerate (p):
        try:
            if l == p [i +1]:
                return True
        except IndexError:
            return False
    return False

def noShrink (p: str) -> bool:
    """ password numbers are the same or larger than those to their left """
    for i, l in enumerate (p):
        try:
            if l > p [i +1]:
                return False
        except IndexError:
            return True
    return True


# PART 2 FILTERS


def nth (p: str) -> Callable [[int], str]:
    """ nth array value or 'E' if index not present """
    def wrap (i: int) -> str:
        try:
            return p [i]
        except IndexError:
            return "E"
    return wrap

def strictDoubles (p: str) -> bool:
    """ password has at least one number repreated exactly 2 times """
    v = nth (p)
    for i, l in enumerate (p):
        if l == v (i+1) and l != v (i-1) and l != v (i+2):
            return True
    return False


# PUZZLE INPUT


""" normalize : generator -> List [str] """
normalize = F.compose (F.map (str), list)
passwords = normalize (range (puzzle4 [0], puzzle4 [1]+1))


# COMMON FILTER


shrinkCheck = F.filter (noShrink)


# PART 1


print (len (shrinkCheck (F.filter (doubles) (passwords)))) #1653


# PART 2


print (len (shrinkCheck (F.filter (strictDoubles) (passwords)))) #1133
