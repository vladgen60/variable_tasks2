import math

a1 = float(input('Введите широту первой точки: '))
a2 = float(input('Введите долготу первой точки: '))
b1 = float(input('Введите широту второй точки: '))
b2 = float(input('Введите долготу второй точки: '))


t1 = math.radians(a1)
t2 = math.radians(a2)
g1 = math.radians(b1)
g2 = math.radians(b2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(distance + 'km')