# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

number = int(input('Введите число: '))
degree = int(input('Введите степень: '))

def exponentiate_number(num, deg):
    if deg == 0:
        return 1
    else:
        return num * exponentiate_number(num, deg - 1)


print(f'Число {number} в степени {degree} равно {exponentiate_number(number, degree)}')