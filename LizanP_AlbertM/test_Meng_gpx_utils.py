import Meng_gpx_utils as Mgu

def test_get_coords_from_gpx_none():
    expection=None,None
    actual=Mgu.get_coords_from_gpx('<lat="45.3888995" lon="-75.7472631">')
    assert expection==actual

def test_get_coords_from_gpx_coords():
    expection='-75.7472631','45.3888995'
    actual=Mgu.get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">')
    assert expection==actual

def test_get_coords_from_gpx_2():
    expection='-75.7472631','45.38889951234'
    actual=Mgu.get_coords_from_gpx('<trkpt lat="45.38889951234" lon="-75.7472631">')
    assert expection==actual

def test_get_coords_from_gpx_3():
    expection='-75.74726311234','45.3888995'
    actual=Mgu.get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.74726311234">')
    assert expection==actual