# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input("Enter VLAN number: ")

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
    if i[0] == int(vlan):
        print(form.format(*i))
