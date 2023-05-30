# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
# Если таких элементов несколько, вы вывести один любой. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X
from random import randint

N = int (input ('Введите кол-во элементов в массиве '))
random_list = [randint(1, 30) for i in range(N)]
print(random_list)
X = int(input('Введите число X: '))
min = abs(X - random_list[0])
element = 0
for i in range(1,N):
    count = abs(X - random_list[i])
    if count < min:
        min = count
        element = i
print(random_list[element])

