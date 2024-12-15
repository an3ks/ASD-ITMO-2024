import unittest
import time
from lab1.task3.src.ex3 import reversed_insertion_sort
from lab1.utils.utils import time_memory_tracking1


class TestTask3(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_reverse_insertion_sort0(self):
        # given
        start_time = time.perf_counter()
        arr = [4, 1, 24, 512, 5, 3]
        list_length = len(arr)
        # when
        result = reversed_insertion_sort(list_length, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEquals(result, [512, 24, 5, 4, 3, 1])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_reverse_insertion_sort1(self):
        # given
        start_time = time.perf_counter()
        arr = [-5, -10, -12034, -431, -4]
        list_length = len(arr)
        # when
        result = reversed_insertion_sort(list_length, arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEquals(result, [-4, -5, -10, -431, -12034])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()