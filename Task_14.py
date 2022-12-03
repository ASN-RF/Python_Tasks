# Задача 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его 
# цифр(отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

Chislo_input = float(input('Введите Ваше любимое вещественное число: '))
# 1 вариант (Числа)
Chislo = Chislo_input
if Chislo < 0:
    Chislo*=(-1)
count = 0
while round((Chislo - Chislo//1), 9) != 0:
    Chislo = round (Chislo * 10, 9)
Chislo_int = int(Chislo)
while Chislo_int%10 !=0:
    count = count + Chislo_int%10
    Chislo_int= Chislo_int//10
print(f'{Chislo_input} -> {count}')