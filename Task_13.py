# Задача 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
#  вхождений подстроки в строку.
#                   Пример:
#                           Проснувшись однажды утром после беспокойного сна.
#                           Проснувшись однажды утром
#                           Количество вхождений - 1
Stroka = str(input('Введите одно предложение из Вашей любимой книги: '))
Pod_Stroka = str(input('Отлично! А теперь, введите самую любимую часть предложения: '))
N = Stroka.count(Pod_Stroka)
print (f'Количество вхождений: {N}')