first_num = int(input('Введите первое целое число: '))
second_num = int(input('Введите второе целое число: '))
third_num = int(input('Введите третье целое число: '))
z = []
mn = min(first_num, second_num, third_num)
mx = max(first_num, second_num, third_num)
mm = first_num + second_num + third_num - mn - mx
print(mn,mm,mx)