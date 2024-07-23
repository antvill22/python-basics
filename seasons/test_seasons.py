import seasons
from datetime import date

def test_get_birth_date_valid_input():
    assert seasons.get_birth_date('1990-01-01') == date(1990, 1, 1)

def test_get_birth_date_invalid_input():
    try:
        seasons.get_birth_date('invalid_date')
    except SystemExit:
        pass  # Expecting sys.exit() for invalid input

def test_calculate_age_in_minutes():
    birth_date = date(1990, 1, 1)
    current_date=date(2024, 3, 9)
    assert seasons.calculate_age_in_minutes(birth_date,current_date) == 17979840

def test_convert_to_words():
    assert seasons.convert_to_words(12345) == "twelve thousand, three hundred forty-five"
    assert seasons.convert_to_words(0) == "zero"
    assert seasons.convert_to_words(100) == "one hundred"
    assert seasons.convert_to_words(1000000) == "one million"
    assert seasons.convert_to_words(999999999) == "nine hundred ninety-nine million, nine hundred ninety-nine thousand, nine hundred ninety-nine"


# Add more test functions as needed

if __name__ == "__main__":
    test_get_birth_date_valid_input()
    test_get_birth_date_invalid_input()
    test_calculate_age_in_minutes()
    test_convert_to_words()
    # Call other test functions as needed
    print("All tests passed!")
