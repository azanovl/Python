with open("salary.txt", "r", encoding="utf-8") as salary_f:
    data_salary = salary_f.readlines()
    sum = 0
    print("Сотрудники с доходом менее 20 000 рублей:")
    for i in data_salary:
        sum += int(data_salary[data_salary.index(i)].split()[1])
        imp = data_salary[data_salary.index(i)].split()[0]
        if int(data_salary[data_salary.index(i)].split()[1]) < 20000:
            print(imp)
    print("*" * 50)
    print(f"Средняя величина дохода сотрудников: {sum / (len(data_salary) + 1):.2f}")

