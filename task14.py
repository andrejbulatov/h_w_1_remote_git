# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите исходное число: '))
    
number_power = 1

if number <= 1:
    print('Исходное число <= 1, значений 2 в какой-либо натуральной степени меньших исходного числа нет')

while number_power < number:
    print(number_power, end = ' ')
    number_power *= 2