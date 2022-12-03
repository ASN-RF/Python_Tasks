# Задача 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#         *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# 1 вариант (один список - добавляем с двух сторон однавременно)
def Negafib_1(x):
    Spisok_Negafib_Pol = [0, 1]
    for i in range(x-1):
        if i == 0:
            Fibonachi = Spisok_Negafib_Pol[i]+Spisok_Negafib_Pol[i+1]
            Spisok_Negafib_Pol.append(Fibonachi)
            Spisok_Negafib_Pol.insert(0, Spisok_Negafib_Pol[i+1])
            Spisok_Negafib_Pol.insert(0, Fibonachi*(-1))
        if i != 0:
            Fibonachi = Spisok_Negafib_Pol[2*i+1]+Spisok_Negafib_Pol[2*i+2]
            Spisok_Negafib_Pol.append(Fibonachi)
            if i % 2 == 0:
                Spisok_Negafib_Pol.insert(0, Fibonachi*(-1))
            else:
                Spisok_Negafib_Pol.insert(0, Fibonachi)
    print(Spisok_Negafib_Pol)

# 2 вариант (два списока - в конце объединяем)
def Negafib_2(x):
    Spisok_Negafib = [1,-1]
    Spisok_Fib = [1,1]
    for i in range(2,x):
        list = Spisok_Fib[i-1]+Spisok_Fib[i-2]
        Spisok_Fib.append(list)
        list_nego = Spisok_Negafib[i-2] - Spisok_Negafib[i-1]
        Spisok_Negafib.append(list_nego)
    Spisok_Negafib.reverse()
    Spisok_Negafib.append(0)
    print(Spisok_Negafib+Spisok_Fib)

Chislo = int(input('Введите Ваше любимое число: '))
if Chislo == 0:
    print (f'- для k = {Chislo} список будет выглядеть так: [0]')
elif Chislo < 0:
    print ('Так как Вы ввели отрицательное число, то мы составим список взяв его по модулю!!! Итак:')
    Chislo *= (-1)
if Chislo > 0:
    print (f'- для k = {Chislo} список будет выглядеть так: ', end='')
    Negafib_1(Chislo)
    # Negafib_2(Chislo)