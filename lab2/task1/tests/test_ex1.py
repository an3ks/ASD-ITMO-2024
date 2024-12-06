import unittest
import time
from lab2.task1.src.ex1 import merge_sort
from lab2.utils.utils import time_memory_tracking


class TestFirstTask(unittest.TestCase):
    pass


with open("test_data.txt", "r") as f:
    # given
    start_time = time.perf_counter()
    for i, line in enumerate(f):
        if line.startswith("#") or not line.strip():
            continue

        unsorted_str, expected_str = line.strip().split("|")
        unsorted = list(map(int, unsorted_str.split(",")))
        expected = list(map(int, expected_str.split(",")))


        def create_test_function(unsorted, expexted):
            def test_should_merge_sort(self):
                merge_sort(unsorted)
                self.assertEquals(unsorted, expexted)

            return test_should_merge_sort


        test_name = f"test_should_merge_sort{i + 1}"
        # when
        test_should_merge_sort = create_test_function(unsorted, expected)
        # then
        setattr(TestFirstTask, test_name, test_should_merge_sort)
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()
