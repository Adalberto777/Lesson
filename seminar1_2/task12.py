# Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: [1, 4, 7, 10, 13, 16, 19]
# Усложнение:
# Создать список, где указанные числа будут стоять на соответствующих индексах, остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1,
# для индекса 4, значение 4 и т.п.
# Пример:
# - Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]

# def List_Number(n):
#     list_num = []
#     list_num_2 = []
#     m = 1

#     for i in range(n+1):
#         m = i * 3 + 1
#         list_num.append(m)

#     for i in range(3 *n + 2):
#         list_num_2.append(0)   

#     for i in range(3 *n + 2):
#         for j in range(n+1):
#             if i == list_num[j]:
#                 list_num_2[i] = list_num[j] 
#     return list_num_2


def List_Number(n):
    list_num = []
       
    for i in range(n+1):
        list_num.append(0)
        list_num.append(i * 3 + 1)
        list_num.append(0)
    list_num.pop()
    return list_num

print('Enter N')
n = int(input())

print(List_Number(n))