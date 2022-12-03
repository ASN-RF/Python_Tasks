# Задача 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# Для N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

def Opisanie(x):
    print(' (', end='')
    for i in range(x):
        for j in range(1, i+2):
            print(j, end='')
        if i == x-1:
           print(')', end='')
        else:
            print(', ', end='')
def Nabor (x):
    count = 1
    Rezult = []
    for i in range(1, x+1):
        count *= i
        Rezult.append(count)
    print (Rezult, end='')
Chislo_input = int(input('Введите Ваше любимое число: '))
print (f'Для N = {Chislo_input}, тогда ', end='')
Nabor(Chislo_input)
Opisanie(Chislo_input)