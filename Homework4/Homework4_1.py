# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""function salary_calc converts string into int and then calculates employee salary based on the provided formula"""
def salary_calc(arg_list2):
    int_list = [int(el) for el in arg_list2] # converting string into int
    result = int_list[0] * int_list[1] + int_list[2]
    return result


from sys import argv

arg_list = []
arg_list2=[]

arg_list = argv
arg_list2 = arg_list[1:] # removing the name of the script from the list received from the cmd

print("Employee salary: ", salary_calc(arg_list2))
