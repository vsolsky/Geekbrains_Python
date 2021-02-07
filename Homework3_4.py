# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# # my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_simple_func(x, y):  # simple function that uses **
    res = x ** y
    print(f"Simple function: {x} to the power of {y} is {res}")
    return res


def my_complex_func(x, y):  # complex function that uses cycle
    a = 1
    for i in range(0, -y):
        a = a * (1 / x)  #function multiplies x on itslef y number of times.
    print(f"Complex function: {x} to the power of {y} is {a}")
    return a


x = int(input("Enter X: "))
y = int(input("Enter negative Y: "))
my_simple_func(x, y)
my_complex_func(x, y)
