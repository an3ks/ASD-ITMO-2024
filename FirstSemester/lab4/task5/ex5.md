# Отчет по заданию

## Задание: Реализация стека с командами добавления и удаления элементов  
Студент ИТМО, Авдиенко Данила, itmoId 464919

## Вариант 1

---

## Задание 1

Реализовать стек с командами добавления элемента в стек (`+`) и удаления элемента из стека (`-`). При удалении элемента из стека результат необходимо сохранить.

---

## Input / Output

### Формат входных данных:
- Первая строка содержит число `n` — количество операций.
- Последующие строки содержат команды:
  - `+ X` — добавить элемент `X` в стек.
  - `-` — удалить верхний элемент из стека.

### Формат выходных данных:
- Список элементов, удаленных из стека в порядке их удаления.

| Input                               | Output             |
|-------------------------------------|--------------------|
| 5                                   | ['2', '1']         |
| + 1                                 |                    |
| + 2                                 |                    |
| -                                   |                    |
| -                                   |                    |
| + 3                                 |                    |

---

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 Мб.

---

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/an3ks/ASD-ITMO-2024
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd lab4/task5/src
   ```
3. Запустите программу:
   ```bash
   python ex5.py
   ```

---

## Тестирование
Для запуска тестов выполните:
```bash
python -m unittest discover test/
```

---

## Код для ex5.py
```python
def stack(n, commands):
    stack = []
    max_stack = []
    results = []

    for command in commands:
        if command[0] == "push":
            value = int(command[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif command[0] == "pop":
            if stack:
                value = stack.pop()
                if max_stack and value == max_stack[-1]:
                    max_stack.pop()
        elif command[0] == "max":
            if max_stack:
                results.append(max_stack[-1])

    return results
```