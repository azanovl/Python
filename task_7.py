import json

result_list = [{}, {}]
with open("data_7.txt", "r", encoding="utf-8") as bis_f:
    av_profit = 0
    i = 0
    for line in bis_f.readlines():
        fin_res = int(line.split()[2]) - int(line.split()[3])
        result_list[0].update({line.split()[0]: fin_res})
        if fin_res >= 0:
            av_profit += fin_res
            i += 1
    result_list[1].update({"average_profit": (av_profit / i)})

print(result_list)

with open("text_77.json", "w", encoding="utf-8") as data_f:
    json.dump(result_list, data_f, ensure_ascii=False)