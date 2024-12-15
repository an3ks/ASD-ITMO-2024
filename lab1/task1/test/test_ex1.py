import unittest
import time
from lab1.task1.src.ex1 import insertion_sort
from lab1.utils.utils import time_memory_tracking1


class TestFirst(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_insertion_sort0(self):
        # given
        start_time = time.perf_counter()
        arr = [234, 325, 5, 1, -6, 0]
        list_length = len(arr)
        # when
        result = insertion_sort(list_length, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, [-6, 0, 1, 5, 234, 325])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_insertion_sort1(self):
        # given
        start_time = time.perf_counter()
        arr = [-1, -5, 5, 5, 3, -3]
        list_length = len(arr)
        # when
        result = insertion_sort(list_length, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, [-5, -3, -1, 3, 5, 5])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
