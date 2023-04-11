# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random

number_first = random.randint(1,10)
number_second = random.randint(1,10)

sum = number_first + number_second
print(f'Сумма чисел {sum}')

product_numbers = number_first * number_second
print(f'Произведение чисел {product_numbers}')

input_number_first = 0
input_number_second = 0

while (input_number_first != number_first and input_number_first != number_second 
      and input_number_second != number_first and input_number_second != number_second):
    input_number_first = int(input('Введите первое число: '))
    input_number_second = int(input('Введите второе число: '))
    print('Вы ввели неверные числа, повторите ввод')
else:
    print(f'Вы отгадали числа - это {input_number_first} и {input_number_second}')
