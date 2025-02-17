wind = int(input('Введите скорость ветра: '))
temp = int(input('Введите температуру: '))

koef = 13.12 + 0.6215 * temp - 11.37 *  (wind ** 0.16) + 0.3965 * temp * (wind ** 0.16)
print('Температура с учетом ветра: {0:4.1f}'.format(koef)) 