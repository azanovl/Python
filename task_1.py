with open("data_1.txt", "w", encoding="utf-8") as data_f:
    while True:
        string = input("Введите новые данные, для выхода из программы нажмите Enter: ")
        data_f.write(string + "\n")
        if string == "":
            break

