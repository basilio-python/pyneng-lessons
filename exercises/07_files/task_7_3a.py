# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Подсказка: Для сортировки удобно сначала создать список списков такого типа,
а потом сортировать.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортировка должна быть по первому элементу (vlan), а если первый элемент одинаковый,
то по второму. Так работает по умолчанию функция sorted и метод sort, если сортировать
список списков выше.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
form = "{:<8} {:<19} {}"
lst = []

with open("CAM_table.txt", 'r') as f:
    flist = f.read().rstrip().split("\n")
    for s in flist:
        if s != "":
            if s.split()[0].isdigit():
                lst.append([int(s.split()[0]), s.split()[1], s.split()[3]])

lst.sort()

for i in lst:
    print(form.format(*i))
