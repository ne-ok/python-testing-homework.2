import unittest

class TestArithmeticOperations(unittest.TestCase):

    def test_addition(self):
        """Проверяем операцию сложения"""
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        """Проверяем операцию вычитания"""
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()