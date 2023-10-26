import Meng_gpx_utils as Mgu

def test_get_coords_from_gpx_none():
    expection=None,None
    actual=Mgu.get_coords_from_gpx('yuuh asc:1111 bnh:9876')
    assert expection==actual


def test_get_coords_from_gpx_coords():
    expection='-75.7472631','45.3888995'
    actual=Mgu.get_coords_from_gpx('trkpt lat="45.3888995" lon="-75.7472631"')
    assert expection==actual