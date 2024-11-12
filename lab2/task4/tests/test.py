import unittest
from lab2.task4.src.four import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_should_binary_search_element_found(self):
        """Простой тест"""
        arr = [1, 3, 5, 7, 9]
        index = binary_search(arr, 5)
        self.assertEqual(index, 2)  # Элемент 5 находится на индексе 2

    def test_should_binary_search_first_element(self):
        """Начальный элемент верный"""
        arr = [1, 3, 5, 7, 9]
        index = binary_search(arr, 1)
        self.assertEqual(index, 0)

    def test_should_binary_search_last_element(self):
        """Крайний элемент верный"""
        arr = [1, 3, 5, 7, 9]
        index = binary_search(arr, 9)
        self.assertEqual(index, 4)

    def test_sshould_binary_search_ingle_element_found(self):
        """Массив с 1 элементом"""
        arr = [10]
        index = binary_search(arr, 10)
        self.assertEqual(index, 0)

    def test_should_binary_search_single_element_not_found(self):
        """Массив с 1 элементом и без искомого элемента"""
        arr = [10]
        index = binary_search(arr, 5)
        self.assertEqual(index, -1)

    def test_should_binary_search_large_sorted_array(self):
        """Большой массив"""
        arr = list(range(1, 1000001))  # Массив от 1 до 1,000,000
        index = binary_search(arr, 500000)
        self.assertEqual(index, 499999)  # Элемент 500000 должен быть на индексе 499999

    def test_should_binary_search_large_array_not_found(self):
        """Тест с поиском отсутствующего элемента"""
        arr = list(range(1, 1000001))
        index = binary_search(arr, 1000001)
        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()
