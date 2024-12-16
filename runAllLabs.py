import os
import subprocess


def run_scripts_in_src(base_dirs, python_cmd="python3"):
    for base_path in base_dirs:
        print(f"\n--- Запуск файлов в директории: {base_path} ---")
        if not os.path.exists(base_path):
            print(f"Директория {base_path} не найдена. Пропускаем.")
            continue

        for dirpath, dirnames, filenames in os.walk(base_path):
            if os.path.basename(dirpath) == "src":
                print(f"\nЗапуск файлов из папки: {dirpath}")
                for file in filenames:
                    if file.endswith(".py") and file != "__init__.py":
                        run_python_file(file, dirpath, python_cmd)


def run_python_file(file_name, script_dir, python_cmd):
    try:
        print(f"  Выполнение файла: {file_name}")
        print(f"  Текущая рабочая директория: {script_dir}")

        # Выполняем файл через subprocess
        result = subprocess.run(
            [python_cmd, file_name],  # Передаём только имя файла
            cwd=script_dir,  # Рабочая директория — папка src
            capture_output=True,
            text=True
        )

        print(result.stdout)
        if result.stderr:
            print(f"  Ошибка выполнения: {result.stderr}")
    except Exception as e:
        print(f"  Ошибка при выполнении {file_name}: {e}")


if __name__ == "__main__":
    # Список всех директории
    base_dirs = ["lab1", "lab2", "lab3", "lab4", "lab5"]

    # Указываем, какой интерпретатор использовать: "python" или "python3"
    run_scripts_in_src(base_dirs, python_cmd="python3")
