# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

lengthChocolate = int(input('Введите длину шоколадки в дольках: '))
widthChocolate = int(input('Введите ширину шоколадки в дольках: '))
sizeBrokenPart = int(input('Введите размер шоколадки в долках, которую хотите отломить: '))

if (sizeBrokenPart % lengthChocolate == 0 or sizeBrokenPart % widthChocolate == 0) and sizeBrokenPart < lengthChocolate * widthChocolate:
  print('Вы разломили шоколадку на два прямоугольника')
else:
  print('Увы, шоколадку на два прямоугольника не разломить')