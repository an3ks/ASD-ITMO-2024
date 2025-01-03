# Отчет по реализации пузырьковой сортировки (Bubble Sort)

## Задание

Реализовать алгоритм пузырьковой сортировки, который последовательно сравнивает соседние элементы массива и меняет их местами, если они находятся в неправильном порядке.

## Реализация

Алгоритм пузырьковой сортировки был реализован для упорядочивания массива чисел. Основной принцип работы заключается в последовательной проверке всех пар соседних элементов и их перестановке при необходимости.

Компоненты реализации:

- Используется двойной цикл: внешний цикл проходит по всему массиву, а внутренний отвечает за сравнение соседних элементов.
- Для повышения удобства работы, данные считываются из файла `input.txt`, а результат записывается в файл `output.txt`.
- В программе добавлены функции для отслеживания времени выполнения и пикового потребления памяти.

## Input / Output

- **Input:** Входной файл `input.txt` должен содержать:
  - Первую строку: длина массива.
  - Вторую строку: элементы массива, разделенные пробелами.
- **Output:** Выходной файл `output.txt` содержит отсортированный массив.

## Потребление времени и памяти

- Ограничение по времени: 10 сек.
- Ограничение по памяти: 256 Мб.

На тестовых данных алгоритм сортировки выполнялся за 0.01 секунды с пиковым потреблением памяти около 100 Кб.

