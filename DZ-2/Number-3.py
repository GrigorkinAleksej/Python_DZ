# Задача 3.
# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.


import math
import fractions


def input_drob(text1, text2):
    # преобразование строки вида a/b в целые числитель и знаменатель
    while True:
        drob = input(text1)
        for i in range(len(drob)):
            if drob[i] == '/':
                break
        a = drob[:i]
        b = drob[i+1:]
        if str.isdigit(a) and str.isdigit(b):
            break
        print(text2)
    return int(a), int(b)


text1 = 'Введите первую дробь вида a/b '
text2 = 'Числитель и знаменатель должны быть натуральными числами'
chisl1, znam1 = input_drob(text1, text2)
text1 = 'Введите вторую дробь вида a/b '
chisl2, znam2 = input_drob(text1, text2)

nod = math.gcd(znam1, znam2)
chisl_sum = int(chisl1*znam2/nod+chisl2*znam1/nod)
znam_sum = int(znam2*znam1/nod)
nod = math.gcd(chisl_sum, znam_sum)
chisl_sum = int(chisl_sum / nod)
znam_sum = int(znam_sum / nod)
chisl_prod = chisl1*chisl2
znam_prod = znam1*znam2
nod = math.gcd(chisl_prod, znam_prod)
chisl_prod = int(chisl_prod / nod)
znam_prod = int(znam_prod / nod)
print(f'{chisl1}/{znam1} + {chisl2}/{znam2} = {chisl_sum}/{znam_sum}')
print(f'{chisl1}/{znam1} * {chisl2}/{znam2} = {chisl_prod}/{znam_prod}')

# Расчёт с помощью библиотеки fractions
drob1 = fractions.Fraction(chisl1, znam1)
drob2 = fractions.Fraction(chisl2, znam2)
print(f'{drob1} + {drob2} = {drob1+drob2}')
print(f'{drob1} * {drob2} = {drob1*drob2}')
