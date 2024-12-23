## Задание: Наибольшая общая подпоследовательность трех последовательностей (LCS-3)  
Студент ИТМО, Авдиенко Данила, itmoId 464919  

---

## Задание 5  
Реализовать алгоритм нахождения наибольшей общей подпоследовательности трех последовательностей.  
Найти длину самой длинной общей подпоследовательности для трех последовательностей `A`, `B` и `C`.

---

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — длина первой последовательности.  
- Вторая строка содержит `n` элементов первой последовательности.  
- Третья строка содержит число `m` — длина второй последовательности.  
- Четвертая строка содержит `m` элементов второй последовательности.  
- Пятая строка содержит число `l` — длина третьей последовательности.  
- Шестая строка содержит `l` элементов третьей последовательности.  

### Формат выходных данных:  
- Одно число — длина наибольшей общей подпоследовательности.  

| Input                               | Output             |
|-------------------------------------|--------------------|
| 3                                   | 2                  |
| 1 2 3                               |                    |
| 3                                   |                    |
| 2 1 3                               |                    |
| 3                                   |                    |
| 1 3 5                               |                    |

**Пояснение**:  
- Общая подпоследовательность для трех последовательностей `A = [1, 2, 3]`, `B = [2, 1, 3]` и `C = [1, 3, 5]` — это `[1, 3]`, длина которой равна `2`.

---

## Ограничения по времени и памяти  
- Ограничение по времени: 1 сек.  
- Ограничение по памяти: 256 Мб.  

---

## Запуск проекта  

1. Клонируйте репозиторий:  
   ```bash  
   git clone https://github.com/an3ks/ASD-ITMO-2024  
   ```  

2. Перейдите в папку с проектом:  
   ```bash  
   cd lab7/task5/src  
   ```

3. Запустите программу:  
   ```bash  
   python ex5.py  
   ```
---

## Тестирование  

### Запуск тестов  
Для запуска тестов выполните:  
```bash  
python -m unittest discover test/  
```