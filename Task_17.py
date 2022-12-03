# Задача 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random


def Zadanie(x):
    Spisok = []                                     # Можно заполнить с шагом 2, тогда !!!for i in range(-x,x,2):!!!
                                                    # Spisok.append(i) - будет простая последовательность
    for i in range(x):                              # Для наглядности и возможности проверки
        Spisok.append(random.randint(-x, x+1))
    print(f'Зададим список из {x} элементов:                         {Spisok}')
    Pozichii = 'file.txt'
    data = open(Pozichii, 'r')
    rezult = 1
    rezult_str = ''
    q = list(map(int, data.read().split('\n')))
    print(f'Прочитаем и конвертируем список позиций из файла:      {q}')
    for i in q:                                # проверяет номер позиции в файле file.txt меньше длины списка
        if i < len(Spisok):                    # если будет больше, то такого элемента в списке небудет (ошибка)
            rezult = rezult * Spisok[i]
            rezult_str += str(Spisok[i]) + ' * '  
    rezult_str = rezult_str[:-3]                # т.к. ' x ' - 3 символа
    print(f'Произведение элементов на указанных позициях в файла = {rezult}')
    print (f'Проверим, правильно ли посчитали:                      {rezult_str} = {rezult}') 
    data.close()
Chislo_input = int(input('Введите Ваше любимое число: '))
Zadanie(Chislo_input)
