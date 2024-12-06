import os
import subprocess

def run_all_py_files(directory):
    # Находим все файлы с расширением .py в заданной директории
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != "run_all.py" and filename != "test.py" and filename != "__init__.py":  # Исключаем сам скрипт
            file_path = os.path.join(directory, filename)
            subprocess.run(["python3", file_path], check=True)  # Запускаем файл

# Задаем директорию, где находятся все файлы
directory = os.path.dirname(os.path.abspath(__file__))
run_all_py_files(directory)


if __name__ == "__main__":
    run_all_py_files(directory)
