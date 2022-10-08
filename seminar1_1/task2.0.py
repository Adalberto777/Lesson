# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
def Max(a, b, c, d, e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    print(max)


print('Enter a')
a = int(input())
print('Enter b')
b = int(input())
print('Enter c')
c = int(input())
print('Enter d')
d = int(input())
print('Enter e')
e = int(input())

Max(a, b, c, d, e)

