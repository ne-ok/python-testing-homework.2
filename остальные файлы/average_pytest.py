
from main import calculate_average

def test_positive_numbers():
    """Среднее арифметическое положительного списка."""
    numbers = [1.5, 2.5, 3.5]
    expected_result = 2  # округляем вниз до целого
    actual_result = calculate_average(numbers)
    assert expected_result == actual_result

def test_negative_numbers():
    """Среднее арифметическое отрицательного списка."""
    numbers = [-1.5, -2.5, -3.5]
    expected_result = -3   # округляем вниз до целого
    actual_result = calculate_average(numbers)
    assert expected_result == actual_result

def test_mixed_numbers():
    """Среднее арифметическое смешанного списка."""
    numbers = [-1.5, 0, 1.5]
    expected_result = 0   # округляем вниз до целого
    actual_result = calculate_average(numbers)
    assert expected_result == actual_result

def test_empty_list():
    """Обработка пустого списка."""
    numbers = []
    expected_result = None
    actual_result = calculate_average(numbers)
    assert actual_result is None

def test_single_element():
    """Список с одним числом."""
    numbers = [7.5]
    expected_result = 7   # округляем вниз до целого
    actual_result = calculate_average(numbers)
    assert expected_result == actual_result