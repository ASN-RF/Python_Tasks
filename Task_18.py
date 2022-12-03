# Задача 18. Реализуйте случайное перемешивания списка.
# *Пример:*
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] Результат -> [250, 3.14, 'True ', 'Веселый пианист']
# from importlib.resources import path
import random

List1 = ['Веселый пианист', 250, 3.14, 'True ']
print(f'Исходный вариант -> {List1}', end='')
random.shuffle (List1)
print(f' Результат -> {List1}')
