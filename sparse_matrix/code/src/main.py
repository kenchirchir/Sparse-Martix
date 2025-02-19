mport os
from sparse_matrix import SparseMatrix
from matrix_operations import MatrixOperations

def main():
    # Get the absolute path of the current script (main.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct correct paths relative to 'code/src/'
    file1 = os.path.join(base_dir, "../../sample_inputs/matrix1.txt")
    file2 = os.path.join(base_dir, "../../sample_inputs/matrix2.txt")

    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    print("Select operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    choice = input("Enter choice: ")

    if choice == "1":
        result = MatrixOperations.add(matrix1, matrix2)
        result.save_to_file(os.path.join(base_dir, "../../sample_inputs/result_add.txt"))
    elif choice == "2":
        result = MatrixOperations.subtract(matrix1, matrix2)
        result.save_to_file(os.path.join(base_dir, "../../sample_inputs/result_subtract.txt"))
    elif choice == "3":
        result = MatrixOperations.multiply(matrix1, matrix2)
        result.save_to_file(os.path.join(base_dir, "../../sample_inputs/result_multiply.txt"))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
