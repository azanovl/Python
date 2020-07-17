class Stationery:
    title = "Канцелярские товары"

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Выбрана ручка! Запуск отрисовки.")

class Pencil(Stationery):
    def draw(self):
        print("Выбран карандаш! Запуск отрисовки.")

class Handle(Stationery):
    def draw(self):
        print("Выбран маркер! Запуск отрисовки.")

a = Pen()
b = Pencil()
c = Handle()
print(a.title)
a.draw()
b.draw()
c.draw()
