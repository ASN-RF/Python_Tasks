# Задача 4. Показать первую цифру дробной части числа. Напишите программу, которая будет принимать на вход 
# дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3
# 1 вариант
# x = float(input('Введите Ваше любимое число:\n'))
# y = x % 1
# a = int(x)
# y = int((x-a)*10)
# if y == 0:
#     print(f'{x} => НЕТ')
# else:
#     print(f'{x} => {y}')

# 2 вариант
a = float(input('Введите Ваше любимое число:\n'))
if a%1 != 0:
    x = int(((a-int(a))*10))
    print(f'{a} -> {x}')
else:
    print(f'{int(a)} -> нет')