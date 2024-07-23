import pytest
from working import convert

def test_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_formats_late_hours():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_invalid_input_format():
    with pytest.raises(ValueError):
        convert("invalid format")

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("12:60 PM to 1:00 PM")

def test_valid_format_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_format_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_format_3():
    assert convert("11:30 AM to 7:30 PM") == "11:30 to 19:30"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 13:60 PM")