def my_func():
    sum = 0
    while True:
        try:
            my_str = input("Enter the digits separated by a space or 'q' for finish: ")
            my_list = my_str.split()
            for i in my_list:
                if i.lower() == "q":
                    break
                else:
                    i = float(i)
                    sum += i
            print(f"{sum:.2f}")
            i = str(i)
            if i.lower() == "q":
                break
        except ValueError:
            print(f"{sum:.2f}")
            print("Error! Enter only digits for processing or 'q' for finish.")

my_func()





