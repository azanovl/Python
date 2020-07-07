def int_func(text):
    for i in text:
        if ord(i) in range(97, 123) or ord(i) == 32:
            check = True
        else:
            check = False
            new_text = "Error!!!"
            break
    if check == True:
        new_text = text.title()

    return new_text

my_str = input("Введите строку из слов, разделенных пробелом маленькими латинскими буквами:\n")
print(int_func(my_str))


