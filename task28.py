# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.



number_first = int(input('Введите первое число: '))
number_second = int(input('Введите второе число: '))


def summa_two_numbers(num_first, num_second):
    if num_first == 0:
        return num_second
    elif num_second == 0:
        return num_first
    else:
        return summa_two_numbers(num_first + 1, num_second - 1)


print(f'Сумма двух чисел {number_first} и {number_second} равна {summa_two_numbers(number_first, number_second)}')