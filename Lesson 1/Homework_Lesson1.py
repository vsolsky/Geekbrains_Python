# 1.Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# var1 = int(input("Enter number:"))
# var2 = 10
# var3 = var1 + var2
# print(f"sum of vars:{var3}")

# ----------------------------------------------------

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# seconds = int(input("Enter seconds"))
# hours = seconds // 360
# minutes = (seconds % 360) // 60
# seconds = ((seconds % 360) % 60)
# print(f"{hours}:{minutes}:{seconds}")

# ----------------------------------------------------

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# var = input("Enter number")
# var1 = var + var
# var2 = var + var + var
# var3=int(var)+int(var1)+int(var2)
# print(var3)
# ----------------------------------------------------

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# Method 1
# var=input("Enter positive number:")
# var2=max([int(d) for d in var])
# print(var2)

# Method 2
# import math
# var = int(input("Enter positive number above 0:"))
# a_lst=[]
# while var > 1:
#    a_lst.append(math.floor(var % 10))
#    var /= 10
# print(max(a_lst))

# Method 3
# import math

# var = int(input("Enter positive number above 0:"))
# b = 0
# a = 0
# while var > 1:
#    a = math.floor(var % 10)
#    if b < a:
#        b = a
#    var /= 10
# print(b)

# ----------------------------------------------------

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с
# каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с
# прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# revenue = int(input("What is the firms revenue?"))
# expenses = int(input("What is the firms expenses?"))
# num_people = int(input("What is number of people:"))
# profit_loss = revenue - expenses

# if profit_loss > 0:
#     print(f"Company profit is {profit_loss}")
#     print(f"Company margin is {round(profit_loss / revenue*100,0)}%")
#     print(f"Profit per employee {round(profit_loss / num_people,2)}")
# elif profit_loss==0:
#     print(f"Company is break even")
# else:
#     print(f"Company loss is {profit_loss}")

# ----------------------------------------------------
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# a = int(input("What is the first result a="))
# b = int(input("What is the goal b="))
# day = 0
# while a < b:
#     a *= 1.1
#     day += 1
# print(f"Sportsman needs {day} days to achieve the goal of {b} km")
