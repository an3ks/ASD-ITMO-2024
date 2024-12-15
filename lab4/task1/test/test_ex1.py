import unittest
import time
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking1
from lab4.task1.src.ex1 import stack


class TestStackFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256
    def test_should_stack1(self):
        """Базовый случай: стандартное добавление и извлечение элементов"""
        # given
        n = 4
        data = [
            ["+", "1"],
            ["+", "2"],
            ["-", ""],
            ["+", "3"],
        ]
        expected_result = ["2"]

        # when
        start_time = time.perf_counter()
        result = stack(n, data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_stack2(self):
        """Все операции — добавление"""
        # given
        n = 3
        data = [
            ["+", "1"],
            ["+", "2"],
            ["+", "3"]
        ]
        expected_result = []

        # when
        start_time = time.perf_counter()
        result = stack(n, data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_stack3(self):
        """Все операции — извлечение"""
        # given
        n = 3
        data = [
            ["+", "1"],
            ["+", "2"],
            ["-", ""],
            ["-", ""],
        ]
        expected_result = ["2", "1"]

        # when
        start_time = time.perf_counter()
        result = stack(n, data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_stack4(self):
        """Случай с большими данными для проверки производительности"""
        # given
        n = 100000
        data = [["+", str(i)] for i in range(1, n + 1)]
        data += [["-", ""] for _ in range(1, n + 1)]

        expected_result = [str(i) for i in range(n, 0, -1)]

        # when
        start_time = time.perf_counter()
        result = stack(n * 2, data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        time_memory_tracking1(start_time)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()