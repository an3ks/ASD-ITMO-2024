import unittest
import time
from lab4.utils.utils import write_output, read_input_lines, time_memory_tracking
from lab4.task1.src.ex1 import stack


class TestStackFunction(unittest.TestCase):

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
        result = stack(n, data)

        # then
        self.assertEqual(result, expected_result)

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
        result = stack(n, data)

        # then
        self.assertEqual(result, expected_result)

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
        result = stack(n, data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_stack4(self):
        """Случай с большими данными для проверки производительности"""
        # given
        n = 100000
        data = [["+", str(i)] for i in range(1, n + 1)]
        data += [["-", ""] for _ in range(1, n + 1)]

        expected_result = [str(i) for i in range(n, 0, -1)]
        start_time = time.perf_counter()

        # when
        result = stack(n * 2, data)

        # then
        self.assertEqual(result, expected_result)
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()