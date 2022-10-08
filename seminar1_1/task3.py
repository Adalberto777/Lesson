# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

print('Enter N')
n = int(input())

for i in range(-n, n):
    print(i, end=", ")
print(n)