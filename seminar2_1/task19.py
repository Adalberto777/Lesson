# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел
from time import time, perf_counter


for i in range(12):
    s = perf_counter()
    s_1 = int(perf_counter())
    s_2 = int((s - s_1) * 10000000000000000)
    s_3 = s_2 % 10

    print(s_3)
    

