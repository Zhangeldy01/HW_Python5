# Задача 26:
# Напишите программу, которая на вход принимает два числа А и В, 
# и возводит число А в целую степень В с помощью рекурсии. 
# *Пример:*
# А = 3; В = 5 -> 243 (35)
# A = 2; B = 3 -> 8

def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a, -b)
    if b % 2 == 0:
        return power(a, b // 2) * power(a, b // 2)

    return power(a, b - 1) * a

a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
print(power(a, b))

