# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    def div_func(self):
        try:
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter denumenator: "))
            print(f"Division result={numerator/denominator}")
        except ZeroDivisionError as err:
            print(f"You entered denominator as zero, system description: {err}")
        except ValueError as err2:
            print(f"You entered non numeric nominator or denominator, system description: {err2}")
        except Exception as err3:
            print(f"God knows what happened, but this is wrong, system description: {err3}")
        finally:
            print("End of execution thank you very much")


div=Division()
div.div_func()
