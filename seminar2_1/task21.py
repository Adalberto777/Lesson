# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1

def check_find(list_scope, find, req_find):
    count = 0
    
    for i in range(len(list_scope)):
        if find == list_scope[i]:
            count += 1
            if count == req_find:
                result = i
                break

    if count <= 1:
        result  = - 1
    
    return result


list_scope = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find = "qwe"
req_find = 2

print(check_find(list_scope, find, req_find))