import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        """Среднее арифметическое положительного списка"""
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2)

    def test_negative_numbers(self):
        """Среднее арифметическое отрицательного списка"""
        self.assertEqual(calculate_average([-1.5, -2.5, -3.5]), -3)

    def test_mixed_numbers(self):
        """Среднее арифметическое смешанного списка"""
        self.assertEqual(calculate_average([-1.5, 0, 1.5]), 0)

    def test_empty_list(self):
        """Обработка пустого списка"""
        self.assertIsNone(calculate_average([]))

    def test_single_element(self):
        """Список с одним числом"""
        self.assertEqual(calculate_average([7.5]), 7)

if __name__ == '__main__':
    unittest.main()
