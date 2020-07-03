# решение задачи через список и словарь
months = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month = 0
while month < 1 or month > 12:
    month = int(input("Для определения времени года, введите месяц в виде целого числа от 1 до 12: "))

for key, value in months.items():
    if month in value:
        print(f"{month}-ый месяц соответствует времени года: {key}")
