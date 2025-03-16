import unittest
import time
from lab1.task4.src.ex4 import linear_search
from FirstSemester.lab1.utils.utils import time_memory_tracking1


class TestFirst(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_linear_search0(self):
        # given
        start_time = time.perf_counter()
        arr = [234, 325, 5, 1, -6, 0]
        v = 5
        # when
        result = linear_search(v, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 2)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_linear_search1(self):
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        # when
        result = linear_search(v, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 6)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_linear_search(self):
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        # when
        result = linear_search(v, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, ([6, 7, 8], 3))
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
