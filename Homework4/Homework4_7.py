#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом:
# for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только
# первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n): # function obtains number of iterations and outputs factorial number one by one using yield
    factorial=1 # factorial will always equal at least one, if user enters zero loop will not happen
    for i in range(1,n+1):
        factorial=i*factorial
        yield factorial

n=int(input("Enter number to factor: "))
output=fact(n)
i=0 # counter
for el in output:
    i+=1
    print(f"iteration {i}:{el}")

