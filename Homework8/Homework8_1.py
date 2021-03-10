#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    @staticmethod
    def date_validation(date):
        day, month, year = Date.date_parsing(date)
        if day<0 or day>31:
            print(f"Error your day is not within the range, should be within 0-31, yours is {day} ")
            exit(1)
        elif month<0 or month>12:
            print(f"Error your month is not within the range, should be within 0-12, yours is {month} ")
            exit(1)
        elif year<0 or year>2100:
            print(f"Error your year is not within the range, should be within 0-2100, yours is {year} ")
            exit(1)
        else:
            print("Your date is in correct format")
    @classmethod
    def date_parsing (cls, date):
        cls.date=date
        day, month, year= cls.date.split('-')
        day=int(day)
        month=int(month)
        year=int(year)
        return day,month, year

date="30-12-2020"
Date.date_validation(date)

