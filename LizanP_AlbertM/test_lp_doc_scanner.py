import lp_doc_scanner as ds

def text_has_x_code_1():
    text = "GTx6op3"
    expected = True
    actual = ds.has_x_code(text)
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
    expected = True
    actual = ds.has_x_code(text)
    assert expected == actual