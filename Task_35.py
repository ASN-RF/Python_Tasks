# Задача № 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
path = 'Task_35.txt'
data = open(path, 'r')
Spisok = []
lines = data.readlines()
for i in lines:
    temp = i.split()
    Spisok.extend(temp)
Spisok = list(map(int, Spisok))
Rezult = []
for i in range(1, len(Spisok)):
    if Spisok [i]-1 != Spisok[i-1]:
        count = Spisok [i]-1
print (f'Нашел!!! Нашел!!! Тут не зватает: {count}')
data.close()
print(Spisok)