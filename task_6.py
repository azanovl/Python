sched_dict = {}
key_list = []
value_list = []
with open("data_6.txt", "r", encoding="utf_8") as sched_f:
    data = sched_f.readlines()
    for i in range(len(data)):
        key_list.append(data[i].split(":")[0])
    for i in range(len(data)):
        hours = []
        for n in data[i].split():
            count = ""
            for d in n:
                if d.isdigit():
                    count += str(d)
            if len(count) > 0:
                hours.append(count)
        sum_h = 0
        for h in hours:
            sum_h += int(h)
        value_list.append(sum_h)
for i in range(len(key_list)):
    sched_dict.update({key_list[i]: value_list[i]})
print(sched_dict)