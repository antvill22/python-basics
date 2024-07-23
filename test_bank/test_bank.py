from bank import value

def main():
    test_bank()


def test_bank():
    assert value("HELLO!")== 0
    assert value("Hello, beauty!")== 0
    assert value("Hello world!")== 0
    assert value("What’s up!")== 100
    assert value("FalSe")== 100
    assert value("DENMARK")== 100
    assert value("jigsaw2")==100
    assert value("what's up! hawdy!")==100
    assert value("hawdy!")==20
    assert value("HAWDY!")==20
    assert value("Hamburger")==20
    assert value("horse to you!")==20


if __name__ == "__main__":
    main()
