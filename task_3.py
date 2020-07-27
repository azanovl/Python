class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

f_list = []

while True:
    new_el = input("Enter the number for create list. Enter 'stop' for finish: ")
    if new_el == "stop":
        break
    try:
        if new_el.isdigit() == False:
            raise MyError("Please, you should enter the numbers only! Try again!")
    except MyError as er:
        print(er)
    else:
        f_list.append(new_el)


print(f_list)