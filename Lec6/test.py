
def test_biggestInt1():
    assert biggestInt(1,2,3,4) == 4
    assert biggestInt(1,2,4,3) == 4
    assert biggestInt(1,4,2,3) == 4

def test_biggestInt2():
    assert biggestInt(5,5,5,5) == 5

def test_biggestInt3():
    assert biggestInt(-5,-10,-11,-100) == -5



def biggestInt(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d