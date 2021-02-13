#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open ("Homework5_1.txt", "a+") as f_obj:
   while True:
        input_string= input("Enter string to the file, to break enter XXX: ")
        if input_string=='XXX':
            break
        f_obj.write("\n")
        f_obj.write(input_string)

