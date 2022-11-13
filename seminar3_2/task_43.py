# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] -> [2, 10]
# [1, 2, 3, 5, 1, 5, 3, 10, 1] -> [2, 10]
# [1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9] -> [4,5,7,9]
# Примечание:
# В этой задаче есть вариант решения "в лоб"(используя списки) или решения эффективного(используя множества)

def mod_lst(sours_lst: list) ->list:
    # result_lst = []
    # for el in sours_lst: 
    #     if sours_lst.count(el) == 1:
    #         result_lst.append(el)
    # return result_lst
    return [el for el in sours_lst if sours_lst.count(el) == 1]
    

sours_lst = [1, 2, 3, 5, 1, 5, 3, 10]

print(mod_lst(sours_lst))