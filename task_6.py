card_pattern = ["название", "цена", "количество", "ед."]
goods_list = []
goods_card = []
analyse_d = {}
for i in range(1, 4):
    goods_card = input(f"Введите поочередно характеристики товара {i}, разделяя их пробелами: Название, Цену, Количество и Ед. хранения: \n").split()
    goods_list.append((i, {card_pattern[0]: goods_card[0], card_pattern[1]: goods_card[1], card_pattern[2]: goods_card[2], card_pattern[3]: goods_card[3]}))

print(goods_list)

val = []
for index in range(len(card_pattern)):
    for i in range(len(goods_list)):
        val.append(goods_list[i][1].get(card_pattern[index]))
    analyse_d.update({card_pattern[index]: val})
    val = []
print('*' * 100)
print(analyse_d)


