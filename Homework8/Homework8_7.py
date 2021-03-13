# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, real_number, imaginary_number):
        self.real_number=real_number
        self.imaginary_number=imaginary_number

    def __add__(self, other):
        sum_real=self.real_number+other.real_number
        sum_imaginary=self.imaginary_number+other.imaginary_number
        return f"{sum_real}+{sum_imaginary}i"
    def __mul__(complex_number1, complex_number2):
        multiplication_real=complex_number1.real_number*complex_number2.real_number+complex_number1.imaginary_number*complex_number2.real_number+complex_number1.imaginary_number*complex_number2.imaginary_number*(-1)
        multiplication_imaginary=complex_number1.real_number*complex_number2.imaginary_number
        return f"{multiplication_real}+{multiplication_imaginary}i"

    @staticmethod
    def complex_number_split(complex_number): # splits complex number into separate digits
        try:
            real_number,imaginary_number = " ".join(filter(str.isdigit, complex_number)).split()
            return int(real_number), int(imaginary_number)
        except:
            print("You entered real numbers above 9, program ends")
            exit(0)


complex_number1=input("Enter complex number 1 (format a+bi): ")
complex_number2=input("Enter complex number 2 (format a+bi): ")
real_number1,imaginary_number1=Complex_number.complex_number_split(complex_number1) #split the complex number into digits
real_number2,imaginary_number2=Complex_number.complex_number_split(complex_number2) #split the complex number into digits
complex_obj1=Complex_number(real_number1,imaginary_number1)
complex_obj2=Complex_number(real_number2,imaginary_number2)
print(f"Sum= {complex_obj1+complex_obj2}")
multipl=complex_obj1*complex_obj2
print(f"Multiplication={multipl}")





