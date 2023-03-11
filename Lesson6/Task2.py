"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)
"""

from random import randint

list_len = int(input('Введите количество элементов массива (списка):\n'))
source_list = [randint(1, 100) for _ in range(list_len)]
print("Список рандомных элементов:", source_list, sep='\n')
range_start = int(input('Введите начало диапазона:\n'))
range_end = int(input('Введите окончание диапазона:\n'))
for i in range(len(source_list)):
    if range_start <= source_list[i] <= range_end:
        print(i)
