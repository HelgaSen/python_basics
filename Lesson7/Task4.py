"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.list_of_lists)

    def __getitem__(self, ind):
        return self.list_of_lists[ind]

    def __add__(self, other):
        if len(self.list_of_lists) == len(other.list_of_lists) and len(
                self.list_of_lists[0]) == len(other.list_of_lists[0]):
            result = [[self.list_of_lists[i][j] + other[i][j] for j in range
            (len(self.list_of_lists[0]))] for i in
                      range(len(self.list_of_lists))]
            return Matrix(result)
        return 'складывать можно только матрицы одинаковой размерности'


input_data = [[31, 22], [37, 13], [51, 86]]
input_list = [[45, -5], [14, -22], [0, 4]]
matrix_1 = Matrix(input_data)
matrix_2 = Matrix(input_list)
print(matrix_1)
print(matrix_2)
matrix_sum = matrix_1 + matrix_2
print(f'Результат сложения матриц:\n{matrix_sum}')
