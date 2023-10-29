import doc_scanner as ds

def test_has_x_code_1():
    in_text = "hzsfsdgsTx6op3gghfjr"
    expected = True
    actual = ds.has_x_code(in_text)
    assert expected == actual

def test_has_x_code_2():
    text = "Tx6op3A"
    expected = True
    actual = ds.has_x_code(text)
    assert expected == actual

def test_has_x_code_3():
    text = "GTx6op3"
    expected = True
    actual = ds.has_x_code(text)
    assert expected == actual

def test_has_x_code_4():
    text = "Tx6op3"
    expected = True
    actual = ds.has_x_code(text)
    assert expected == actual

def test_has_x_code_5():
    text = "tx6op3h"
    expected = False
    actual = ds.has_x_code(text)
    assert expected == actual

def test_get_x_code_position_1():
    in_text = "hzsTx6op3gghfjr"
    expected = 4
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

def test_get_x_code_position_2():
    in_text = "Tx6op3A"
    expected = 1
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

def test_get_x_code_position_3():
    in_text = "GTx6op3"
    expected = 2
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

def test_get_x_code_position_4():
    in_text = "Tx6op3"
    expected = 1
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

def test_get_x_code_position_5():
    in_text = "tx6op3h"
    expected = -1
    actual = ds.get_x_code_position(in_text)
    assert expected == actual