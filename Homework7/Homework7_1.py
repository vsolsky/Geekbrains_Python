#1. Реализовать класс Matrix (матрица).

class Matrix:
    def __init__(self, matr):
        self.matr=matr
    def __str__(self):
        for line in self.matr:
            print(line)
    def __add__(self, other):
        matr3=[]
        self.matr1=matr1
        other.matr2=matr2
        for i in range(len(self.matr1)): #reading each line in both matrixes
            row_matr3 = [] # raw for the result matrix, make it zero for each new row
            for b in range(len(other.matr[i])):
                el=self.matr1[i][b]+other.matr2[i][b] #summing elements in each raw/column respectively
                row_matr3.append(el)
            matr3.append(row_matr3)
        return matr3

matr1=[[1,2,3],[4,5,6],[7,8,9]]
matr2=[[10,11,12],[13,14,15],[16,17,18]]
M1=Matrix(matr1)
M2=Matrix(matr2)
matr3=M1+M2
M3=Matrix(matr3)
print(M3)
print(M1)

