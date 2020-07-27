class Data:
    def __init__(self, string):
        self.string = string

    @classmethod
    def op_data(cls, string):
        data = string.split("-")
        return cls.check(data)


    @staticmethod
    def check(data_list):
        leap_year = {1: 30, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        us_year = {1: 30, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if int(data_list[2]) % 4 == 0 and int(data_list[1]) in leap_year and int(data_list[0]) in range(1, (
                leap_year.get(int(data_list[1])) + 1)):
            return f"Дата записана верно:\nЧисло:\t{(data_list[0])}\nМесяц:\t{(data_list[1])}\nГод:\t{(data_list[2])}\n{'-' * 18}"
        elif int(data_list[2]) % 4 != 0 and int(data_list[1]) in us_year and int(data_list[0]) in range(1, (
                us_year.get(int(data_list[1])) + 1)):
            return f"Дата записана верно:\nЧисло:\t{(data_list[0])}\nМесяц:\t{(data_list[1])}\nГод:\t{(data_list[2])}\n{'-' * 18}"
        else:
            return f"Ошибка! Такой даты существовать не может!"

d = Data("29-02-2024")
print(d.op_data(d.string))


