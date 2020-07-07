def my_func(x, y):
    x_1 = 1
    for i in range(-y):
        x_1 = x_1 * x
    z = 1 / x_1
    return z

while True:
    try:
        a = float(input("Enter first digit: "))
        break
    except ValueError:
        print("Error! Please, enter the digit: ")

while True:
    try:
        b = int(input("Enter integer negative digit: "))
        break
    except ValueError:
        print("Error! Please, enter the integer negative digit: ")

if b < 0 and b % 1 == 0:
    print(my_func(a, b))
else:
    print("Error! The program is finished")
