#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
# чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

"""is_number unction converts numbers in list from str to int, if attribute is not in it is left out"""
def is_number (separated_list):
    numbers_list=[]
    a=0 #variable to convert i into int
    for i in separated_list:
        if i=="w":
            check=False
            return numbers_list, check #returns false into a function
        else:
            try:
                a=int(i)
                numbers_list.append(a)
                check = True
            except:
                pass
    return numbers_list, check

check=True
sum_numbers=0
while check==True:
    input_string= input("Enter line of numbers, space separated: ")
    separated_list=input_string.split(" ")
    numbers_list, check = is_number(separated_list)
    sum_numbers=sum_numbers+sum(numbers_list) #accumulates sum of integers
    print(sum_numbers)
