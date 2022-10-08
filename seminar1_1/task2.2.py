# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
list_num = []
for i in range(5):
    list_num.append(int(input("Введите число: ")))

print(f"Максимальное число из {list_num} будет {max(list_num)}")