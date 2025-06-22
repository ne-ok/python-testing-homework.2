from main import calculate_average

def test_positive_numbers():
    """Среднее арифметическое положительного списка"""
    assert calculate_average([1.5, 2.5, 3.5]) == 2

def test_negative_numbers():
    """Среднее арифметическое отрицательного списка"""
    assert calculate_average([-1.5, -2.5, -3.5]) == -3

def test_mixed_numbers():
    """Среднее арифметическое смешанного списка"""
    assert calculate_average([-1.5, 0, 1.5]) == 0

def test_empty_list():
    """Обработка пустого списка"""
    assert calculate_average([]) is None

def test_single_element():
    """Список с одним числом"""
    assert calculate_average([7.5]) == 7
