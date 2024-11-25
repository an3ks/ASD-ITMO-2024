import os
import subprocess

def run_all_py_files(directory):
    # Находим все файлы с расширением .py в заданной директории
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != "run_all.py" and filename != "test.py":  # Исключаем сам скрипт
            file_path = os.path.join(directory, filename)
            print(f"Запускаем {file_path}")
            subprocess.run(["python3", file_path], check=True)  # Запускаем файл

# Задаем директорию, где находятся все твои файлы
directory = os.path.dirname(os.path.abspath(__file__))
run_all_py_files(directory)
