# Задача 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух
# чисел.

def NOK_Algoritm_Evklida(x, y):
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x
    while max % min != 0:
        z = max-min
        max = min
        min = z
        if max < min:
            q = max
            max = min
            min = q
    NOD = min
    NOK = int((x*y) / NOD)
    print(f'1 ВАРИАНТ (Алгоритм Евклида):\nНаименьшее общие кратное чисел {x} и {y}, будет => НОК = {NOK}\nДля справки: НОД будет равен => {NOD}')


def Prostie(x):
    Prostie_MN = []
    count = 2
    while count * count <= x:
        if x % count == 0:
            Prostie_MN.append(count)
            x //= count
        else:
            count += 1
    if x > 1:
        Prostie_MN.append(x)
    return Prostie_MN


def NOK_Razlozenie(x, y):
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x
    max_prostie = Prostie(max)
    min_prostie = Prostie(min)
    obshie_prostie = []
    for i in min_prostie:
        if i not in max_prostie:
            obshie_prostie.append(i)
    obshie_prostie += max_prostie
    NOK = 1
    for i in obshie_prostie:
        NOK *= i
    print(f'2 ВАРИАНТ:\nНаименьшее общие кратное чисел {x} и {y}, будет => НОК = {NOK}')

Chislo_1 = int(input('Введите первое число:\n'))
Chislo_2 = int(input('Введите второе число:\n'))
NOK_Algoritm_Evklida(Chislo_1, Chislo_2)
NOK_Razlozenie(Chislo_1, Chislo_2)
