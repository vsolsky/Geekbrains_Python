#Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
num_lines=0
num_words=0
with open ("Homework5_2.txt", "r") as f_obj:
    for line in f_obj:
        num_words=len(line.split())+num_words
        num_lines+=1

print(f"Number of lines: {num_lines}, number of words: {num_words}")


