def my_func(a, b, c):
    list = [a, b, c]
    max_number = max(a, b, c)
    for i in list:
        if i == max_number:
            list.remove(max_number)
    return max_number + max(list[0], list[1])

num_1 = 107
num_2 = 7
num_3 = 33

print(my_func(num_1, num_2, num_3))