import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class WriteToFileMixin:
    def write_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(str(self))


class NiceConsoleOutputMixin:
    def __str__(self):
        return '[\n ' + '\n '.join(
            '[' + ' '.join(
                f"{int(x)}" if x.is_integer() else f"{x}"
                for x in row
            ) + ']'
            for row in self.matrix
        ) + '\n]'

class GetterAndSetterMixin:
    @property
    def matrix(self) -> np.ndarray:
        return self._matrix

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @matrix.setter
    def matrix(self, value: list[list[int | float]] | np.ndarray) -> None:
        self._matrix = np.array(value, dtype=np.float64)
        if self._matrix.ndim != 2:
            raise ValueError("Matrix must have dimension 2")
        self._rows, self._cols = self._matrix.shape


class MatrixWithMixins(WriteToFileMixin, NiceConsoleOutputMixin, GetterAndSetterMixin, NDArrayOperatorsMixin):
    def __init__(self, matrix: list[list[int | float]] | np.ndarray):
        self.matrix = matrix

    def __array_ufunc__(
            self,
            ufunc,
            method,
            *inputs,
            **kwargs,
    ):
        args = [input_.matrix
                if isinstance(input_, MatrixWithMixins)
                else np.array(input_) if isinstance(input_, list)
        else input_ for input_ in inputs]
        result = getattr(ufunc, method)(*args, **kwargs)
        return MatrixWithMixins(result) if isinstance(result, np.ndarray) else result
