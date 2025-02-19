import unittest
from sparse_matrix import SparseMatrix
from matrix_operations import MatrixOperations

class TestMatrixOperations(unittest.TestCase):
    def test_add(self):
        matrix1 = SparseMatrix(num_rows=2, num_cols=2)
        matrix1.set_element(0, 0, 1)
        matrix1.set_element(1, 1, 2)

        matrix2 = SparseMatrix(num_rows=2, num_cols=2)
        matrix2.set_element(0, 0, 3)
        matrix2.set_element(1, 1, 4)

        result = MatrixOperations.add(matrix1, matrix2)
        self.assertEqual(result.get_element(0, 0), 4)
        self.assertEqual(result.get_element(1, 1), 6)

if __name__ == "__main__":
    unittest.main()
