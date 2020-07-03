user_string = input("Наберите несколько слов, разделяя их пробелами: ")
i = 0
for el in user_string.split():
    i += 1
    print(f"{i}: {el[:10]}")