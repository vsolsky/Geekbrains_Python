#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func (a,b,c):
     try:
        numbers_list=[a,b,c] # add parameters into the list, in order to sort and choose the last two numbers.
        numbers_list.sort()
        return print(f"The two biggest numbers are:{numbers_list[-1]} and {numbers_list[-2]}, the sum is {numbers_list[-1]+numbers_list[-2]}")
     except:
         print("Something went wrong, probably you entered 3 similar digits")

a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))
my_func(a,b,c)