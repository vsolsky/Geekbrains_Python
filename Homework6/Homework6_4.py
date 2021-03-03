# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go_m(self):
        return "The car is going straight"
    def stop_m(self):
        return "The car stopped"
    def turn_m(self, direction):
        if direction=="Right":
            return "The car turned right"
        elif direction == "Left":
            return "The car turned left"
        else:
            return "You did nto specify the direction properly, enter Left or Right"
    def show_speed_m(self):
        return f"The car speed is {self.speed}"
    def color_m(self):
        return f"The car color is {self.color}"
    def name_m(self):
        return f"The car name is {self.name}"
    def is_police_m (self):
        if self.is_police==True:
            return "The car is police"
        else:
            return "The car is regular"
class SportsCar(Car):
    pass
class PoliceCar(Car):
    pass

class TownCar(Car):
    def show_speed_m(self):
        if self.speed>60:
            return f"You have reached the speed limit of 60 km/h, you speed is {self.speed}"
        else:
            return f"Your speed is {self.speed}"

class WorkCar(Car):
    def show_speed_m(self):
        if self.speed >40:
            return f"You have reached the speed limit of 40 km/h, your speed is {self.speed}"
        else:
            return f"Your speed is {self.speed}"

speed=80
color="Blue"
name="Bugatti"
turn="Right"

sport=SportsCar(speed,color,name)
police=PoliceCar(speed,color,name,True)
towncar=TownCar(speed,color,name)
workcar=WorkCar(speed,color,name)

print ("\n Sport car data:")
print (sport.go_m())
print(sport.stop_m())
print(sport.turn_m(turn))
print(sport.show_speed_m())
print(sport.color_m())
print(sport.name_m())
print(sport.is_police_m())

print ("\n Police car data:")
print (police.go_m())
print(police.stop_m())
print(police.turn_m(turn))
print(police.show_speed_m())
print(police.color_m())
print(police.name_m())
print(police.is_police_m())

print ("\n Town car data:")
print (towncar.go_m())
print(towncar.stop_m())
print(towncar.turn_m(turn))
print(towncar.show_speed_m())
print(towncar.color_m())
print(towncar.name_m())
print(towncar.is_police_m())

print ("\n Work car data:")
print (workcar.go_m())
print(workcar.stop_m())
print(workcar.turn_m(turn))
print(workcar.show_speed_m())
print(workcar.color_m())
print(workcar.name_m())
print(workcar.is_police_m())