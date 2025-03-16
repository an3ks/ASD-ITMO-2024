import unittest
import random
import time

from lab3.task4.src.ex4 import lottery
from lab3.utils.utils import time_memory_tracking1


class TestLotteryFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_lottery1(self):
        """базовый"""
        # given
        start_time = time.perf_counter()
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
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_lottery2(self):
        """отрезки не пересекаются с точками"""
        # given
        start_time = time.perf_counter()
        data = [
            (2, 3),
            (1, 2),
            (5, 6),
            [3, 4, 7]
        ]
        expected_result = [0, 0, 0]

        # when
        result = lottery(data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_lottery3(self):
        """все точки внутри одного отрезка"""
        # given
        start_time = time.perf_counter()
        data = [
            (1, 3),
            (0, 10),
            [1, 5, 9]
        ]
        expected_result = [1, 1, 1]

        # when
        result = lottery(data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_lottery4(self):
        """точки находятся на границах отрезков"""
        # given
        start_time = time.perf_counter()
        data = [
            (2, 3),
            (1, 3),
            (3, 6),
            [3, 4, 5]
        ]
        expected_result = [2, 1, 1]

        # when
        result = lottery(data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


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
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
