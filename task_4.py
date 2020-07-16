en_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
num_f = open("data_4.txt", "r", encoding="utf-8")
new_d_f = open("new_data_4.txt", "w", encoding="utf-8")
for i in num_f:
    if i.split()[0] in en_dict:
        print(f"{en_dict.get(i.split()[0])} {' '.join(i.split()[1:])}", file=new_d_f)
num_f.close()
new_d_f.close()

