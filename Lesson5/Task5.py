"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def ascii_printer(start, stop, cnt=0):
    if start == stop:
        return print('%4d-%s' % (start, chr(start)))
    else:
        print('%4d-%s' % (start, chr(start)), end='')
        cnt += 1
        if cnt % 10 == 0:
            print()
            ascii_printer(start + 1, stop, cnt)
        else:
            ascii_printer(start + 1, stop, cnt)


ascii_printer(32, 127)
