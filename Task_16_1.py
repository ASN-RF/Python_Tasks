#  Задача 16_1. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
#     *Пример:*
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def Posledov(x):
    sum = 0
    print(f'Для n={x} ', end='')
    print('{', end='')
    for i in range(1, x+1):
        y = round((1+1/i)**i, 2)
        if i < x:
            print(f'{i}: {y}, ', end='')
        else:
            print(f'{i}: {y}', end='')
        sum += y
    print('}')
    print(f'Сумма: {sum}')
Chislo_input = int(input('Введите Ваше любимое число: '))
Posledov(Chislo_input)