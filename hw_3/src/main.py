import numpy as np

from matrix_lib.matrix import Matrix
from matrix_lib.matrix_mixins import MatrixWithMixins


def generate_artifacts():
    np.random.seed(0)
    # task 1
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    with open("artifacts/task1/matrix_add.txt", "w") as f:
        f.write(str(matrix1 + matrix2))
    with open("artifacts/task1/matrix_mul.txt", "w") as f:
        f.write(str(matrix1 * matrix2))
    with open("artifacts/task1/matrix_matmul.txt", "w") as f:
        f.write(str(matrix1 @ matrix2))

    # task 2
    np.random.seed(0)
    matrix_mixins1 = MatrixWithMixins(np.random.randint(0, 10, (10, 10)).tolist())
    matrix_mixins2 = MatrixWithMixins(np.random.randint(0, 10, (10, 10)).tolist())
    (matrix_mixins1 + matrix_mixins2).write_to_file("artifacts/task2/matrix_add.txt")
    (matrix_mixins1 * matrix_mixins2).write_to_file("artifacts/task2/matrix_mul.txt")
    (matrix_mixins1 @ matrix_mixins2).write_to_file("artifacts/task2/matrix_matmul.txt")

    # task 3
    A = Matrix([[1, 2], [3, 4]])
    C = Matrix([[0, 0], [0, 10]])
    B = D = Matrix([[1, 0], [0, 1]])
    AB = A @ B
    CD = C @ D

    with open("artifacts/task3/AB.txt", "w") as f:
        f.write(str(A @ B))
    with open("artifacts/task3/CD.txt", "w") as f:
        f.write(str(C @ D))
    with open("artifacts/task3/hash.txt", "w") as f:
        f.write(f"Hash(AB): {hash(AB)}\nHash(CD): {hash(CD)}")


if __name__ == "__main__":
    generate_artifacts()
