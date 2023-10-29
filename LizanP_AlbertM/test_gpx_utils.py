import gpx_utils as gu

def test_get_coords_from_gpx_1():
    gpx = '<trkpt lat="45.3888995" lon="-75.7472631">'
    expected_longitude = -75.7472631
    expected_latitude = 45.3888995
    actual_longitude, actual_latitude = gu.get_coords_from_gpx(gpx)
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_get_coords_from_gpx_2():
    gpx = '<lat="45.3888995" lon="-75.7472631">'
    expected_longitude = None
    expected_latitude = None
    actual_longitude, actual_latitude = gu.get_coords_from_gpx(gpx)
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_get_coords_from_gpx_3():
    gpx = '<trkpt lat="-45.3888995" lon="-75.74726311234">'
    expected_longitude = -75.74726311234
    expected_latitude = -45.3888995
    actual_longitude, actual_latitude = gu.get_coords_from_gpx(gpx)
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_get_coords_from_gpx_4():
    gpx = '<trkpt lat="45.38889951234" lon="75.7472631">'
    expected_longitude = 75.7472631
    expected_latitude = 45.38889951234
    actual_longitude, actual_latitude = gu.get_coords_from_gpx(gpx)
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude

def test_get_coords_from_gpx_5():
    gpx = '<trkpt lat="45.38889951234" lon="-75.74726311234">'
    expected_longitude = -75.74726311234
    expected_latitude = 45.38889951234
    actual_longitude, actual_latitude = gu.get_coords_from_gpx(gpx)
    assert expected_longitude == actual_longitude
    assert expected_latitude == actual_latitude