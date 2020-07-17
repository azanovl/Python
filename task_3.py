class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        t_inc = self._income.get("wage") + self._income.get("bonus")
        print(f"Доход сотрудника: {t_inc}")

b = Position("Leonid", "Azanov", "manager", 10000, 5000)
b.get_full_name()
b.get_total_income()
