"""Задание1
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
"""
import datetime

current_year = datetime.datetime.now().year
user_name = input('Введите ваше имя: ')
user_age = current_year - int(input('Укажите ваш год рождения: '))
user_login = input('Задайте логин: ')
user_password = input('Задайте пароль: ')

print(f'Ваши данные для входа:\n Имя - {user_name}\n Логин - {user_login}\n '
      f'Возраст - {user_age}\n Пароль - {user_password}\n')
