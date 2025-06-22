
import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):

    def test_positive_numbers(self):
        """Среднее арифметическое положительного списка."""
        numbers = [1.5, 2.5, 3.5]
        expected_result = 2  # округляем вниз до целого
        actual_result = calculate_average(numbers)
        self.assertEqual(expected_result, actual_result)

    def test_negative_numbers(self):
        """Среднее арифметическое отрицательного списка."""
        numbers = [-1.5, -2.5, -3.5]
        expected_result = -3  # округляем вниз до целого
        actual_result = calculate_average(numbers)
        self.assertEqual(expected_result, actual_result)

    def test_mixed_numbers(self):
        """Среднее арифметическое смешанного списка."""
        numbers = [-1.5, 0, 1.5]
        expected_result = 0  # округляем вниз до целого
        actual_result = calculate_average(numbers)
        self.assertEqual(expected_result, actual_result)

    def test_empty_list(self):
        """Обработка пустого списка."""
        numbers = []
        expected_result = None
        actual_result = calculate_average(numbers)
        self.assertIsNone(actual_result)

    def test_single_element(self):
        """Список с одним числом."""
        numbers = [7.5]
        expected_result = 7  # округляем вниз до целого
        actual_result = calculate_average(numbers)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()