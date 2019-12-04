import day4 as d4

def test_doubles ():
    assert d4.doubles ("1113311") == True
    assert d4.doubles ("1234561") == False
    assert d4.doubles ("12344561") == True

def test_noShrink ():
    assert d4.noShrink ("12344567") == True
    assert d4.noShrink ("12344367") == False

def test_strictDoubles ():
    assert d4.strictDoubles ("1113311") == True
    assert d4.strictDoubles ("1113481") == False
    assert d4.strictDoubles ("1113222") == False
    assert d4.strictDoubles ("1234561") == False
    assert d4.strictDoubles ("12344561") == True
    assert d4.strictDoubles ("11345678") == True
    assert d4.strictDoubles ("12345677") == True

