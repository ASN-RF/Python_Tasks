# Задание 2. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


print ('Для упрощения проверки просим выбрать один из вариантов:')
Vibor = int(input('1 - Ввести список самому\n2 - Выбрать список из примера\n'))
if Vibor == 1:
    Spisok = list(input('Введите Ваш список через пробел: ').split())
elif Vibor == 2:
    print ('Выерите какой список Вы хотели бы использовать:')
    Vibor_primera = int(input('1 - ["qwe", "asd", "zxc", "qwe", "ertqwe"]\n2 - ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]\n3 - ["йцу", "фыв", "ячс", "цук", "йцукен"]\n4 - ["123", "234", 123, "567"]\n5 - []\n'))
    if Vibor_primera == 1: 
        Spisok = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    elif Vibor_primera == 2:
        Spisok = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
    elif Vibor_primera == 3:
        Spisok = ["йцу", "фыв", "ячс", "цук", "йцукен"]
    elif Vibor_primera == 4:
        Spisok = ["123", "234", 123, "567"]
    elif Vibor_primera == 5:
        Spisok = []
    else:
        print('Такой вариант не предусмотрен попробуйте снова!')
else:
    print('Такой вариант не предусмотрен попробуйте снова!')
print (f'Вот наш список: {Spisok}')
x = str(input('Что ищем браток?: '))
# 1 вариант
# count = 0
# if x in Spisok:
#     for i in range(len(Spisok)):
#         if Spisok[i] == x:
#             count += 1
#             index = i
#     if count == 2:
#         print (f'Позиция второго вхождения = {index}')
#         print (f'список: {Spisok}, ищем: "{x}", ответ: {index}')
#     if count == 1:
#         print (f'К сожалению данный элемент встречается всего ОДИН раз!!!')
#         print (f'список: {Spisok}, ищем: "{x}", ответ: {-1}')  
# else:
#     print('Что-то ты не то набрал браток!')
#     print (f'К сожалению такого элемента вообще НЕТ в списке!!!')
#     print (f'список: {Spisok}, ищем: "{x}", ответ: {-1}')


# 2 вариант
# def Reshenue(Spisok, Poisk):
#     index = 0
#     count = 0
#     for i in Spisok:
#         if i == Poisk:
#             count += 1
#         if count == 2:
#             index_2 = index
#             break
#         index += 1
#     if count == 0 or count == 1:
#         print(f'список: {Spisok:}: ищем: "{Poisk}", ответ: -1')
#     if count == 2:
#         print(f'список: {Spisok:}: ищем: "{Poisk}", ответ: {index_2}')

# Reshenue(Spisok, x)
# 3 вариант (Семинар)
def Reshenue(Spisok, Poisk):
    count = 0
    for i in range (len (Spisok)):
        if Spisok[i] == Poisk:
            count +=1
            if count == 2:
                 return i
    return -1
print (f'список: {Spisok:}: ищем: "{x}", ответ: {Reshenue(Spisok, x)}')
