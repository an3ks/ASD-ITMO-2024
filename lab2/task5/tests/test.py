import unittest
from lab2.task5.src.fifth import majority_element


class TestMajorityElement(unittest.TestCase):
    def test_should_majority_element_majority_element_exists(self):
        """Обычный тест"""
        # given
        arr = [1, 2, 3, 3, 3, 3, 3]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 3)

    def test_should_majority_element_no_majority_element(self):
        """Тест без представителей большинства"""
        # given
        arr = [1, 2, 3, 4, 5, 6, 7]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 0)

    def test_should_majority_element_single_element_array(self):
        """Тест с массивом из 1-го элемента"""
        # given
        arr = [10]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 10)

    def test_should_majority_element_all_elements_same(self):
        """Массив с одинаковыми элементами"""
        # given
        arr = [5, 5, 5, 5, 5]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 5)

    def test_should_majority_element_large_array(self):
        """Большой массив"""
        # given
        arr = [4] * 100000 + [1, 2, 3, 5, 6]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
