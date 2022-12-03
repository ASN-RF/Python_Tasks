# Задача 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
Vibor_Spiska = int(input('Здравствуйте! Уважаемый проверяющий, как бы Вы хотели проверить решение?\nЕсли хотите использовать Список чисел из примера, то введите "1" и нажмите "Enter",\nесли хотите использовать список из случайных чисел, то введите "2" и нажмите "Enter",\nесли хотите ввести список самостоятельно, то введите "3" и нажмите "Enter"?\nИтак: \n1 - список из примера\n2 - список случайных чисел\n3 - ввести список самостоятельно\n'))
def SumNechetSpisok (Spisok):
        sum = 0
        print(f'{Spisok} -> на нечётных позициях стоят элементы ', end='')
        for i in range(len(Spisok)):
            if i % 2 != 0:
                sum += Spisok[i]
                if i != len(Spisok):
                    print(f'{Spisok[i]}, ', end='')
                else:
                    print(f'и {Spisok[i]},', end='')
        print(f'ответ: {sum}')
if Vibor_Spiska == 1:
    Spisok_1 = [2, 3, 5, 9, 3]
    SumNechetSpisok (Spisok_1)
elif Vibor_Spiska == 2:
    Spisok_2 = []
    Razmer_Spiska = int(input('Введите размер желаемого списка: '))
    for i in range (Razmer_Spiska):
        Spisok_2.append(random.randint(1,10))
    SumNechetSpisok (Spisok_2)
elif Vibor_Spiska == 3:
    Spisok_3 = list(map(int, input('Введити элементы списка:\n').split()))
    print (Spisok_3)
    SumNechetSpisok (Spisok_3)
else:
    print ('К сожалению данный алгоритм поддерживает только 3 варианта. Попробуйте еще раз.')