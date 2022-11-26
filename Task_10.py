# Задача 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# import cmath
# import math
# x1 = int(input('Введите координату X точки A: '))
# y1 = int(input('Введите координату Y точки A: '))
# x2 = int(input('Введите координату X точки B: '))
# y2 = int(input('Введите координату Y точки B: '))
# a = round(math.sqrt(abs(x2-x1)),2)
# b = round(math.sqrt(abs(y2-y1)),2)
# Rastounie = round(math.sqrt(((x2-x1)**2)+((y2-y1)**2)),3)
# print(f'A ({x1},{y1}); B ({x2},{y2}) -> {Rastounie}')

# Варианты представленные в ДЗ:
# 1 вариант
print('Доброго времени суток!')
x1 = int(input('Укажите, координаты точки A\nX = '))        # turn off to enable the second option
y1 = int(input('Y = '))                                     # turn off to enable the second option
x2 = int(input('Укажите, координаты точки B\nX = '))        # turn off to enable the second option
y2 = int(input('Y = '))                                     # turn off to enable the second option
Distance = round((((x2-x1)**2+(y2-y1)**2))**0.5,3)          # turn off to enable the second option
print(f'A ({x1},{y1}); B ({x2},{y2}) --> {Distance}')       # turn off to enable the second option

# 2 вариант
# x = list(map(int, input('Укажите, координаты точки A, отделяя их пробелом и нажмите Enter\n').split(' ')))   # turn off to enable the first option
# y = list(map(int, input('Укажите, координаты точки B, отделяя их пробелом и нажмите Enter\n').split(' ')))    # turn off to enable the first option
# Distance = round((((y[0]-x[0])**2+(y[1]-x[1])**2))**0.5,2)     # turn off to enable the first option
# print (f'A ({x[0]},{x[1]}); B ({y[0]},{y[1]}) --> {Distance}') # turn off to enable the first option