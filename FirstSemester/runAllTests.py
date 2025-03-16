import os
import sys
import unittest
import importlib
from io import StringIO  # Для перехвата вывода


def discover_and_run_all_tests(base_dirs):
    """
    Функция для запуска всех тестов во всех лабораториях с изоляцией импортов.
    """
    print("\n========== Запуск всех тестов во всех лабораториях ==========\n")

    for base_path in base_dirs:
        print(f"\n--- Поиск и запуск тестов в директории: {base_path} ---")
        if not os.path.exists(base_path):
            print(f"Директория {base_path} не найдена. Пропускаем.")
            continue

        # Рекурсивно ищем папки 'test' в каждой 'task'
        for dirpath, dirnames, filenames in os.walk(base_path):
            if os.path.basename(dirpath) == "test":

                # Добавляем текущую директорию с тестами в sys.path
                sys.path.insert(0, dirpath)

                try:
                    # Удаляем старые кэши импортов
                    for module in list(sys.modules.keys()):
                        if "test_" in module:
                            del sys.modules[module]

                    # Загружаем тесты
                    loader = unittest.TestLoader()
                    suite = loader.discover(start_dir=dirpath, pattern="test_*.py")

                    # Подавляем стандартный вывод TextTestRunner
                    buffer = StringIO()
                    runner = unittest.TextTestRunner(stream=buffer, verbosity=0)
                    result = runner.run(suite)

                    # Кастомный вывод
                    if result.wasSuccessful():
                        print(f"✅ Тесты в папке '{dirpath}' прошли успешно!")
                    else:
                        print(f"❌ Тесты в папке '{dirpath}' завершились с ошибками.")

                finally:
                    # Убираем путь из sys.path после завершения тестов
                    sys.path.pop(0)


if __name__ == "__main__":
    # Список директорий лабораторных работ
    base_dirs = ["lab1", "lab2", "lab3", "lab4", "lab5", "lab6", "lab7"]

    # Добавляем текущую директорию в sys.path для корректного импорта
    sys.path.append(os.path.abspath(".."))

    # Запускаем функцию
    discover_and_run_all_tests(base_dirs)