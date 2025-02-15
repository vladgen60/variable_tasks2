import math

r = float(input('Введите радиус основания: '))
h = float(input('Введите высоту цилиндра: '))

vol = (math.pi * r ** 2) * h

print(f'Объем цилиндра равен: {vol:{4}.{12}}')