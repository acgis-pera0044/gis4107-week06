import lp_dms_converter as dc

def test_dms2dd_1():
    coordinates = "075 45 03 e 45 23 05 s"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = 75.75083
    expected_latitude = -45.38472
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_dms2dd_2():
    coordinates = "075 45 03 W 45 23 05 N"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = -75.75083
    expected_latitude = 45.38472
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_dms2dd_3():
    coordinates = "075 45 03 W 91 23 05 N"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = None
    expected_latitude = None
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_dms2dd_4():
    coordinates = "075 45 03 w 45 23 05 s"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = -75.75083
    expected_latitude = -45.38472
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_dms2dd_5():
    coordinates = "181 45 03 W 90 23 05 N"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = None
    expected_latitude = None
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude


def test_dms2dd_6():
    coordinates = "180 00 00 W 90 00 00 N"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = -180.00000
    expected_latitude = 90.00000
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_dms2dd_7():
    coordinates = "180 45 03 W 90 23 60 N"
    actual_longitude, actual_latitude = dc.dms2dd(coordinates)
    expected_longitude = None
    expected_latitude = None
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude