# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую.

# print('Enter N')   это не то, это для проверки символов
# n = int(input())
# list_num = []
# list_num_2 = []
# m = 1
# count = 0

# for i in range(n+1):
#     m = i * 3 + 1
#     list_num.append(m)

# for i in range(3 *n + 2):
#     list_num_2.append(0)   

# for i in range(3 *n + 2):
#     for j in range(n+1):
#         if i == list_num[j]:
#             list_num_2[i] = list_num[j]

# if len(list_num) > len(list_num_2):
#     for i in range(len(list_num)):
#         for j in range(len(list_num_2)):
#             if  list_num[i] == list_num_2[j]:
#                 count += 1 
# if len(list_num) < len(list_num_2):
#     for i in range(len(list_num_2)):
#         for j in range(len(list_num)):
#             if  list_num_2[i] == list_num[j]:
#                 count += 1 

# print(list_num) 
# print(list_num_2)
# print(count)

str_scope = '1285564dasd152asdasd12asdasdaswqe1234'
str_find = '12'

# print (str_scope.count(str_find))

find_count = 0
for i in range(len(str_scope)):
    if str_find == str_scope[i:i+len(str_find)]:    
        find_count += 1

print(find_count)