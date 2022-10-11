# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Для N = 5: 1, -3, 9, -27, 81
def List_Number(n):
    list_num = []
    m = 1
    for i in range(n):
        list_num.append(m)
        # if i % 2 == 0:
        #     m = - (m * 3)
        # else: m = (m * 3)
        m = m *(- 3)    
    return list_num

print('Enter N')
n = int(input())
    
print(List_Number(n)) 