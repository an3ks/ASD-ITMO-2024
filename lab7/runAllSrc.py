import sys
import os
import subprocess


def discover_and_run_scripts():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ищем все папки, начинающиеся с 'task'
    task_dirs = [d for d in os.listdir(base_dir) if d.startswith('task') and os.path.isdir(os.path.join(base_dir, d))]

    for task_dir in task_dirs:
        # Путь к папке src внутри текущей taskX
        src_dir = os.path.join(base_dir, task_dir, 'src')

        if not os.path.exists(src_dir):
            continue  # Пропускаем, если src отсутствует

        # Ищем файлы, оканчивающиеся на .py
        scripts = [f for f in os.listdir(src_dir) if f.endswith('.py')]

        for script in scripts:
            script_path = os.path.join(src_dir, script)

            try:
                # Запускаем файл через subprocess
                result = subprocess.run(
                    [sys.executable, script_path],
                    cwd=src_dir,  # Устанавливаем рабочую директорию как src
                    capture_output=True,
                    text=True
                )

                # Выводим результаты выполнения
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(f"Ошибки:\n{result.stderr}")

            except Exception as e:
                print(f"Ошибка при запуске {script} из {task_dir}/src: {e}")


if __name__ == "__main__":
    discover_and_run_scripts()
