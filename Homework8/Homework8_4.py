# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на
# склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


import json

""" Class Warehouse - adds dictionary that it receives from Office_equipment subclasses into Jason file"""


class Warehouse:
    def __init__(self, product_dict):
        self.product_dict = product_dict  # dictionary with products details

    def add_line_to_DB(self):
        tovary_db_list = []
        tovary_db_list.append(product_dict)
        with open("Homework8_4_JSON.json", "a+") as write_f:
            json.dump(tovary_db_list, write_f)


class Office_equipment:
    def __init__(self, brand, model, price, size, quantity, department):
        self.price = price
        self.size = size
        self.brand = brand
        self.model = model
        self.quantity = quantity
        self.department = department

    """entry_validation - method that validates entered data. Use staticmethod to avoid calling class"""

    @staticmethod
    def entry_validation(price, quantity, number_pages_printed):
        try:
            int(price) == price
            int(quantity) == quantity
            int(number_pages_printed) == number_pages_printed
            return print("All data accurately entered and added to the database, thank you!")
        except ValueError:
            print("You entered str instead of integer in one of the fields, no entry added to the database")


"""Printer/ Scanner/Copier - are classes that are repsoncible for compiling the entered data into dictionary 
that will be added to the Json file"""


class Printer(Office_equipment):
    def __init__(self, brand, model, price, size, quantity, department, number_pages_printed):
        """

        :type number_pages_printed: specifies how many pages the printer prints per minute
        """
        super().__init__(brand, model, price, size, quantity, department)
        self.number_pages_printed = number_pages_printed

    def line_compilation(self):
        return {"brand:": self.brand, "model": self.model, "price": self.price, "size": self.size,
                "quantity": self.quantity,
                "department": self.department, "number of pages": self.number_pages_printed}


class Scanner(Office_equipment):
    def __init__(self, brand, model, price, size, quantity, department, number_pages_scanned):
        super().__init__(brand, model, price, size, quantity, department)
        self.number_pages_scanned = number_pages_scanned

    def line_compilation(self):
        return {"brand:": self.brand, "model": self.model, "price": self.price, "size": self.size,
                "quantity": self.quantity,
                "department": self.department, "number of pages": self.number_pages_scanned}


class Copier(Office_equipment):
    def __init__(self, brand, model, price, size, quantity, department, number_pages_copied):
        super().__init__(brand, model, price, size, quantity, department)
        self.number_pages_copied = number_pages_copied

    def line_compilation(self):
        return {"brand:": self.brand, "model": self.model, "price": self.price, "size": self.size,
                "quantity": self.quantity,
                "department": self.department, "number of pages": self.number_pages_copied}


type_item = input("What type of product (1-printer, 2-scanner, 3-Copier): ")
brand = input("Enter the brand: ")
model = input("Enter the model: ")
price = input("Enter price: ")
size = input("Enter size: ")
quantity = input("Enter quantity: ")
number_pages = input("Enter number of pages that product can process (print/ scan/ copy per minute): ")
department = input("Enter which department will own this item: ")

Office_equipment.entry_validation(price, quantity, number_pages)

if type_item == 1:
    printer = Printer(brand, model, price, size, quantity, department, number_pages)
    product_dict = printer.line_compilation()
    warehouse = Warehouse(product_dict)
    warehouse.add_line_to_DB()
if type_item == 2:
    scanner = Scanner(brand, model, price, size, quantity, department, number_pages)
    product_dict = scanner.line_compilation()
    warehouse = Warehouse(product_dict)
    warehouse.add_line_to_DB()
if type_item == 3:
    copier = Copier(brand, model, price, size, quantity, department, number_pages)
    product_dict = copier.line_compilation()
    warehouse = Warehouse(product_dict)
    warehouse.add_line_to_DB()
