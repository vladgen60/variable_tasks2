n = int(input('Введите число: '))
count = 1
n_midl = []
n_midl.append(n)

if n==0:
    print('Вы сразу ввели ноль.')
else:
    while n != 0:  
        n = int(input('Введите число: '))
        n_midl.append(n)             
        a = sum(n_midl)  / count     
        count += 1         
    print(f'Среднее число равно: {a}')