# Задача 31. Составить список простых множителей натурального числа N.

def NatyrMnogitel(x):
    Spisok = []
    for i in range(2, x):
        while i <= x:
            while x % i == 0:
                Spisok.append(i)
                x //= i
            else:
                i += 1
    return Spisok

N = int(input('Здравствуйте! Введите Ваше любимое натуральное число:\n'))
if N == 1:
    print(f'Число {N} - простое!')
elif N == 0:
    print(f'{N} - это ноль, а ноль и есть "0"!')
elif N < 0:
    Vibor = str(input(
        f'{N} - это не натуральное число, однако можем попробывать разложить если возьмем его по модулю!\nВзять (да или нет)?\n'))
    if Vibor == 'да':
        N = N*(-1)
        print(f'Число {N} можно разложить на: {NatyrMnogitel(N)}')
        NatyrMnogitel(N)
    if Vibor == 'нет':
        print(f'Желание проверяющего ЗАКОН! Good Bye, Game over!')
elif N > 1:
    print(f'Число {N} можно разложить на: {NatyrMnogitel(N)}')