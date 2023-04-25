# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.

def input_data(message):
    return int(input(f'{message}'))

first_element = input_data('Введите первый элемент: ')
difference = input_data('Введите разность: ')
count_elements = input_data('Введите количество элементов: ')

result_list = [i for i in range(first_element, first_element + count_elements * difference, difference)]

print(*result_list)