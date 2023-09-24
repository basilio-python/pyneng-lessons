# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес: ')

key = True
while key:
    if len(list(ip.split("."))) != 4:
        print("Неправильный IP-адрес")
    elif ip.count(' ') > 0 or ip.count(',') > 0:
        print("Неправильный IP-адрес")
    else:
        k = 0
        for i in list(ip.split(".")):
            try:
                if not 0 <= int(i) <= 255:
                    print("Неправильный IP-адрес")
                    break
            except:
                print("Неправильный IP-адрес")
                break

            if k == 3:
                first: int = int(list(ip.split("."))[0])
                if first >= 1 and first <= 223:
                    print("unicast")
                elif first >= 224 and first <= 239:
                    print("multicast")
                elif ip == "255.255.255.255":
                    print("local broadcast")
                elif ip == "0.0.0.0":
                    print("unassigned")
                else:
                    print("unused")
                key = False
            k = k + 1

        if key:
            ip = input('Введите IP-адрес: ')