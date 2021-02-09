# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""Function that divides one number by another, with denominator check"""


def my_div(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except:
        print("You entered zero into denominator")


a = int(input("enter numerator:"))
b = int(input("enter denomenator:"))
print(f"Division result: {my_div(a, b)}")
