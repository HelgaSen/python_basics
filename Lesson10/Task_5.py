"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess


def ping_website(website):
    my_attr = ['ping', website]
    website_ping = subprocess.Popen(my_attr, stdout=subprocess.PIPE)
    print(website_ping.stdout)
    for line in website_ping.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


ping_website('yandex.ru')
ping_website('youtube.com')
