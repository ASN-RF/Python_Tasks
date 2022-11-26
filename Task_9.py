# Задача 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).
Chetvert = int(input('Введите номер чертверти: '))
if Chetvert==1:
    print (f'В четверти {Chetvert} точки могут принимать значения: X(0;+oo), Y(0;+oo)')
elif Chetvert==2:
    print (f'В четверти {Chetvert} точки могут принимать значения: X(0;-oo), Y(0;+oo)')
elif Chetvert==3:
    print (f'В четверти {Chetvert} точки могут принимать значения: X(0;-oo), Y(0;-oo)')
elif Chetvert==4:
    print (f'В четверти {Chetvert} точки могут принимать значения:  X(0;+oo), Y(0;-oo)')
else:
    print (f'Пока известно только о 4-х четвертях. Начните заново и введите цифру в диапозоне от 1 до 4!')

# Варианты решения представленные в ДЗ
# 1 вариант
# print('Здравствуйте! Магия продолжается!')
# print('Укажите номер четверти координатной плоскости и Вы узнаете диапазон возможных координат точек в этой четверти!')
# Chetvert = int(input('Итак, какую четверть выбираете:\n'))
#  1 вариант
# if Chetvert == 1:                                                # turn off to enable the second option
#     print (f'Отличный выбор! 1 четверть: X(0;+oo) и Y(0;+oo)') # turn off to enable the second option
# elif Chetvert == 2:                                            # turn off to enable the second option
#     print (f'Замечательно! 2 четверть: X(0;-oo) и Y(0;+oo)')   # turn off to enable the second option
# elif Chetvert == 3:                                            # turn off to enable the second option
#     print (f'Неплохо! 3 четверть: X(0;-oo) и Y(0;-oo)')        # turn off to enable the second option
# elif Chetvert == 4:                                            # turn off to enable the second option
#     print (f'Круто! 4 четверть: X(0;-oo) и Y(0;-oo)')          # turn off to enable the second option
# else:                                                          # turn off to enable the second option
#     print('Мне очень жаль, но пока существует всего 4 координатных плоскости. Не расстраивайтесь! В следующий раз Вам обязательно повезет') # turn off to enable the second option

# 2 вариант                                                      # turn off to enable the first option
# Koordinat = ['(x > 0; y > 0)', '(x < 0; y > 0)', '(x < 0; y < 0)', '(x > 0; y < 0)'] # turn off to enable the first option
# def show_Koordinat(Chetvert, Koordinat):                         # turn off to enable the first option
#     return Koordinat[Chetvert-1]                                 # turn off to enable the first option
# if 0 < Chetvert < 5:                                             # turn off to enable the first option
#     print(f'{Chetvert} четверть имеет координаты: {Koordinat[Chetvert-1]}')  # turn off to enable the first option
# else:                                                            # turn off to enable the first option
#     print('Мне очень жаль, но пока существует всего 4 координатных плоскости. Не расстраивайтесь! В следующий раз Вам обязательно повезет')  # turn off to enable the first option