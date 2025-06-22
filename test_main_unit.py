import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    
    def test_positive_numbers(self):
        numbers = [1.5, 2.5, 3.5]
        self.assertEqual(calculate_average(numbers), 2)  # Положительные числа

    def test_negative_numbers(self):
        numbers = [-1.5, -2.5, -3.5]
        self.assertEqual(calculate_average(numbers), -3) # Отрицательные числа

    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-1.5, 0, 1.5]), 0) # Смешанные числа

    def test_empty_list(self):
        self.assertIsNone(calculate_average([])) # Пустой список
        
    def test_single_element(self):
        self.assertEqual(calculate_average([7.5]), 7) # Единичный элемент

if __name__ == '__main__':
    unittest.main()
