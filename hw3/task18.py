# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint

list_nums = [randint(1, 21) for i in range(int(input()))]

print(list_nums)
num = int(input())
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print(right_num)

# 2 вариант

from random import randint

n = int(input())
list_nums = [randint(1, 50) for i in range(n)]
print(list_nums)
b = int(input())
m = min(list_nums, key=lambda x: abs(x - b))
print(m)
