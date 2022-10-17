# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

def check_num(list_scope):
    for i in list_scope:
        if i.isdigit():
            flag = True
            break
        else:
            flag = False
    return flag


list_scope = ["qwe", "asd", "zxc", "111", "erqwe"]

print(check_num(list_scope))