import unittest
import time
from lab2.task5.src.ex5 import majority_element
from lab2.utils.utils import time_memory_tracking


class TestMajorityElement(unittest.TestCase):
    def test_should_majority_element1(self):
        """Обычный тест"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 3, 3, 3, 3]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 3)
        time_memory_tracking(start_time)

    def test_should_majority_element2(self):
        """Тест без представителей большинства"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 0)
        time_memory_tracking(start_time)

    def test_should_majority_element3(self):
        """Тест с массивом из 1-го элемента"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 10)
        time_memory_tracking(start_time)

    def test_should_majority_element4(self):
        """Массив с одинаковыми элементами"""
        # given
        start_time = time.perf_counter()
        arr = [5, 5, 5, 5, 5]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 5)
        time_memory_tracking(start_time)

    def test_should_majority_element5(self):
        """Большой массив"""
        # given
        start_time = time.perf_counter()
        arr = [4] * 100000 + [1, 2, 3, 5, 6]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        # then
        self.assertEqual(result, 4)
        time_memory_tracking(start_time)


if __name__ == '__main__':
    unittest.main()
