import math

r = float(input('Введите радиус: '))
area = math.pi * r ** 0.5
volume = 4/3 * math.pi * (r ** 3)
print(f'Площадь круга ровна {area: {3}.{4}}')
print(f'Объем шара равен: {volume: {3}.{5}}')