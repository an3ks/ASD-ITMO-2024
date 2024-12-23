## Задание: Наибольшая возрастающая подпоследовательность (LIS)  
Студент ИТМО, Авдиенко Данила, itmoId 464919  

---

## Задание 6  
Реализовать алгоритм нахождения наибольшей возрастающей подпоследовательности.  
Найти длину самой длинной возрастающей подпоследовательности для последовательности `A`.

---

## Input / Output  

### Формат входных данных:  
- Первая строка содержит число `n` — длина последовательности.  
- Вторая строка содержит `n` элементов последовательности.  

### Формат выходных данных:  
- Первая строка содержит длину наибольшей возрастающей подпоследовательности.  
- Вторая строка содержит элементы наибольшей возрастающей подпоследовательности.  

| Input                               | Output             |
|-------------------------------------|--------------------|
| 6                                   | 3                  |
| 3 29 5 28 6 8                       | 3 5 6              |

**Пояснение**:  
- Наибольшая возрастающая подпоследовательность для последовательности `A = [3, 29, 5, 28, 6, 8]` — это `[3, 5, 6]`, длина которой равна `3`.

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
   cd lab7/task6/src  
   ```

3. Запустите программу:  
   ```bash  
   python ex6.py  
   ```
---

## Тестирование  

### Запуск тестов  
Для запуска тестов выполните:  
```bash  
python -m unittest discover test/  
```