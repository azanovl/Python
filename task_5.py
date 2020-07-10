from random import randrange
from functools import reduce

gen_list = [el for el in range(100, 1001) if el % 2 == 0]

def my_func(a, b):
    return a * b

print(reduce(my_func, gen_list))

