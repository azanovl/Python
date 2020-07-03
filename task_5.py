my_list = [7, 5, 3, 3, 2]
print ("The current rating is " + ", ".join(map(str, my_list)))
new_el = float(input("Please, enter a new element to add to the rating: "))
new_list = []
for i in my_list:
    if new_el <= i:
        new_list.append(i)
    elif new_el > i:
        new_list.append(new_el)
        break

if new_el not in new_list:
    new_list.append(new_el)
else:
    for i in range(len(new_list)-1, len(my_list)):
        new_list.append(my_list[i])

print("The new rating is " + ", ".join(map(str, new_list)))