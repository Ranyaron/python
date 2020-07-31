class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.matrix = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix])
        return self.matrix

        # my_matrix = []
        # for i in self.matrix:
        #     my_list = []
        #     for j in i:
        #         my_list.append(str(j))
        #     my_matrix += ['\t'.join(my_list)]
        # my_matrix = '\n'.join(my_matrix)
        # return my_matrix

    def __add__(self, other):
        self.matrix = [[sum(i) for i in zip(x, y)] for x, y in zip(self.matrix, other.matrix)]
        return Matrix(self.matrix)

        # sum_matrix = []
        # for x, y in zip(self.matrix, other.matrix):
        #     my_list = []
        #     for i in zip(x, y):
        #         my_list.append(sum(i))
        #     sum_matrix.append(my_list)
        # return Matrix(sum_matrix)


matrix_1_1 = Matrix([[1, 3], [4, 8], [7, 3]])
matrix_1_2 = Matrix([[9, 5], [7, 1], [3, 2]])
print(matrix_1_1 + matrix_1_2)
print('-' * 21)

matrix_2_1 = Matrix([[1, 3, 4], [4, 7, 8], [1, 7, 3]])
matrix_2_2 = Matrix([[3, 9, 5], [7, 6, 1], [3, 2, 8]])
print(matrix_2_1 + matrix_2_2)
print('-' * 21)

matrix_3_1 = Matrix([[1, 3, 4, 5], [2, 4, 7, 8]])
matrix_3_2 = Matrix([[3, 9, 5, 7], [7, 3, 6, 1]])
print(matrix_3_1 + matrix_3_2)
print('-' * 21)
