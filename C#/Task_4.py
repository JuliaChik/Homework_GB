# Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
# 2, 3, 7 -> 7
# 44 5 78 -> 78
# 22 3 9 -> 22

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > b and a > c:
    max = a
if b > a and b > c:
    max = b
else:
    max = c
if a < b and a < c:
    min = a
if b < a and b < c:
    min = b
else:
    min = c
print(f"max: {max}, min: {min}")
