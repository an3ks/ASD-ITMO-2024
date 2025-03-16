import unittest
import time
from FirstSemester.lab4.utils.utils import time_memory_tracking1
from FirstSemester.lab4.task6.src.ex6 import queue_min


class TestQueueMin(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_process_simple_operations(self):
        """Простой случай: добавление, удаление и поиск минимума"""
        # given
        n = 6
        commands = [
            ["+", "3"],
            ["+", "1"],
            ["?", ""],
            ["-", ""],
            ["?", ""],
            ["+", "2"]
        ]
        expected_result = [1, 1]

        # when
        start_time = time.perf_counter()
        result = queue_min(n, commands)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_process_large_data(self):
        """Случай с большими данными для проверки производительности"""
        # given
        n = 10000
        commands = [["+", str(i)] for i in range(10000)] + [["?"]]  # Добавляем числа от 0 до 9999 и ищем минимум
        expected_result = [0]

        # when
        start_time = time.perf_counter()
        result = queue_min(n, commands)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_removals(self):
        """Случай с последовательными удалениями и запросами минимума"""
        # given
        n = 7
        commands = [
            ["+", "5"],
            ["+", "3"],
            ["+", "8"],
            ["-", ""],
            ["?", ""],
            ["-", ""],
            ["?", ""]
        ]
        expected_result = [3, 8]

        # when
        start_time = time.perf_counter()
        result = queue_min(n, commands)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_handle_negative_numbers(self):
        """Случай с отрицательными числами"""
        # given
        n = 5
        commands = [
            ["+", "-1"],
            ["+", "-5"],
            ["?", ""],
            ["-", ""],
            ["?", ""]
        ]
        expected_result = [-5, -5]

        # when
        start_time = time.perf_counter()
        result = queue_min(n, commands)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_only_minimum_requests(self):
        """Случай, когда есть только запросы на минимум"""
        # given
        n = 5
        commands = [
            ["+", "10"],
            ["+", "15"],
            ["?", ""],
            ["?", ""],
            ["?", ""]
        ]
        expected_result = [10, 10, 10]

        # when
        start_time = time.perf_counter()
        result = queue_min(n, commands)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()