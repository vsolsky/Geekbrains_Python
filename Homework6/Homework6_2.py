#Реализовать класс Road (дорога).

# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width,thickness):
        self._length=length
        self._width=width
        self._thickness=thickness
    def asphalt_mass(self):
        print(f"Asphalt weight is = : {(self._length*self._width*self._thickness*25)/1000} tonnes")


length = int(input("Enter length in meters: "))
width = int(input("Enter width in meters: "))
thickness = int(input("Enter thickness in centimeters: "))
rd=Road(length, width, thickness)
rd.asphalt_mass()


