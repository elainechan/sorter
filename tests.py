from main import sort

def test_standard():
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_bulky_by_volume():
    assert sort(100, 100, 100, 5) == "SPECIAL" # volume above threshold, dimensions not
    assert sort(150, 10, 10, 5) == "SPECIAL" # width at threshold

def test_heavy():
    assert sort(10, 10, 10, 200) == "SPECIAL" # mass above threshold, dimensions not
    assert sort(10, 10, 10, 20) == "SPECIAL" # mass at threshold

def test_rejected():
    assert sort(150, 150, 150, 20) == "REJECTED" # by volume and mass
    assert sort(10, 150, 10, 20) == "REJECTED"  # by height and mass

def test_volume_under_threshold():
    assert sort(99.99, 99.99, 99.99, 5) == "STANDARD"

def test_dimension_under_threshold():
    assert sort(149.99, 10, 10, 5) == "STANDARD" # by width
    assert sort(10, 10, 149.99, 5) == "STANDARD" # by length