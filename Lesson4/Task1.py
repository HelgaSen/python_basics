"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами
элементы множеств.

"""
bunch_n_len = int(input('Введите натуральное число N: '))
bunch_m_len = int(input('Введите натуральное число M: '))
list_n = []
list_m = []

for i in range(bunch_n_len):
    if i == 0:
        temp_var = int(input('Введите первый элемент множества N: '))
        list_n.append(temp_var)
    elif i == bunch_n_len - 1:
        temp_var = int(input('Введите последний элемент множества N: '))
        list_n.append(temp_var)
    else:
        temp_var = int(input('Введите следующий элемент множества N: '))
        list_n.append(temp_var)
    i += 1

for i in range(bunch_m_len):
    if i == 0:
        temp_var = int(input('Введите первый элемент множества M: '))
        list_m.append(temp_var)
    elif i == bunch_m_len - 1:
        temp_var = int(input('Введите последний элемент множества M: '))
        list_m.append(temp_var)
    else:
        temp_var = int(input('Введите следующий элемент множества M: '))
        list_m.append(temp_var)
    i += 1
print(f'Набор целых чисел N:\n {list_n}')
print(f'Набор целых числе M: \n {list_m}')
list_n.sort()
list_m.sort()
bunch_n = set(list_n)
bunch_m = set(list_m)

final_bunch = set.intersection(bunch_n, bunch_m)
final_bunch_list = list(final_bunch)
final_bunch_list.sort()
print(f'Числа, которые встречаются в обоих наборах; \n '
      f'{final_bunch_list}')
