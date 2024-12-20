import unittest
import time
from lab4.utils.utils import time_memory_tracking1
from lab4.task5.src.ex5 import stack


class TestStackFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 5
    MEMORY_LIMIT_MB = 512

    def test_should_stack1(self):
        """Базовый случай: стандартное добавление и извлечение элементов"""
        # given
        n = 5
        data = [
            ["push", "2"],
            ["push", "1"],
            ["max", ""],
            ["pop", ""],
            ["max", ""],
        ]
        expected_result = [2, 2]

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
        """Случай только с добавлением элементов"""
        # given
        n = 3
        data = [
            ["push", "1"],
            ["push", "2"],
            ["push", "3"],
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
        """Случай с несколькими вызовами max"""
        # given
        n = 7
        data = [
            ["push", "5"],
            ["push", "1"],
            ["max", ""],
            ["pop", ""],
            ["max", ""],
            ["pop", ""],
            ["max", ""],
        ]
        expected_result = [5, 5]

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
        """Случай с большим количеством данных"""
        # given
        n = 100000
        data = [["push", str(i)] for i in range(1, n + 1)]
        data += [["max", ""]] * 10

        expected_result = [n] * 10

        # when
        start_time = time.perf_counter()
        result = stack(len(data), data)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()