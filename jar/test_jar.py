from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(7)
    assert jar.size == 12
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    # Test deposit exceeding capacity
    try:
        jar.deposit(1)
    except ValueError as e:
        assert str(e) == "Deposit would exceed the jar's capacity."


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    try:
        jar.withdraw(7)
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar to withdraw."
