import lp_dms_converter as dc

def test_dms2dd_1():
    coordinates = "075 45 03 e 45 23 05 s"
    expected = "(75.75083,-45.38472)"
    actual = dc.dms2dd(coordinates)
    assert expected == actual

def test_dms2dd_2():
    coordinates = "075 45 03 W 45 23 05 N"
    expected = "(-75.75083,45.38472)"
    actual = dc.dms2dd(coordinates)
    assert expected == actual

def test_dms2dd_3():
    coordinates = "075 45 03 W 91 23 05 N"
    expected = (None, None)
    actual = dc.dms2dd(coordinates)
    assert expected == actual

def test_dms2dd_4():
    coordinates = "075 45 03 w 45 23 05 s"
    expected = "(-75.75083,-45.38472)"
    actual = dc.dms2dd(coordinates)
    assert expected == actual

def test_dms2dd_5():
    coordinates = "181 45 03 W 90 23 05 N"
    expected = (None, None)
    actual = dc.dms2dd(coordinates)
    assert expected == actual


def test_dms2dd_6():
    coordinates = "180 00 00 W 90 00 00 N"
    expected = "(-180.00000,90.00000)"
    actual = dc.dms2dd(coordinates)
    assert expected == actual

def test_dms2dd_7():
    coordinates = "180 45 03 W 90 23 60 N"
    expected = (None, None)
    actual = dc.dms2dd(coordinates)
    assert expected == actual