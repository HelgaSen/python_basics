"""
Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.
"""

the_list = list((input('Введите слова через пробел: ').split(' ')))
for i in range(len(the_list)):
    print(f'{i + 1}. {the_list[i][:10]}')