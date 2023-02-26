"""Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

time_seconds = int(input('Введите время в секундах: '))
hour = time_seconds // 3600
minute = (time_seconds % 3600) // 60
second = time_seconds % 60
output_time = "%02d:%02d:%02d" % (hour, minute, second)
print(f'Время в формате чч:мм:сс {output_time}')
