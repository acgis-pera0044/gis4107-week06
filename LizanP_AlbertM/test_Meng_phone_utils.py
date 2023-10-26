import Meng_phone_utils as Mpu

def test_is_valid_phone_number_False1():
    expection=False
    actual=Mpu.is_valid_phone_number("ABC-ABC-DEFD")
    assert expection==actual 

def test_is_valid_phone_number_False2():
    expection=False
    actual=Mpu.is_valid_phone_number("1234567890")
    assert expection==actual 

def test_is_valid_phone_number_False3():
    expection=False
    actual=Mpu.is_valid_phone_number("123-3444-123")
    assert expection==actual 

def test_is_valid_phone_number_True1():
    expection=True
    actual=Mpu.is_valid_phone_number("123-456-7890")
    assert expection==actual 

def test_is_valid_phone_number_True2():
    expection=True
    actual=Mpu.is_valid_phone_number("000-111-0000")
    assert expection==actual 
