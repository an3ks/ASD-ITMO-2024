ЗАДАНИЕ: Наибольшая общая подпоследовательность трех последовательностей (LCS-3)

Выполненные шаги:

1. Постановка задачи
Реализован алгоритм нахождения длины наибольшей общей подпоследовательности для трех последовательностей.

2. Алгоритм
Использован подход динамического программирования с трехмерным массивом `dp[i][j][k]`, где `i`, `j`, `k` - текущие длины префиксов последовательностей A, B, C.

3. Формула перехода:
Если текущие элементы последовательностей совпадают:
    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
Иначе:
    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

4. Ограничения:
- Время выполнения: O(n * m * l)
- Используемая память: O(n * m * l), где n, m, l — длины последовательностей.

Пример входных данных:
3
1 2 3
3
2 1 3
3
1 3 5

Вывод программы:
2

Пояснение: Общая подпоследовательность для [1, 2, 3], [2, 1, 3] и [1, 3, 5] — это [1, 3].