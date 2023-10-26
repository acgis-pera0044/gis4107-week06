import Meng_code_parser as Mp

def test_get_db_link():
    expection="BO-642"
    actual=Mp.get_db_link("20-WBO-109642-809")
    assert expection==actual