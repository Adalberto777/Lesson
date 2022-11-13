# Напишите программу вычисления арифметического выражения заданного строкой.
# Возможные операции в выражении только: +,-,/,*. приоритет операций стандартный.
# Техническое задание:
# 1) Числа могут быть только целые, любой размерности
# 2) Унарный оператор минус не рассматриваем, т.е. '-2*3' недопустимо
# 3) Не используйте функцию eval.
# 4) Программа возвращает результат вычисления в виде числа.
# Пример:
# '2+2' -> 4
# '1+2*3' -> 7
# '1-2*3' -> -5
# '1-2*33' -> -65
# '2-1+3*7' -> 10
# '1-2*3/5' -> -0.2
# '1+2*3-6*5+78' -> 55
# Общая схема решения:
# 1) Выделить части алгоритма, использовать для них функции.
# 2) Протестировать функции на множестве примеров, убедиться в правильности работы. Создать "модуль тестирования".
# Усложнение:
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# - Скобки рассматриваем однократные, нет учета вложенных скобок.
# - Не забыть протестировать граничные случаи: скобка в начале и/или в конце строки
# Пример:
# '(1+2)*3' -> 9;
# '(1-2)*3/5' -> -0.6
# '(1+2)*3-6*(5+78)' -> -489
# '(1+2)*(3-6)*(5+78)' -> -747


def pars_str(my_str: str) -> list:
    new_list = []
    idx_d = 0
    for idx, el in enumerate(my_str):
        if el in "-+*/":
            new_list.append(my_str[idx_d:idx])
            new_list.append(el)
            idx_d = idx + 1
    new_list.append(my_str[idx_d:])
    print(new_list)


def run(new_list):
    temp = 0
    tmp_list = new_list.copy()
    length = len(tmp_list)
    idx = 0

    while idx < length:
        elem = tmp_list[idx]
        if elem == '*':
            temp = tmp_list[idx-1] * tmp_list[idx+1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        elif elem == '/':
            temp = tmp_list[idx-1] / tmp_list[idx +1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        else: idx += 1
    length = len(tmp_list)
    idx = 0
    return tmp_list[0]







my_str ='1+2*3-6*5+78'

pars_str(my_str)
