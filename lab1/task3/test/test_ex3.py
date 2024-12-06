import unittest
import time
from lab1.task3.src.ex3 import reversed_insertion_sort
from lab1.utils.utils import time_memory_tracking


class TestTask3(unittest.TestCase):

    def test_should_reverse_insertion_sort0(self):
        # given
        start_time = time.perf_counter()
        arr = [4, 1, 24, 512, 5, 3]
        list_length = len(arr)
        # when
        result = reversed_insertion_sort(list_length, arr)
        # then
        self.assertEquals(result, [512, 24, 5, 4, 3, 1])
        time_memory_tracking(start_time)

    def test_should_reverse_insertion_sort1(self):
        # given
        start_time = time.perf_counter()
        arr = [-5, -10, -12034, -431, -4]
        list_length = len(arr)
        # when
        result = reversed_insertion_sort(list_length, arr)
        # then
        self.assertEquals(result, [-4, -5, -10, -431, -12034])
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()