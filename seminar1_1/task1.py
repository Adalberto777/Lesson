# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
def Check(a, b):
    if a == (b * b) or b == (a * a):
        print('да')
    else:
        print('нет')


print('Enter a')
a = int(input())
print('Enter b')
b = int(input())

Check(a, b)


