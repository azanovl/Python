class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

f_num = input("Enter first number: ")
s_num = input("Enter second number for divide: ")

try:
    if int(s_num) == 0:
        raise MyError("Error! Division by zero is not possible!")
    res = round((int(f_num) / int(s_num)), 2)
except ValueError:
    print("Error! You should enter numbers only!")
except MyError as er:
    print(er)
else:
    print(f"The result of the division: {res}")
finally:
    print(f"{'-' * 35}\nThe program is completed.")