# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

number_coins = int(input('Введите количество монет: '))

count_eagle = 0
count_tails = 0

for i in range(number_coins):
    value_coin = random.randint(0,1)
    print(value_coin, end = ' ')
    if value_coin == 1:
        count_eagle += 1
    else:
        count_tails += 1

print()
if count_eagle < count_tails:
    print(f'Минимальное количество монет, которое надо перевернуть {count_eagle}')
else:
    print(f'Минимальное количество монет, которое надо перевернуть {count_tails}')