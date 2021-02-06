# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#    который должен принимать данные (список списков) для формирования матрицы.


class Matrix:

    def __init__(self, data_matrix):
        self.data_matrix = data_matrix

    def __add__(self, other):
        my_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.data_matrix)):
            for j in range(len(self.data_matrix[i])):
                my_matrix[i][j] = self.data_matrix[i][j] + other.data_matrix[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))

    def __str__(self):
        pass


matrix_1 = [[33, 16, 2], [15, 20, 25], [13, -5, 0]]
matrix_2 = [[0, 0, 1], [5, 0, 5], [-13, 5, 0]]

my_matrix_1 = Matrix(matrix_1)
my_matrix_2 = Matrix(matrix_2)

print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_1])))
print('\n    +\n')
print(str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_2])))
print('\n    =\n')
print(my_matrix_1 + my_matrix_2)