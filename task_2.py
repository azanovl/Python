from random import randint
my_list = [randint(1, 300) for i in range(10)]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_list)
print(new_list)

