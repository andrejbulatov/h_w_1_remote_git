# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random

number_first = int(input('Введите исходный размер первого списка: '))

list_first = [random.randint(-5,5) for i in range(number_first)]
print(*list_first)

number_second = int(input('Введите исходный размер первого списка: '))

list_second = [random.randint(-5,5) for i in range(number_second)]
print(*list_second)

set_number_first = set(list_first)
set_number_second = set(list_second)

print(*sorted(set_number_first.intersection(set_number_second)))