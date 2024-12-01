import unittest
import random
import time

from lab3.task4.src.ex4 import lottery
from lab3.utils.utils import time_memory_tracking


class TestLotteryFunction(unittest.TestCase):

    def test_should_lottery1(self):
        """базовый"""
        # given
        data = [
            (3, 3),
            (1, 5),
            (2, 6),
            (3, 7),
            [2, 4, 6]
        ]
        expected_result = [2, 3, 2]

        # when
        result = lottery(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_lottery2(self):
        """отрезки не пересекаются с точками"""
        # given
        data = [
            (2, 3),
            (1, 2),
            (5, 6),
            [3, 4, 7]
        ]
        expected_result = [0, 0, 0]

        # when
        result = lottery(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_lottery3(self):
        """все точки внутри одного отрезка"""
        # given
        data = [
            (1, 3),
            (0, 10),
            [1, 5, 9]
        ]
        expected_result = [1, 1, 1]

        # when
        result = lottery(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_lottery4(self):
        """точки находятся на границах отрезков"""
        # given
        data = [
            (2, 3),
            (1, 3),
            (3, 6),
            [3, 4, 5]
        ]
        expected_result = [2, 1, 1]

        # when
        result = lottery(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_lottery5(self):
        """случай с большими входными данными для проверки производительности"""
        # given
        s, p = 100000, 100000
        segments = [(i, i + 10) for i in range(0, s * 10, 10)]
        points = [i for i in range(5, s * 10, 10)]

        expected_result = [1] * p
        data = [(s, p)] + segments + [points]
        start_time = time.perf_counter()

        # when
        result = lottery(data)

        # then
        self.assertEqual(result, expected_result)
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()
