import sys
import os
import unittest


base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

def discover_and_run_tests():
    base_dir = os.path.dirname(__file__)

    task_dirs = [d for d in os.listdir(base_dir) if d.startswith('task') and os.path.isdir(os.path.join(base_dir, d))]

    for task_dir in task_dirs:
        print(f"\n=== Запуск тестов для {task_dir} ===")

        test_dir = os.path.join(base_dir, task_dir, 'test')

        if not os.path.exists(test_dir):
            print(f"Папка с тестами отсутствует: {test_dir}")
            continue

        loader = unittest.TestLoader()
        suite = loader.discover(start_dir=test_dir, pattern="test_*.py")

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        if result.wasSuccessful():
            print(f"Все тесты для {task_dir} прошли успешно!")
        else:
            print(f"Ошибки в тестах для {task_dir}. Проверьте детали выше.")


if __name__ == "__main__":
    discover_and_run_tests()