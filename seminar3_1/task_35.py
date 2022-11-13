# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось 
# условие A[i] - 1 = A[i-1]. Найдите это число.
# Для работы с файлами используйте менеджер контекста
import os
os.system('cls||clear')

def read_data(filename: str) -> list:
    with open(filename, "r", encoding = "utf-8") as data:
        a = data.read().split()
        a = [int(elem) for elem in a] # или a =  list(map(int,a))
    return a
num_lst = read_data("test_35.txt")

def check_data(my_list: list) -> int:
    for i in range(1,len(my_list)):
        if my_list[i] - 1 != my_list[i-1]:
            return my_list[i] - 1


print(check_data(num_lst))