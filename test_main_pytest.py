from main import calculate_average

def test_positive_numbers():
    assert calculate_average([1.5, 2.5, 3.5]) == 2

def test_negative_numbers():
    assert calculate_average([-1.5, -2.5, -3.5]) == -3

def test_empty_list():
    assert calculate_average([]) is None