# : Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
m=input('Введите номер билета ')
m1=int(m[0])+int(m[1])+int(m[2])
m2=int(m[3])+int(m[4])+int(m[5])
if m1==m2:
    print("yes")
else:
    print("now")