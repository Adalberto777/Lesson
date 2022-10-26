# Найти элементы элементы более 5 и записать их квадрат ы в другой список с использованием compi hanchen 
lst_1 = [1, 2, 3, 6, 78, 456, 3, 55, 89, 78]
lst_2 = []

for el in lst_1:
    if el > 5:
        lst_2.append(el ** 2)


lst_3 = [el** 2 for el in lst_1 if el > 5]
print(lst_2)
print(lst_3)