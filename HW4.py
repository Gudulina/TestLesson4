# 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import math
# from math import pi
# d = list(input('d = '))
# d.pop(0)
# d.pop(0)
# i, j = 0, -1
# d[i], d[j] = d[j], d[i]
# result = (int(''.join(map(str, d))) * 10)
# print(int(pi*result)/result)


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('n = '))
# i = 2
# sp = []
# while i <= n:
#     if n % i == 0:
#         sp.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(sp)


# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = list(input('Введите числа через пробел: ').split())
# def get_unique_sp(numbers):
#     sp = []
#     for i in numbers:
#         if i not in sp:
#             sp.append(i)
#     print(sp)

# get_unique_sp(numbers)


# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*d² + 4*d + 5 = 0 или d² + 5 = 0 или 10*d² = 0

# from random import randint
# import itertools

# k = int(input('k = '))

# def get_koeff(k):
#     koeff = [randint(0, 100) for i in range (k + 1)]
#     while koeff[0] == 0:
#         koeff[0] = randint(1, 100) 
#     return koeff

# def get_polynomial(k, koeff):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(koeff, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')

# koeff = get_koeff(k)
# polynom = get_polynomial(k, koeff)
# print(polynom)

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom)


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from sympy.parsing.sympy_parser import parse_expr

expression = "-2+x^1-3*x^2+x^2+100*x^3-2*x"
x = 0
formula = expression.replace('x', str(x)).replace('^', '**')
print(parse_expr(formula))