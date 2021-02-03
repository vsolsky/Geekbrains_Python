# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

# my_list=["text",12,3,23.4, None]
# for a in my_list:
#     print(type(a))

# -----------------------------------------------------------------

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

# import ast
#
# my_list2 = []
#
# while True:
#     el = ast.literal_eval(input("enter the element:"))
#     my_list2.append(el)
#     choice = input("Continue entry? y/n")
#     if choice == "n":
#         break
#
# for el in range(0,len(my_list2),2):
#     my_list2[el],my_list2[el+1]= my_list2[el+1],my_list2[el]
#     print(my_list2[el],my_list2[el+1])

# -----------------------------------------------------------------

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# list_winter=[12,1,2]
# list_spring=[3,4,5]
# list_summer=[6,7,8]
# list_fall=[9,10,11]
#
# dict_seasons={1:"winter",2:"winter",3:"spring",4:"spring",5:"spring",6:"summer",7:"summer",8:"summer",9:"fall",10:"fall",11:"fall",12:"winter"}
#
# selected_month = int(input("Enter month: "))
#
# print("Using lists:")
# if selected_month in list_winter:
#     print("winter")
# elif selected_month in list_spring:
#     print("spring")
# elif selected_month in list_summer:
#     print("summer")
# elif selected_month in list_fall:
#     print("fall")
#
# print("----------")
# print("Using dictionaries")
#
# print(dict_seasons.get(selected_month))

# -----------------------------------------------------------------

#4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


