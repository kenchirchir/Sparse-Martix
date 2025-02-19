import unittest
from sparse_matrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def test_load_from_file(self):
        matrix = SparseMatrix("dsa/sparse_matrix/sample_inputs/matrix1.txt")
        self.assertEqual(matrix.get_element(0, 381), -694)
        self.assertEqual(matrix.get_element(0, 128), -838)

    def test_set_element(self):
        matrix = SparseMatrix(num_rows=3, num_cols=3)
        matrix.set_element(1, 1, 5)
        self.assertEqual(matrix.get_element(1, 1), 5)

if __name__ == "__main__":
    unittest.main()
