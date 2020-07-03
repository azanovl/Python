user_string = input("Enter a list of values separated by a space in the string: ")
user_list = user_string.split(" ")
format_list = []

for i in user_list:
    if user_list.index(i) == 0:
        format_list.append(user_list[user_list.index(i) + 1])
        format_list.append(user_list[user_list.index(i)])
    elif user_list.index(i) == len(user_list) - 1 and len(user_list) != len(format_list):
        format_list.append(user_list[user_list.index(i)])
    elif user_list.index(i) % 2 == 0:
        format_list.append(user_list[user_list.index(i) + 1])
        format_list.append(user_list[user_list.index(i)])

print(f"The origin list before processing: {', '.join(user_list)}")
print(f"The new list after processing:     {', '.join(format_list)}")

