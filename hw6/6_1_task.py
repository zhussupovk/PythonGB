# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input())
sub = int(input())
count = int(input())

for i in range(count):
    print(first + i * sub, end=" ")