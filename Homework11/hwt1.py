
class Matrix:
    """Class Matrix"""
    def __init__(self, matrix: [[]]):
        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])

    def __add__(self, other):
        """Method for addition two matrix in Class Matrix"""
        if isinstance(other, Matrix):
            result = []

            if (self.row == other.row and self.column == other.column):

                for i in range(self.row):
                    result_row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.column)]
                    result.append(result_row)

                return Matrix(result)

            else:
                return 'Матрицы разной размерности, нельзя складывать!'

    def __mul__(self, other):
        """Method for multiplication two matrix in Class Matrix
        The number of columns of the first matrix must match the number of rows of the second matrix"""
        if isinstance(other, Matrix):
            if self.column == other.row:
                result = []
                for i in range(self.row):
                    result_row = []
                    for j in range(self.column):
                        elem = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.column))
                        result_row.append(elem)
                    result.append(result_row)

                return Matrix(result)

            else:
                return 'Для умножения матриц количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы'
            return Matrix(result)
        return False

    def __eq__(self, other):
        """Method for equality two matrix in Class Matrix"""
        iseq = True
        if self.row == other.row and self.column == other.column:
            for i in range(self.row):
                for j in range(self.column):
                    if self.matrix[i][j] == other.matrix[i][i]:
                        continue
                    else:
                        iseq = False
                        break
        else:
            return 'Нельзя сравнивать матрицы разной размерности'

        return iseq

    def __lt__(self, other):
        """Method for equality two matrix in Class Matrix
        self less other matrix"""
        islt = True
        if self.row == other.row and self.column == other.column:
            for i in range(self.row):
                for j in range(self.column):
                    if self.matrix[i][j] < other.matrix[i][i]:
                        continue
                    else:
                        islt = False
                        break
        else:
            return 'Нельзя сравнивать матрицы разной размерности'

        return islt

    def __gt__(self, other):
        """Method for equality two matrix in Class Matrix
                self more other matrix"""
        isgt = True
        if self.row == other.row and self.column == other.column:
            for i in range(self.row):
                for j in range(self.column):
                    if self.matrix[i][j] > other.matrix[i][i]:
                        continue
                    else:
                        isgt = False
                        break
        else:
            return 'Нельзя сравнивать матрицы разной размерности'

        return isgt

    def __str__(self):
        if isinstance(self, Matrix):
            return "\n".join((str(i)) for i in self.matrix)


if __name__ == "__main__":
    mat_A = Matrix([[3, 5, 6], [5, 5, 5], [6, -1, -7]])
    mat_B = Matrix([[2, 4, 5], [0, 1, 2], [3, -2, -9]])
    mat_C = Matrix([[6, -5, -6, 3], [-1, 12, -4, 6]])
    mat_D = Matrix([[6, -5, -6], [-1, 12, -4]])
    print('Первая матрица:')
    print(mat_A)
    print('Вторая матрица: ')
    print(mat_B)
    add_matr = mat_A + mat_B
    print(add_matr)
    add_matr2 = mat_A + mat_C
    print(add_matr2)
    print(mat_A * mat_B)
    print(mat_A * mat_C)
    print(mat_A * mat_D)
    print(mat_D * mat_A)
    print(mat_A == mat_B)
    print(mat_A == mat_C)
    print(mat_A < mat_B)
    print(mat_A > mat_B)

