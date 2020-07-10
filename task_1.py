from sys import argv

hours, w_rate, bonus = argv[1:]

print("Выработка в часах: ", hours)
print("Ставка заработной платы: ", w_rate)
print("Премия: ", bonus)
print((int(hours) * int(w_rate)) + int(bonus))

