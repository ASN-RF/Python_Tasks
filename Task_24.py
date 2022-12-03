# Задача 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
def Razniza_celoe(y):
    while round((y - y//1), 9) != 0:
        y = round (y * 10, 9)
        y_int = int(y)
    return y_int

def MaxMinFloat(x):
    max = x[0]-int(x[0])
    min = x[0]-int(x[0])
    for i in range(len(x)):
        if max < x[i]-int(x[i]):
            max = x[i]-int(x[i])
        if min > x[i]-int(x[i]):
            min = x[i]-int(x[i])
    print(f'Список: {x} => {round(max-min, 2)} => {Razniza_celoe(round(max-min, 2))}')


Vibor_Spiska = int(input(
    'Здравствуйте! Уважаемый проверяющий, как будет Вам удобно проверить решение?\nЕсли хотите использовать задать cписок вещественных чисел примера, то введите "1" и нажмите "Enter",\nесли хотите использовать список из случайных вещественных чисел, то введите "2" и нажмите "Enter"\nесли хотите ввести сами список, то введите "3"?\nИтак: \n1 - [1.1, 1.2, 3.1, 5, 10.01]\n2 - список случайных вещественных чисел\n3 - хочу ввести свой список!!!\n'))
if Vibor_Spiska == 1:
    Spisok = [1.1, 1.2, 3.1, 5.1, 10.01]
elif Vibor_Spiska == 2:
    Spisok = []
    Dlina_Spiska = int(input('Какой длины Вы бы хотели задать список?\n'))
    for i in range(Dlina_Spiska):
        Spisok.append(round(random.uniform(0.0, 99.0),2))
elif Vibor_Spiska == 3:
    Spisok = []
    Spisok = list(map (float, input('Введите Ваши вещественные числа через пробел!\n').split()))
MaxMinFloat(Spisok)
