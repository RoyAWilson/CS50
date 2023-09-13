'''

Unit test number with pytest

'''

from number import square

def test_postive():
    assert square(2) == 4
    assert square(3) == 9

def test_nagative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    