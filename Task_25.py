# Задача 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
# 1 вариант (int)
def TenInTwo(x):
    b = []
    while int(x / 2) != 0:
        b.append(x % 2)
        x = int(x / 2)
        if x == 1:
            b.append(x)
    print("".join(map(str, b)))

# 2 вариант (str)
# def TenInTwo(x):
#     b = ''
#     while x > 0:
#         b = str(x % 2) + b
#         x = x // 2
#     print(b)

Chislo = int(input('Введите Ваше любимое десятичное число:\n'))
print (f'- {Chislo} -> ', end='')
TenInTwo(Chislo)