import unittest
import time
from lab6.utils.utils import time_memory_tracking1
from lab6.task2.src.ex2 import phone_book


class TestPhoneBook(unittest.TestCase):
    TIME_LIMIT_SECONDS = 6
    MEMORY_LIMIT_MB = 512

    def test_should_phone_book1(self):
        """Базовый случай: добавление, удаление и поиск номеров"""
        # given
        queries = ["add 12345 Alice", "add 67890 Bob", "find 12345", "del 12345", "find 12345"]
        expected_result = ["Alice", "not found"]

        # when
        start_time = time.perf_counter()
        result = phone_book(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_phone_book2(self):
        """Поиск несуществующего номера"""
        # given
        queries = ["find 11111", "add 22222 Eve", "find 33333"]
        expected_result = ["not found", "not found"]

        # when
        start_time = time.perf_counter()
        result = phone_book(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_should_phone_book3(self):
        """Добавление и поиск нескольких номеров"""
        # given
        queries = ["add 123 Alice", "add 456 Bob", "add 789 Carol", "find 123", "find 456", "find 789"]
        expected_result = ["Alice", "Bob", "Carol"]

        # when
        start_time = time.perf_counter()
        result = phone_book(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_should_phone_book4(self):
        """Стресс-тест с большим количеством запросов"""
        # given
        queries = ["add " + str(i) + " Name" + str(i) for i in range(100000)] + ["find 50000"]
        expected_result = ["Name50000"]

        # when
        start_time = time.perf_counter()
        result = phone_book(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()