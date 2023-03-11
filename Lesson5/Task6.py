"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random

number = random.randint(0, 100)


def guess_number(num, try_cnt, cnt=0):
    cnt += 1
    input_number = int(input('Введите целое число от 0 до 100:\n'))
    if cnt <= 10 and num == input_number:
        return print(f'Поздравляю! Вы угадали! Загаданное число {num}')
    elif cnt < 10 and num > input_number:
        print(f'Очень жаль, вы не угадали. Введенное вами число меньше'
              f' загаданного. У вас осталось {try_cnt - cnt} попыток')
        guess_number(num, try_cnt, cnt)
    elif cnt < 10 and num < input_number:
        print(f'Очень жаль, вы не угадали. Введенное вами число больше'
              f' загаданного. У вас осталось {try_cnt - cnt} попыток')
        guess_number(num, try_cnt, cnt)
    elif cnt == try_cnt:
        return print(
            f'Очень жаль, вы не угадали число. Загаданное число: {num}')


guess_number(number, 10)
