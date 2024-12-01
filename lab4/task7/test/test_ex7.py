import unittest
import time
from lab4.utils.utils import time_memory_tracking
from ..src.ex7 import max_in_window


class TestMaxInWindow(unittest.TestCase):

    def test_should_return_correct_result1(self):
        """Базовый случай с окном размера 3"""
        # given
        n = 8
        arr = [1, 3, -1, -3, 5, 3, 6, 7]
        m = 3
        expected_result = [3, 3, 5, 5, 6, 7]

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_result2(self):
        """Случай, где длина окна равна длине массива"""
        # given
        n = 5
        arr = [4, 2, 12, 3, 8]
        m = 5
        expected_result = [12]

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_result3(self):
        """Случай с одним элементом в окне"""
        # given
        n = 5
        arr = [4, 2, 12, 3, 8]
        m = 1
        expected_result = [4, 2, 12, 3, 8]

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_result4(self):
        """Случай с повторяющимися элементами"""
        # given
        n = 6
        arr = [5, 5, 5, 5, 5, 5]
        m = 3
        expected_result = [5, 5, 5, 5]

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_data(self):
        """Случай с большими данными для проверки производительности"""
        # given
        n = 10000
        arr = list(range(10000))  # [0, 1, 2, ..., 9999]
        m = 100
        expected_result = list(range(99, 10000))
        start_time = time.perf_counter()

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)
        time_memory_tracking(start_time)

    def test_should_return_empty_for_small_array(self):
        """Случай, когда размер окна больше размера массива"""
        # given
        n = 3
        arr = [1, 2, 3]
        m = 5
        expected_result = []

        # when
        result = max_in_window(n, arr, m)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()