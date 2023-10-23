import lp_code_parser as cp

def test_get_db_link():
    code = "20-WBO-109642-809"
    expected = "BO-642"
    actual = cp.get_db_link(code)
    assert expected == actual