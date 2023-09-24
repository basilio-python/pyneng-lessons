# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
netmask = input("Введите адрес и маску сети в формате X.X.X.X/Y: ")
list_1 = netmask.split('/')

mask = int(list_1[1])
mask_str = "1" * mask + "0" * (32 - mask)
net = list_1[0].split('.')
form = '{:08b}'
net_str = form.format(int(net[0])) + form.format(int(net[1])) + form.format(int(net[2])) + form.format(int(net[3]))

mask_list = list()
mask_list.append(int(mask_str[0:8], 2))
mask_list.append(int(mask_str[8:16], 2))
mask_list.append(int(mask_str[16:24], 2))
mask_list.append(int(mask_str[24:32], 2))

net_list = list()
net_list.append(int(mask_str[0:8], 2) & int(net_str[0:8], 2))
net_list.append(int(mask_str[8:16], 2) & int(net_str[8:16], 2))
net_list.append(int(mask_str[16:24], 2) & int(net_str[16:24], 2))
net_list.append(int(mask_str[24:32], 2) & int(net_str[24:32], 2))

print("Network:")
formstr = "{0:<10}{1:<10}{2:<10}{3:<10}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}"
print(formstr.format(net_list[0],net_list[1],net_list[2],net_list[3]))

print("\nMask:")
print("/" + str(mask))
print(formstr.format(mask_list[0],mask_list[1],mask_list[2],mask_list[3]))
