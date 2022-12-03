#  Задача 16. Задайте список из n чисел последовательности (1+1n)n и выведите на экран их сумму.

def Posledov(x):
    sum = 0
    print(f'Для n={x} ', end='')
    print('{', end='')
    for i in range(1, x+1):
        y = round((1+1*i)*i, 2)
        if i < x:
            print(f'{i}: {y}, ', end='')
        else:
            print(f'{i}: {y}', end='')
        sum += y
    print('}')
    print(f'Сумма: {sum}')
Chislo_input = int(input('Введите Ваше любимое число: '))
Posledov(Chislo_input)