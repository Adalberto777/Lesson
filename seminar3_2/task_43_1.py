# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] -> [2, 10]
# [1, 2, 3, 5, 1, 5, 3, 10, 1] -> [2, 10]
# [1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9] -> [4,5,7,9]
# Примечание:
# В этой задаче есть вариант решения "в лоб"(используя списки) или решения эффективного(используя множества)

def unique_set(sours_lst: list) ->list:
    unique = set()
    not_unique = set()
    for el in sours_lst:
        if el in unique:
            unique.remove(el)
            not_unique.add(el)
        elif el not in not_unique:
            unique.add(el)
    return list(unique)


sours_lst = [1, 2, 3, 5, 1, 5, 3, 10]

print(unique_set(sours_lst))
    

