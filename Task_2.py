# Задача 2. Найти максимальное из пяти чисел
a = []
for element in input('Введите пять целых чисел, через запятую: \n').split (','): # можно через пробел тогда ....split ():
    a.append(int(element))
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(f'{a} -> {max}')
print(f'Максимальное число = {max}')