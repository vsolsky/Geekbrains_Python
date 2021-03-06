#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothing (ABC):
    @abstractmethod
    def material_usage (self,size):
        pass
class Suit(Clothing):
    def material_usage (self,height_suit):
        return round(2*height_suit+0.3,2)
class Coat(Clothing):
    @property
    def material_usage(self):
        return round(self.size_coat/6.5+0.5,2)
    @material_usage.setter
    def material_usage(self, size_coat):
        self.size_coat=size_coat

suit=Suit()
coat=Coat()
height_suit=int(input("Enter your height for suit: "))
coat.size_coat=int(input("Enter your size for coat: "))

print(suit.material_usage(height_suit))
print(coat.material_usage)


