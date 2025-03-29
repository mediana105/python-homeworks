import numpy as np


class Matrix:
    def __init__(self, data: list[list[int | float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            raise TypeError(f"Can not add {type(other).__name__} to Matrix")
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError(
                f"Matrix size mismatch: first: {self.rows}x{self.cols}, second: {other.rows}x{other.cols}"
            )
        return Matrix([
            [i + j for i, j in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ])

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Can not add {type(other).__name__} to Matrix")
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError(
                f"Matrix size mismatch: first: {self.rows}x{self.cols}, second: {other.rows}x{other.cols}"
            )
        return Matrix([
            [
                i * j for i, j in zip(row_self, row_other)
            ]
            for row_self, row_other in zip(self.data, other.data)
        ])

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Can not add {type(other).__name__} to Matrix")
        if self.cols != other.rows:
            raise ValueError(
                f"Matrix size mismatch: first: {self.rows}x{self.cols}, second: {other.rows}x{other.cols}"
            )
        other_transposed = list(zip(*other.data))
        return Matrix([
            [
                sum(i * j for i, j in zip(row_self, col_other))
                for col_other in other_transposed
            ]
            for row_self in self.data
        ])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


def generate_txt_file():
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    with open("artifacts/matrix_add.txt", "w") as f:
        f.write(str(matrix1 + matrix2))
    with open("artifacts/matrix_mul.txt", "w") as f:
        f.write(str(matrix1 * matrix2))
    with open("artifacts/matrix_matmul.txt", "w") as f:
        f.write(str(matrix1 @ matrix2))


if __name__ == "__main__":
    generate_txt_file()
