# Задача 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - умножаем его
# самого на себя.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
Vibor_Spiska = int(input(
    'Здравствуйте! Уважаемый проверяющий, на каком примере Вы бы хотели проверить решение? Если хотите использовать Список чисел из 1-го примера, то введите "1" и нажмите "Enter", если хотите использовать список из 2-го примера, то введите "2" и нажмите "Enter"?\nИтак: \n1 - [2, 3, 4, 5, 6]\n2 - [2, 3, 5, 6]\n3 - Хочу ввести свой список!!!\n'))
Spisok_1 = [2, 3, 4, 5, 6]
Spisok_2 = [2, 3, 5, 6]


def ProizvedParSpiska(Spisok):
    Rezult_Spisok = []
    if len(Spisok) % 2 == 0:
        for i in range(int(len(Spisok)/2)):
            Rezult_Spisok.append(Spisok[i]*Spisok[(len(Spisok)-1)-i])
    else:
        for i in range(int((len(Spisok)-1)/2)):
            Rezult_Spisok.append(Spisok[i]*Spisok[(len(Spisok)-1)-i])
        Rezult_Spisok.append(Spisok[int((len(Spisok)-1)/2)]**2)
    print(f'{Spisok} => {Rezult_Spisok}')


if Vibor_Spiska == 1:
    ProizvedParSpiska(Spisok_1)
elif Vibor_Spiska == 2:
    ProizvedParSpiska(Spisok_2)
elif Vibor_Spiska == 3:
    Spisok_3 = list(map(int, input('Введите свой список целых чисел через пробел:\n').split()))
    ProizvedParSpiska(Spisok_3)
else:
    print('К сожалению данный алгоритм поддерживает только 2 варианта. Попробуйте еще раз.')