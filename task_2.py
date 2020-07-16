with open("data_2.txt", "r", encoding="utf-8") as data_f:
    data_list = data_f.readlines()
    print(f"Всего в файле строк: {len(data_list)}")
    for line in data_list:
        print(f"В строке номер {data_list.index(line) + 1} всего слов {len(line.split())}")

