"""ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ.

Задача 4:
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S
журавликов. Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала
 в два раза больше журавликов, чем Петя и Сережа вместе?"""

quantity = int(input('Сколько всего бумажных журавликов сделали дети?\n'
                     'Введите целое число кратое 6: '))
if quantity % 6 == 0:
    cnt = quantity / 6
    petya_cnt = int(cnt)
    serezha_cnt = int(petya_cnt)
    katya_cnt = int(4 * cnt)
    print(f'Катя сделала бумажных журавликов - {katya_cnt} \n'
          f'Петя сделал бумажных журавликов - {petya_cnt} \n'
          f'Серёжа сделал бумажных журавликов - {serezha_cnt} \n')
else:
    print('Вы ввели неверное число.')