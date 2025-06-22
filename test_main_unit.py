import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        numbers = [1.5, 2.5, 3.5]
        self.assertEqual(calculate_average(numbers), 2)

    def test_negative_numbers(self):
        numbers = [-1.5, -2.5, -3.5]
        self.assertEqual(calculate_average(numbers), -3)

    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))

if __name__ == '__main__':
    unittest.main()