# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

script, filename = argv

with open(filename, 'r') as f:
    flist = f.read().rstrip().split("\n")
    for s in flist:
        for i in ignore:
            if s.startswith("!") or s.__contains__(i):
                break
            if i == ignore[len(ignore) - 1]:
                print(s)
