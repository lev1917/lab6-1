'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
__author__ = 'student'
mas = open('input.txt','r')
V = open('output','w')
f = mas.readline()
g = mas.readline()
f = f.rstrip()
g = g.rstrip()
a = list(map(int, g.split()))

for d in range(len(a)):
    a[d]=int(a[d])
l=min(a)
t=0
o=max(a)
while o>=l:
    if a.count(l)==2:
        t=l
        break
    l+=1
print(t, file=V)

V.close()
mas.close()
