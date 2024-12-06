import unittest
import time
from lab1.task4.src.ex4 import linear_search
from lab1.utils.utils import time_memory_tracking


class TestFirst(unittest.TestCase):

    def test_should_linear_search0(self):
        # given
        start_time = time.perf_counter()
        arr = [234, 325, 5, 1, -6, 0]
        v = 5
        # when
        result = linear_search(v, arr)
        # then
        self.assertEqual(result, 2)
        time_memory_tracking(start_time)

    def test_should_linear_search1(self):
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        # when
        result = linear_search(v, arr)
        # then
        self.assertEqual(result, 6)
        time_memory_tracking(start_time)

    def test_should_linear_search(self):
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        # when
        result = linear_search(v, arr)
        # then
        self.assertEqual(result, ([6, 7, 8], 3))
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()
