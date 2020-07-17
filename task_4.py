class Car:
    def __init__(self, color, name, speed, direction, is_police = False,):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
        self.type_auto = "автомобиль"

    def go(self):
        print(f"{self.type_auto.title()} {self.color} {self.name} поехал.")

    def stop(self):
        print(f"{self.type_auto.title()} {self.color} {self.name} остановился.")

    def turn(self):
        print(f"{self.type_auto.title()} {self.color} {self.name} двигается {self.direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.type_auto[:-1]}я {self.color} {self.name}: {self.speed} км/ч.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание! Превышение скорости на {self.speed - 60}!")
        else:
            print(f"Текущая скорость {self.type_auto[:-1]}я {self.color} {self.name}: {self.speed} км/ч.")


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание! Превышение скорости на {self.speed - 40}!")
        else:
            print(f"Текущая скорость {self.type_auto[:-1]}я {self.color} {self.name}: {self.speed} км/ч.")

class PoliceCar(Car):
    def go(self):
        print(f"{self.type_auto.title()} {self.color} {self.name} включил мигалки и поехал.")

a = TownCar("синяя", "Mazda", 80, "налево")
a.go()
a.stop()
a.turn()
a.show_speed()

b = WorkCar("серый", "Mitsubishi", 50, "направо")
b.go()
b.stop()
b.turn()
b.show_speed()

с = SportCar("красный", "Ferarri", 210, "направо")
с.go()
с.stop()
с.turn()
с.show_speed()

d = PoliceCar("белый", "Chevrolet", 120, "направо")
d.go()
d.stop()
d.turn()
d.show_speed()