"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

progression_len = int(input('Введите количество элементов массива:\n'))
progression = [0] * progression_len
progression[0] = int(input('Введите первый элемент прогрессии:\n'))
progression_step = int(input('Введите шаг прогрессии:\n'))
print(progression[0], end='\n')
for i in range(1, progression_len):
    progression[i] = progression[i - 1] + progression_step
    print(progression[i], end='\n')
