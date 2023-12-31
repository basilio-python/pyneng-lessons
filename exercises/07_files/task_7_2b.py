# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

script, filename_in, filename_out = argv

with open(filename_in, 'r') as f, open(filename_out, 'w') as fw:
    flist = f.read().rstrip().split("\n")
    for s in flist:
        for i in ignore:
            if s.startswith("!") or s.__contains__(i):
                break
            if i == ignore[len(ignore) - 1]:
                fw.write(f"{s}\n")
