# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

def input_data(message):
    return int(input(f'{message}'))

def fill_list(list):
    return [random.randint(0,10) for _ in range(list)]

length_list = input_data('Введите размер списка: ')
input_list = fill_list(length_list)
print(*input_list)

min_value = input_data('Введите минимальное значение: ')
max_value = input_data('Введите максимальное значение: ')

result_list = [i for i in range(length_list) if min_value <= input_list[i] <= max_value]

print(*result_list)

