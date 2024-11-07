import unittest
from lab2.task5.src.fifth import majority_element


class TestMajorityElement(unittest.TestCase):
    def test_majority_element_exists(self):
        """Обычный тест"""
        arr = [1, 2, 3, 3, 3, 3, 3]
        result = majority_element(arr, 0, len(arr) - 1)
        self.assertEqual(result, 3)

    def test_no_majority_element(self):
        """Тест без представителей большинства"""
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = majority_element(arr, 0, len(arr) - 1)
        self.assertEqual(result, 0)

    def test_single_element_array(self):
        """Тест с массивом из 1-го элемента"""
        arr = [10]
        result = majority_element(arr, 0, len(arr) - 1)
        self.assertEqual(result, 10)

    def test_all_elements_same(self):
        """Массив с одинаковыми элементами"""
        arr = [5, 5, 5, 5, 5]
        result = majority_element(arr, 0, len(arr) - 1)
        self.assertEqual(result, 5)

    def test_large_array(self):
        """Большой массив"""
        arr = [4] * 100000 + [1, 2, 3, 5, 6]
        result = majority_element(arr, 0, len(arr) - 1)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()