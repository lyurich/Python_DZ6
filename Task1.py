# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

first_num = int(input('Введите первый элемент массива: '))
step = int(input('Введите шаг арифметической прогрессии: '))
size = int(input('Введите количество элементов прогрессии: '))


for i in range(size):
    print(first_num + i * step)
