# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 50 -> 1, 2, 4, 8, 16, 32

N = int(input('Введите максимальную границу N: '))
def powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power *= 2
print(powers_of_two(N))
