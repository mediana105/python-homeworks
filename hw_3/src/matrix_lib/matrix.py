class HashMixin:
    def __hash__(self):
        """The simplest function that sums all elements in matrix to create more collisions"""
        return sum(sum(row) for row in self.matrix)


class Matrix(HashMixin):
    # Dictionary: stores the product matrix for two matrix hashes
    _cache = {}

    def __init__(self, matrix: list[list[int | float]]):
        self._validate_matrix(matrix)
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.matrix == other.matrix

    def __hash__(self):
        return super().__hash__()

    @staticmethod
    def _validate_matrix(matrix: list[list[int | float]]) -> None:
        """Checks the correctness of the input matrix"""
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise TypeError("Matrix must be represented as a list of lists")

        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same dimension")

        if not all(isinstance(item, (int, float)) for row in matrix for item in row):
            raise TypeError("All matrix elements must be int or float")

    def _validate_arithmetic_operation(self, other, operation: str):
        """Checks the correctness of the + and * operations"""
        if not isinstance(other, Matrix):
            raise TypeError(f"Operation {operation} cannot be applied for {type(other).__name__} with Matrix")
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError(
                f"Matrix size mismatch for {operation}:"
                f"  first matrix: {self.rows}x{self.cols}"
                f"  second matrix: {other.rows}x{other.cols}"
            )

    def _validate_matmul(self, other):
        """Checks the correctness of the @ operation"""
        if self.cols != other.rows:
            raise ValueError(
                f"Matrix size mismatch for matmul:"
                f"  first matrix: {self.rows}x{self.cols}"
                f"  second matrix: {other.rows}x{other.cols}"
            )

    def __add__(self, other: 'Matrix') -> 'Matrix':
        self._validate_arithmetic_operation(other, "+")
        return Matrix([
            [i + j for i, j in zip(row_self, row_other)]
            for row_self, row_other in zip(self.matrix, other.matrix)
        ])

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        self._validate_arithmetic_operation(other, "*")
        return Matrix([
            [
                i * j for i, j in zip(row_self, row_other)
            ]
            for row_self, row_other in zip(self.matrix, other.matrix)
        ])

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError(f"Operation @ cannot be applied for {type(other).__name__} with Matrix")
        self._validate_matmul(other)
        key = hash(self), hash(other)
        if key not in Matrix._cache:
            other_transposed = list(zip(*other.matrix))
            matmul = Matrix([
                [
                    sum(i * j for i, j in zip(row_self, col_other))
                    for col_other in other_transposed
                ]
                for row_self in self.matrix
            ])
            Matrix._cache[key] = matmul
        return Matrix._cache[key]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
