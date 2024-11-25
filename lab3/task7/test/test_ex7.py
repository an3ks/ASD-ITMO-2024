import unittest

from ..src.ex7 import digital_sorting
class TestDigitalSortingFunction(unittest.TestCase):

    def test_should_digital_sorting1(self):
        """Базовый тест"""
        n, m, k = 3, 3, 1
        matrix = [
            "bab",
            "bba",
            "baa"
        ]
        expected_result = [2, 3, 1]

        # when
        result = digital_sorting(n, m, k, matrix)

        # then
        self.assertEqual(result, expected_result)

    def test_should_digital_sorting2(self):
        """Тест с несколькими фазами сортировки"""
        n, m, k = 3, 3, 2
        matrix = [
            "bab",
            "bba",
            "baa"
        ]
        expected_result = [3, 2, 1]

        # when
        result = digital_sorting(n, m, k, matrix)

        # then
        self.assertEqual(result, expected_result)


    def test_should_digital_sorting3(self):
        n, m, k = 5, 5, 3
        matrix = [
            "edcba",
            "zyxwv",
            "kjihg",
            "utsrq",
            "ponml"
        ]
        expected_result = [5, 4, 3, 2, 1]

        # when
        result = digital_sorting(n, m, k, matrix)

        # then
        self.assertEqual(result, expected_result)

    def test_should_digital_sorting4(self):
        """Тест на пустую матрицу"""
        n, m, k = 0, 0, 0
        matrix = []
        expected_result = []

        # when
        result = digital_sorting(n, m, k, matrix)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()