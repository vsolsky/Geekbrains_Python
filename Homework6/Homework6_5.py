#Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title=title
    def draw(self):
        return "Start drawing"
class Pen(Stationery):
    def draw(self):
        if self.title=="Pen":
            return "Start drawing Pen"
        else:
            pass
class Pencil(Stationery):
    def draw(self):
        if self.title == "Pencil":
            return "Start drawing Pencil"
        else:
            pass

class Handle(Stationery):
    def draw(self):
        if self.title == "Handle":
            return "Start drawing Handle"
        else:
            pass


title="Pen"

pen=Pen(title)
pencil=Pencil(title)
handle=Handle(title)
print(pen.draw())
print(pencil.draw())
print(handle.draw())
