# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

russ_dict = {'1': "odin", '2': "dva", '3': "tri", '4': "chetyre"}

transl_list = []
with open("Homework5_4_Input.txt", "r") as f_obj:
    for line in f_obj:
        line_split = line.strip().split(' - ')
        transl_list = [russ_dict[line_split[1]], line_split[1]]
        with open("Homework5_4_Output.txt", "a+") as f_obj_output:
            # f_obj_output.write(transl_list)
            #f_obj_output.writelines(transl_list)
            print(f"{transl_list}\n", file=f_obj_output)
        # if line_split[1]=='1':
        #     line_split[0]="Один"
        print(line_split)
        print(transl_list)
print(russ_dict)
