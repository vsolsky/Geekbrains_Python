# Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self,name, surname, wage, bonus):
        self.name=name
        self.surname=surname
        self._income={"wage":wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Employee full name is {self.name} {self.surname}")
    def get_total_income(self):
        total_income=self._income["wage"]+self._income["bonus"]
        print(total_income)

name="Vadym" #input("Enter name: ")
surname="Solskyy" #input("Enter surname: ")
wage=100 #int(input("Enter wage: "))
bonus=50 #int(input("Enter bonus"))
position=Position(name,surname,wage,bonus)
position.get_full_name()
position.get_total_income()