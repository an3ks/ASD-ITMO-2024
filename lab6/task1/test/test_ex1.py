import unittest
import time
from lab6.utils.utils import time_memory_tracking1
from lab6.task1.src.ex1 import process_set_operations


class TestSetOperations(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_process_set_operations1(self):
        """Базовый случай: добавление, удаление и проверка элемента"""
        # given
        queries = ["A 2", "A 5", "A 3", "? 2", "? 4", "D 2", "? 2"]
        expected_result = ["Y", "N", "N"]

        # when
        start_time = time.perf_counter()
        result = process_set_operations(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_set_operations2(self):
        """Проверка элемента в пустом множестве"""
        # given
        queries = ["? 1", "? 5", "? 10"]
        expected_result = ["N", "N", "N"]

        # when
        start_time = time.perf_counter()
        result = process_set_operations(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_set_operations3(self):
        """Добавление одинаковых элементов"""
        # given
        queries = ["A 10", "A 10", "? 10", "D 10", "? 10"]
        expected_result = ["Y", "N"]

        # when
        start_time = time.perf_counter()
        result = process_set_operations(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_set_operations4(self):
        """Стресс-тест с большим количеством добавлений и проверок"""
        # given
        queries = ["A " + str(i) for i in range(100000)] + ["? 50000", "? 99999", "? 100000"]
        expected_result = ["Y", "Y", "N"]

        # when
        start_time = time.perf_counter()
        result = process_set_operations(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()