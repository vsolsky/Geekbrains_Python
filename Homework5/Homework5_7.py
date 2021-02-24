#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
positive_profit=[]
firm_dictionary={}
profit_dictionary={}
output_list=[]
with open("Homework5_7.txt", "r") as f_obj:
    for line in f_obj:
        name, revenue,costs = line.strip().split()
        revenue= int(revenue)
        costs = int(costs)
        profit=revenue-costs
        firm_dictionary[name]=profit
for el in firm_dictionary:
    if firm_dictionary[el]>0:
        positive_profit.append(firm_dictionary[el])
average_profit=sum(positive_profit)/len(positive_profit)
profit_dictionary["average profit"]=average_profit
print(profit_dictionary)
output_list=firm_dictionary,profit_dictionary
print(output_list)
with open("Homework5_7_JSON.json","w") as write_f:
    json.dump(output_list, write_f)