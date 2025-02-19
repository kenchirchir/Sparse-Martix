ass SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        self.rows = num_rows
        self.cols = num_cols
        self.data = {}  # Dictionary to store non-zero elements: (row, col) -> value

        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path):
        """Loads matrix from a file"""
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("rows="):
                    self.rows = int(line.split("=")[1])
                elif line.startswith("cols="):
                    self.cols = int(line.split("=")[1])
                elif line.startswith("("):
                    self._parse_matrix_line(line)
                else:
                    raise ValueError("Input file has wrong format")

    def _parse_matrix_line(self, line):
        """Parses a matrix entry"""
        try:
            line = line.strip("()")
            row, col, value = map(int, line.split(","))
            self.set_element(row, col, value)
        except Exception:
            raise ValueError("Input file has wrong format")

    def set_element(self, row, col, value):
        """Sets an element in the matrix"""
        if row >= self.rows or col >= self.cols:
            raise IndexError("Row or column index out of bounds")
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get_element(self, row, col):
        """Gets an element from the matrix"""
        if row >= self.rows or col >= self.cols:
            raise IndexError("Row or column index out of bounds")
        return self.data.get((row, col), 0)

    def save_to_file(self, file_path):
        """Saves matrix to a file"""
        with open(file_path, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (row, col), value in self.data.items():
                file.write(f"({row}, {col}, {value})\n")
