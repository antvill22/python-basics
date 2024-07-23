from plates import is_valid

def test_plates():
    assert is_valid("CS50")==True
    assert is_valid("HELLO")==True
    assert is_valid("HE")==True
    assert is_valid("HEL")==True
    assert is_valid("HELL")==True
    assert is_valid("HELLOT")==True
    assert is_valid("CC")==True
    assert is_valid("CSP750")==True
    assert is_valid("CS9750")==True
    assert is_valid("CS50p")==False
    assert is_valid("C2")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("CS05")==False
    assert is_valid( "PI3.14")==False
    assert is_valid("H")==False
    assert is_valid(",H60")==False
    assert is_valid("00H60")==False
    assert is_valid("9OH60")==False
    assert is_valid("C90H60")==False
    assert is_valid("60")==False
