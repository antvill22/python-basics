import um

def test_count_no_um():
    assert um.count("Hello, world!") == 0

def test_count_one_um():
    assert um.count("Um, what do you think?") == 1

def test_count_multiple_um():
    assert um.count("Um, um, um, excuse me!") == 3

def test_count_mixed_case():
    assert um.count("uM, uM, uM, um!") == 4

def test_count_um_in_words():
    assert um.count("Album, umbrella, drums.") == 0

def test_count_um_with_punctuation():
    assert um.count("Well, um, that's interesting!") == 1
