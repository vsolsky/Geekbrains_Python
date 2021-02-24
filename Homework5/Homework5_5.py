# 5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

input_numbers = input("Enter numbers separated by space:")
list_numbers = []
with open("Homework5_5.txt", "r+") as f_obj:
    f_obj.truncate(0)
    f_obj.write(input_numbers)
    f_obj.seek(0)
    list_numbers = f_obj.readline().split()

test_list = list(map(int, list_numbers))
print(f"Numbers entered: {test_list} , their sum {sum(test_list)} ")