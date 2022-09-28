# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
#    координат точек в этой четверти (x и y).

list = (1,2,3,4)
quarter = int(input("Введите номер четверти: "))
if quarter == list[0]:
    print("x > 0, y > 0")
elif quarter == list[1]:
    print("x < 0, y > 0")
elif quarter == list[2]:
    print("x < 0, y < 0")
elif quarter == list[3]:
    print("x > 0, y < 0")
else:
    print("Нет такой четверти")