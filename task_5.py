with open("data_5.txt", "w", encoding="utf_8") as sum_f:
    sum_f.write(f"2 34 45 54 67 89 43 5 90 238")
sum = 0
with open("data_5.txt", "r", encoding="utf_8") as sum_f:
    num_list = sum_f.readline()
    for i in num_list.split():
        sum += int(i)
print(f"\nСумма всех чисел в файле равна: {sum}")
