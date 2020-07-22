from abc import ABC, abstractmethod

class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return (self.num - other.num) if self.num > other.num else f"Операцию выполнить невозможно!"

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return round((self.num / other.num)) if self.num > other.num else f"Операцию выполнить невозможно!"

    def make_order(self, len_raw):
        return "\n".join(['*' * len_raw for _ in range(self.num // len_raw)]) + '\n' + '*' * (self.num % len_raw)

cell_1 = Cell(15)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))