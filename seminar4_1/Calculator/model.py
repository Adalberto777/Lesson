# вычисление общего наименьшего знаменателя
def lcm(num_1, num_2) -> int:
    i = max(num_1, num_2)
    while ((i % num_1 != 0) or (i % num_2 != 0)):
        i += 1
    return i


# Парсинг строки. (строка) -> (список)
def parsing(my_str: str) ->list:
    if "/" in my_str:
        new_list = my_str.split("/")
        new_list = [int(el) for el in new_list]
    else:
        new_list = [int(my_str), 1]
    return new_list


# вычисление
def calculate(num_1: list, num_2: list, op: str) -> list:
    numer1, denom1 = num_1
    numer2, denom2 = num_2
    nok = lcm(num_1[1], num_2[1])
    cf1 = nok // denom1
    cf2 = nok // denom2
    if op == '+':
        return [numer1 * cf1 + numer2 * cf2, nok]
    elif op == '-':
        return [numer1 * cf1 - numer2 * cf2, nok]
    elif op == '*':
        return [numer1 * numer2, denom1 * denom2]
    elif op == '/':
        return [numer1 * denom2, denom1 * numer2]


def new_parsing(my_list: list) -> str:
    my_str = []
    if my_list[1] > 1:
        my_str = str(my_list[0]) + "/" + str(my_list[1])
    else: my_str = str(my_list[0])
    return my_str


