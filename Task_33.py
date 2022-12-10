# Задача № 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int (input('Введите натуральную степень многочлена:\n')) #Для пользователя
# k = 2
def Spisok_Kof(k):
    # List_kof = []                                            # Заменил на List Comprehensions
    # for i in range(k+1):                                     # Заменил на List Comprehensions
    #     List_kof.append(random.randint(0, 100))              # Заменил на List Comprehensions
    List_kof = [random.randint(0, 100) for i in range((k+1))]  # <= Вот на него заменил
    with open ('Task_33.txt', 'w') as data:
        data.write(f'For k={k} => ')
    data = open('Task_33.txt', 'a')
    for i in range(k+1):
        if ((k+1)-i) <= 1:
            data.write(f'{List_kof[i]} = 0')
            # print(f'{List_kof[i]} = 0', end='')             # Для вывода в консоль (необязательно активировать)
        else:
            if (k-i) == 1:
                data.write(f'{List_kof[i]}*x')
                # print(f'{List_kof[i]}*x', end='')           # Для вывода в консоль (необязательно активировать)
            else:
                data.write(f'{List_kof[i]}*x^{(k-i)}')
                # print(f'{List_kof[i]}*x^{(k-i)}', end='')   # Для вывода в консоль (необязательно активировать)
            data.write(' + ')
            # print(' + ', end='')                            # Для вывода в консоль (необязательно активировать)
    data.close()
Spisok_Kof(k)