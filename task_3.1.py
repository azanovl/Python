#решение задачи через список
months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ["Зима", "Весна", "Лето", "Осень"]
month = 0
while month < 1 or month > 12:
    month = int(input("Для определения времени года, введите месяц в виде целого числа от 1 до 12: "))
for i in months:
    for el in i:
        if month == el:
            print(f"{month}-ый месяц соответствует времени года: {seasons[months.index(i)]}")

            

