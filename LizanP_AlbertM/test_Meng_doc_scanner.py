import Meng_doc_scanner as Mds

def test_has_x_code():
    expection=True
    actual=Mds.has_x_code("ABmaTx6op34")
    assert expection==actual


def test_get_x_code_position():
    expection=3
    actual=Mds.get_x_code_position("A1Tx6op301")
    assert expection==actual

