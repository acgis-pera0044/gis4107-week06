import Meng_dms_converter as dc

def test_converter1():
    expection=None,None
    actual=dc.dms2dd("91 00 00 N")
    assert expection==actual

def test_converter2():
    expection=None,None
    actual=dc.dms2dd("183 01 02 E 88 22 33 N")
    assert expection==actual

def test_converter3():
    expection=-100.0,81.0
    actual=dc.dms2dd("100 00 00 w 81 00 00 N")
    assert expection==actual

def test_converter4():
    expection=99.8,-23.6
    actual=dc.dms2dd("99 48 00 E 23 36 00 S")
    assert expection==actual

def test_converter5():
    expection=-127.78,-86.88
    actual=dc.dms2dd("127 46 48 W 86 52 48 s")
    assert expection==actual

def test_converter6():
    expection=-75.75083,45.38472
    actual=dc.dms2dd("075 45 03 W 45 23 05 N")
    assert expection==actual