# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

list_num = []
for i in range(5):
    list_num.append(int(input("Введите число: ")))

max = list_num[0]

for el in list_num:
    if el > max:
        max = el
print(f"Максимальное число из {list_num} будет {max}")