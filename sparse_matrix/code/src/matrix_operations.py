
m sparse_matrix import SparseMatrix

class MatrixOperations:
    @staticmethod
    def add(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(num_rows=matrix1.rows, num_cols=matrix1.cols)
        for (row, col), value in matrix1.data.items():
            result.set_element(row, col, value + matrix2.get_element(row, col))
        for (row, col), value in matrix2.data.items():
            if (row, col) not in matrix1.data:
                result.set_element(row, col, value)
        return result

    @staticmethod
    def subtract(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(num_rows=matrix1.rows, num_cols=matrix1.cols)
        for (row, col), value in matrix1.data.items():
            result.set_element(row, col, value - matrix2.get_element(row, col))
        for (row, col), value in matrix2.data.items():
            if (row, col) not in matrix1.data:
                result.set_element(row, col, -value)
        return result

    @staticmethod
    def multiply(matrix1, matrix2):
        if matrix1.cols != matrix2.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result = SparseMatrix(num_rows=matrix1.rows, num_cols=matrix2.cols)
        for (row1, col1), value1 in matrix1.data.items():
            for col2 in range(matrix2.cols):
                value2 = matrix2.get_element(col1, col2)
                if value2 != 0:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        return result
