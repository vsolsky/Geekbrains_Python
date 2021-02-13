#Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.
#Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

import itertools
n = int(input("Enter number to start generation: "))# request user to enter first number
for el in itertools.count(n,1):
    print(el)
    if el>10:
        break

start_list=['one', 'two','three', 'four','five'] # fixed list
i=0 # counter to break cycle
for el in itertools.cycle(start_list):
     print(el)
     i+=1
     if i>10:
         break #breaks after 10 elements

