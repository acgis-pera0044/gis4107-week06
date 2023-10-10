import lp_phone_utils as pu

def test_is_valid_phone_number_1():
    phone_number = "123-456-7890"
    expected = True
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_2():
    phone_number = "123-456-789"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_3():
    phone_number = "1237456-7890"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_4():
    phone_number = "1*3-456-7890"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_5():
    phone_number = "123-456-78901"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual