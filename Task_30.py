# Задача 30. Вычислите число Пи с заданной точностью d:
# Пример: при d=0,001, Пи= 3,141. 10^-1<=d<=10^-10
import math
def Pi_Var_1(x):
    count = 0
    Pi = 0
    for i in range(1, 10**x, 2):
        if count % 2 == 0:
            Pi += 4/i
        elif count % 2 != 0:
            Pi -= 4/i
        count += 1
    return (round(Pi, x))
def Pi_Var_2(d) -> float:
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d)


Vibor = float(input('Здравствуйте! Хотите проверить работу на точности из примера или ввести самому?\n1 - Использовать точность из примера.\n2 - Ввести самому.\n'))
if Vibor == 1:
    d = 3
    print (f'1 вариант - С точностью {0.001}, число Пи = {Pi_Var_1(d)}')
    print(f'2 вариант - С точностью {0.001}, число Пи = {Pi_Var_2(d)}; ')
    
elif Vibor == 2:
    Tocnost = float(input('Введите точность определения числа Пи (количество знаков после запятой):\n'))
    if Tocnost < 1:
        d = 0
        while Tocnost < 1:
            d += 1
            Tocnost *= 10
        print (f'1 вариант - С точностью {d} знаков после запятой, число Пи = {Pi_Var_1(d)}')
        print (f'2 вариант - С точностью {d} знаков после запятой, число Пи =  {Pi_Var_2(d)}; ')
    else:
        Tocnost = int(Tocnost)
        print(f'1 вариант - С точностью {Tocnost} знаков после запятой, Пи = {Pi_Var_1(Tocnost)}')
        print(f'2 вариант - С точностью {Tocnost} знаков после запятой, число Пи =  {Pi_Var_2(Tocnost)}; ')