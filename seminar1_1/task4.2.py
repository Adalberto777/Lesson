# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

print('Enter N')
num = input()
lst = num.split(",") # строку разбиваем сплитом по признаку "," на две части и заносим в список 6,355 получаем ["6", "355"]
print(lst[1][0]) # выводим на экран первый (0) элемент второго элемента списка (1)

print(num[num.find(",") + 1]) # или при помощи функции find находим номер элемента строки "," и выводи следующий за ней элемент 