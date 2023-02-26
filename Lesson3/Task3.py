"""
3. Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя.

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
"""
param_dict_one = dict(
    [('наименование', input('Введите наименование товара: ')),
     ('цена', int(input('Введите цену товара: '))),
     ('ед.изм', input('Введите единицу измерения товара: ')),
     ('количество', int(input('Введите количество единиц товара: '))),
     ])
param_dict_two = dict(
    [('наименование', input('Введите наименование товара: ')),
     ('цена', int(input('Введите цену товара: '))),
     ('ед.изм', input('Введите единицу измерения товара: ')),
     ('количество', int(input('Введите количество единиц товара: '))),
     ])
param_dict_three = dict(
    [('наименование', input('Введите наименование товара: ')),
     ('цена', int(input('Введите цену товара: '))),
     ('ед.изм', input('Введите единицу измерения товара: ')),
     ('количество', int(input('Введите количество единиц товара: '))),
     ])
product_one = (1, param_dict_one)
product_two = (2, param_dict_two)
product_three = (3, param_dict_three)
product_structure = [product_one, product_two, product_three]
print('Структура данных "ТОВАРЫ": ')
print(*product_structure, sep='\n')
analytics_dict = dict()
analytics_dict['Названия'] = param_dict_one.get('наименование'), \
    param_dict_two.get('наименование'), \
    param_dict_three.get('наименование')
analytics_dict['Цены'] = param_dict_one['цена'], param_dict_two['цена'], \
    param_dict_three['цена']
analytics_dict['Ед.изм'] = param_dict_one['ед.изм'], \
    param_dict_two['ед.изм'], param_dict_three['ед.изм']
analytics_dict['Количество'] = param_dict_one['количество'], \
    param_dict_two['количество'], param_dict_three['количество']

print('Аналитика по товарам: ')
for key, value in analytics_dict.items():
    print(key, ':', value)