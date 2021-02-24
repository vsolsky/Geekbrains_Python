#Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                        Физика:   30(л)   —   10(лаб)
#                                        Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lectures_amount=0
dictionary_schedule={}
with open("Homework5_6.txt", "r") as f_obj:
    try:
        for line in f_obj:
            key, unparsed_line = line.split(':')
            for word in unparsed_line.split():
                if word.isdigit():
                    lectures_amount+=int(word)
            dictionary_schedule[key]=lectures_amount
            lectures_amount=0
        print(dictionary_schedule)
    except:
        exit (2)