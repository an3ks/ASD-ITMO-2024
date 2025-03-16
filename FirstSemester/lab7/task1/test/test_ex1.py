import unittest
import time
from lab7.utils.utils import time_memory_tracking1
from lab7.task1.src.ex1 import process_min_coins


class TestProcessMinCoins(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 128

    def test_should_process_min_coins_case1(self):
        """Базовый случай: есть решение"""
        # given
        money = 6
        coins = [1, 3, 4]
        expected_result = 2

        # when
        start_time = time.perf_counter()
        result = process_min_coins(money, coins)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_min_coins_case2(self):
        """Нет решения"""
        # given
        money = 7
        coins = [2, 4]
        expected_result = -1

        # when
        start_time = time.perf_counter()
        result = process_min_coins(money, coins)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_min_coins_case3(self):
        """Случай с большим количеством монет"""
        # given
        money = 100
        coins = [1, 5, 10, 25]
        expected_result = 4

        # when
        start_time = time.perf_counter()
        result = process_min_coins(money, coins)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_min_coins_case4(self):
        """Стресс-тест: большое значение money"""
        # given
        money = 1000
        coins = [1, 2, 5]
        expected_result = 200

        # when
        start_time = time.perf_counter()
        result = process_min_coins(money, coins)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()