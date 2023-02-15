# Определить индексы элементов массива(списка), значения которых принадлежат заданному диапазону
# (т.е.не меньше заданного минимума и не больше заданного максимума)

from random import randint
size = int(input('Введите количество элементов: '))
list1 = []
for _ in range(size):
    list1.append(randint(-10, 11))

print(list1)

num1 = int(input('Введите минимум: '))
num2 = int(input('Введите максимум: '))

list2 = []
for i in range(size):
    if num1 <= list1[i] <= num2:
        print(i)
