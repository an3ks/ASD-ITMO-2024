import unittest
import time
from lab6.utils.utils import time_memory_tracking1
from FirstSemester.lab6.task5.src.ex5 import count_votes


class TestCountVotes(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 128

    def test_should_count_votes1(self):
        """Базовый случай: несколько кандидатов с разными голосами"""
        # given
        queries = ["McCain 10", "McCain 5", "Obama 9", "Obama 8", "McCain 1"]
        expected_result = ["McCain 16", "Obama 17"]

        # when
        start_time = time.perf_counter()
        result = count_votes(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_count_votes2(self):
        """Один кандидат с несколькими голосами"""
        # given
        queries = ["ivanov 100", "ivanov 500", "ivanov 300"]
        expected_result = ["ivanov 900"]

        # when
        start_time = time.perf_counter()
        result = count_votes(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_count_votes3(self):
        """Несколько кандидатов с одним голосом каждый"""
        # given
        queries = ["petr 70", "tourist 1", "tourist 2"]
        expected_result = ["petr 70", "tourist 3"]

        # when
        start_time = time.perf_counter()
        result = count_votes(queries)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
