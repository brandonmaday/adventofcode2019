import c1

def test_moduleFule ():
    assert c1.moduleFule (12) == 2
    assert c1.moduleFule (14) == 2
    assert c1.moduleFule (1969) == 654
    assert c1.moduleFule (100756) == 33583

def test_FuleFule ():
    assert c1.totalFule (0, 2) == 0
    assert c1.totalFule (0, 1969) == 966
    assert c1.totalFule (0, 100756) == 50346
