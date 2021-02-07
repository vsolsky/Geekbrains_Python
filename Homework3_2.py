# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

"""FUnction that merges data about the user """


def my_data_merge(name, surname, year_birth, city_birth, email, phone):
    print(
        f" Data about the user: \n Name:{name} \n Surname: {surname}\n Year birth: {year_birth}\n City birth: {city_birth}\n Email: {email}\n Phone:{phone}\n")


name = input("Enter name")
surname = input("Enter surname:")
year_birth = input("Enter year birth")
city_birth = input("Enter city birth")
email = input("Enter email")
phone = input("Phone ")

my_data_merge(name, surname, year_birth, city_birth, email, phone)
