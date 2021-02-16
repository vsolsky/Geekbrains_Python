# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

dict1={}
with open ("Homework5_3.txt", "r") as f_obj:
    for line in f_obj:
        (name,salary)=line.split()
        if int(salary)<20000:
            dict1[name]=int(salary)

avg_salaries=dict1.values() #в задании не понятно для всех сотрудников считать среднее или только для <20k, посчитал для
                            # тех что меньше 20к

print(f"Average salary of employees with salary <20 000: {round(sum(avg_salaries)/len(avg_salaries),2)}")

print(f"Employees with salary below 20 000:\n")
for el in dict1:
    print(el, dict1[el])





