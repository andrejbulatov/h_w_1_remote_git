# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

number = int(input('Введите исходный размер списка: '))

list = [random.randint(-500,500) for i in range(number)]
print(*list)

number_comparing = int(input('Введите число, ближайшее к которому надо выбрать из списка: '))

index_min_difference = 0
min_difference = abs(list[index_min_difference] - number_comparing)

for i in range(1,len(list)):
    if abs(list[i] - number_comparing) < min_difference:
        min_difference = abs(list[i] - number_comparing)
        index_min_difference = i

print(f'Число из списка ближайшее к {number_comparing} равно {list[index_min_difference]}')




