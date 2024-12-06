import sys
import os
import unittest
from io import StringIO  # Для перехвата вывода

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

def discover_and_run_tests():
    base_dir = os.path.dirname(__file__)

    task_dirs = [d for d in os.listdir(base_dir) if d.startswith('task') and os.path.isdir(os.path.join(base_dir, d))]

    for task_dir in task_dirs:
        test_dir = os.path.join(base_dir, task_dir, 'test')

        if not os.path.exists(test_dir):
            continue  # Если папка с тестами отсутствует, пропускаем её

        loader = unittest.TestLoader()
        suite = loader.discover(start_dir=test_dir, pattern="test_*.py")

        # Перехватываем вывод unittest
        buffer = StringIO()
        runner = unittest.TextTestRunner(stream=buffer, verbosity=1)
        result = runner.run(suite)

        # Просто очищаем буфер без его вывода
        buffer.close()

        # Выводим только ваш результат
        if result.wasSuccessful():
            print(f"=========={task_dir}: Все тесты прошли успешно.========== \n")
        else:
            print(f"{task_dir}: Обнаружены ошибки в тестах. Проверьте выше.")

if __name__ == "__main__":
    discover_and_run_tests()