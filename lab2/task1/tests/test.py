import unittest
from lab2.task1.first import merge_sort


class TestFirstTask(unittest.TestCase):
    pass


with open("test_data.txt", "r") as f:
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
        test_name = f"test_should_merge_sort{i+1}"
        test_should_merge_sort = create_test_function(unsorted, expected)
        setattr(TestFirstTask, test_name, test_should_merge_sort)
if __name__ == "__main__":
    unittest.main()

