# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

"""Create multiplication function my_multipl using lambda, generate list using generator, generating result using reduce() """
from functools import reduce

my_multipl = lambda a, b: a * b
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_multipl, my_list))
