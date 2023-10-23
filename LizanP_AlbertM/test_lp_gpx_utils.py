import lp_gpx_utils as gu

def test_get_coords_from_gpx_1():
    gpx = '<trkpt lat="45.3888995" lon="-75.7472631">'
    expected = "(-75.7472631,45.3888995)"
    actual = gu.get_coords_from_gpx(gpx)
    assert expected == actual

def test_get_coords_from_gpx_2():
    gpx = '<lat="45.3888995" lon="-75.7472631">'
    expected = (None, None)
    actual = gu.get_coords_from_gpx(gpx)
    assert expected == actual

def test_get_coords_from_gpx_3():
    gpx = '<trkpt lat="45.38889951234" lon="-75.7472631">'
    expected = "(-75.7472631,45.38889951234)"
    actual = gu.get_coords_from_gpx(gpx)
    assert expected == actual

def test_get_coords_from_gpx_4():
    gpx = '<trkpt lat="45.3888995" lon="-75.74726311234">'
    expected = "(-75.74726311234,45.3888995)"
    actual = gu.get_coords_from_gpx(gpx)
    assert expected == actual