import unittest
import time
from FirstSemester.lab5 import time_memory_tracking1
from FirstSemester.lab5.task2 import calculate_tree_height


class TestCalculateTreeHeight(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_calculate_height1(self):
        """Базовый случай: дерево с 5 узлами"""
        # given
        n = 5
        parents = [4, -1, 4, 1, 1]
        expected_result = 3

        # when
        start_time = time.perf_counter()
        result = calculate_tree_height(n, parents)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_calculate_height2(self):
        """Случай с одним узлом"""
        # given
        n = 1
        parents = [-1]
        expected_result = 1

        # when
        start_time = time.perf_counter()
        result = calculate_tree_height(n, parents)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_should_calculate_height3(self):
        """Случай с деревом глубиной 2"""
        # given
        n = 3
        parents = [-1, 0, 0]
        expected_result = 2

        # when
        start_time = time.perf_counter()
        result = calculate_tree_height(n, parents)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_should_calculate_height5(self):
        """Случай с максимальным количеством узлов для проверки производительности"""
        # given
        n = 100000
        parents = [-1] + [0] * (n - 1)  # Дерево с глубиной 2
        expected_result = 2

        # when
        start_time = time.perf_counter()
        result = calculate_tree_height(n, parents)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
