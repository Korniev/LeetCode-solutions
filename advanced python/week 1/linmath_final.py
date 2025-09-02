from __future__ import annotations
from typing import Iterable, Iterator, Tuple, List, Any

from functools import total_ordering


@total_ordering
class Vector:
    __slots__ = ("_data",)

    def __init__(self, data: Iterable[float]):
        self._data: List[float] = list(data)

    def __repr__(self) -> str:
        return f"Vector({self._data!r})"

    def __str__(self) -> str:
        return f"<{', '.join(str(x) for x in self._data)}>"

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[float]:
        return iter(self._data)

    def __getitem__(self, index: int) -> float:
        return self._data[index]

    def __setitem__(self, index: int, value: float) -> None:
        self._data[index] = float(value)

    def __bool__(self) -> bool:
        return any(self._data)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector):
            return self._data == other._data
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Vector):
            return self._data < other._data
        return NotImplemented

    def _op_elementwise(self, other: Any, op) -> Vector:
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same length")
            return Vector(op(x, y) for x, y in zip(self._data, other._data))
        elif isinstance(other, (int, float)):
            return Vector(op(x, float(other)) for x in self._data)
        return NotImplemented

    def __add__(self, other: Any) -> Vector:
        return self._op_elementwise(other, lambda x, y: x + y)

    def __radd__(self, other: Any) -> Vector:
        return self.__add__(other)

    def __iadd__(self, other: Any):
        result = self + other
        if result is NotImplemented:
            return NotImplemented
        self._data = result._data
        return self

    def __sub__(self, other: Any) -> Vector:
        return self._op_elementwise(other, lambda x, y: x - y)

    def __rsub__(self, other: Any) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(float(other) - x for x in self._data)
        if isinstance(other, Vector):
            return other.__sub__(self)
        return NotImplemented

    def __isub__(self, other: Any) -> float | Vector:
        result = self - other
        if result is NotImplemented:
            return NotImplemented
        self._data = result._data
        return self

    def __mul__(self, other: Any) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(x * float(other) for x in self._data)
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same length for dot product")
            return sum(x * y for x, y in zip(self._data, other._data))
        return NotImplemented

    def __rmul__(self, other: Any) -> Vector:
        if isinstance(other, (int, float)):
            return self * other
        return NotImplemented

    def __imul__(self, other: Any) -> Vector:
        if isinstance(other, (int, float)):
            self._data = [x * float(other) for x in self._data]
            return self
        return NotImplemented

    @property
    def t(self) -> Vector:
        return self

    def copy(self) -> Vector:
        return Vector(self._data)

    @staticmethod
    def zeros(n: int) -> Vector:
        return Vector([0.0] * n)


class Matrix:
    __slots__ = ("_rows", "_shape")

    def __init__(self, rows: Iterable[Iterable[float]]):
        rows = [Vector(row) if not isinstance(row, Vector) else row.copy() for row in rows]
        if not rows:
            raise ValueError("Matrix must have at least one row")
        n = len(rows[0])
        if any(len(row) != n for row in rows):
            raise ValueError("All rows must have the same length")
        self._rows: List[Vector] = rows
        self._shape: Tuple[int, int] = len(rows), n

    def __repr__(self) -> str:
        return f"Matrix({[list(r) for r in self._rows]!r})"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self._rows)

    def __len__(self) -> int:
        return self._shape[0]

    def __iter__(self) -> Iterator[Vector]:
        return iter(self._rows)

    def __getitem__(self, index: int | Tuple[int, int]) -> float | Vector:
        if isinstance(index, tuple):
            i, j = index
            return self._rows[i][j]
        return self._rows[index]

    def __setitem__(self, index: int | Tuple[int, int], value: float | Iterable[float] | Vector) -> None:
        if isinstance(index, tuple):
            i, j = index
            self._rows[i][j] = float(value)
        else:
            row = Vector(value) if not isinstance(value, Vector) else value
            if len(row) != self._shape[1]:
                raise ValueError("Row must have the same length as the matrix")
            self._rows[index] = row

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Matrix):
            return self._shape == other._shape and all(x == y for x, y in zip(self._rows, other._rows))
        return NotImplemented

    @property
    def shape(self) -> Tuple[int, int]:
        return self._shape

    @property
    def t(self) -> Matrix:
        r, c = self._shape
        return Matrix([[self[i, j] for i in range(r)] for j in range(c)])

    def _op_elementwise(self, other: Any, op) -> Matrix:
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrix shapes must match")
            return Matrix([[op(a, b) for a, b in zip(ra, rb)] for ra, rb in zip(self, other)])
        elif isinstance(other, (int, float)):
            return Matrix([[op(a, float(other)) for a in row] for row in self])
        return NotImplemented

    def __add__(self, other: Any) -> Matrix:
        return self._op_elementwise(other, lambda x, y: x + y)

    def __radd__(self, other: Any) -> Matrix:
        return self.__add__(other)

    def __iadd__(self, other: Any) -> Matrix:
        result = self + other
        if result is NotImplemented:
            return NotImplemented
        self._rows = result._rows
        return self

    def __sub__(self, other: Any) -> Matrix:
        return self._op_elementwise(other, lambda x, y: x - y)

    def __rsub__(self, other: Any) -> Matrix:
        if isinstance(other, (int, float)):
            return Matrix([[float(other) - a for a in row] for row in self])
        if isinstance(other, Matrix):
            return other.__sub__(self)
        return NotImplemented

    def __isub__(self, other: Any) -> Matrix:
        res = self - other
        if res is NotImplemented:
            return NotImplemented
        self._rows = res._rows
        return self

    def __mul__(self, other: Any) -> "Matrix" | Vector | NotImplemented:
        # matrix @ vector / matrix @ matrix, а також scalar * matrix
        if isinstance(other, (int, float)):
            return Matrix([[a * float(other) for a in row] for row in self])

        # Matrix * Vector => Vector
        if isinstance(other, Vector):
            r, c = self.shape
            if len(other) != c:
                raise ValueError("Matrix-Vector shapes are incompatible")
            return Vector(sum(self[i, k] * other[k] for k in range(c)) for i in range(r))

        # Matrix * Matrix => Matrix
        if isinstance(other, Matrix):
            r1, c1 = self.shape
            r2, c2 = other.shape
            if c1 != r2:
                raise ValueError("Matrix shapes are incompatible for multiplication")
            return Matrix([
                [sum(self[i, k] * other[k, j] for k in range(c1)) for j in range(c2)]
                for i in range(r1)
            ])
        return NotImplemented

    def __rmul__(self, other: Any) -> "Matrix" | Vector | NotImplemented:
        if isinstance(other, (int, float)):
            return self * other
        if isinstance(other, Vector):
            r, c = self.shape
            if len(other) != r:
                raise ValueError("Vector-Matrix shapes are incompatible")
            # (1×r) * (r×c) = (1×c)
            return Vector(sum(other[i] * self[i, j] for i in range(r)) for j in range(c))
        return NotImplemented

    def __imul__(self, other: Any):
        if isinstance(other, (int, float)):
            self._rows = [[a * float(other) for a in row] for row in self._rows]  # in-place scale
            return self
        return NotImplemented

    @staticmethod
    def zeros(rows: int, cols: int) -> Matrix:
        return Matrix([[0.0] * cols for _ in range(rows)])

    @staticmethod
    def identity(n: int) -> Matrix:
        return Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])

    def copy(self) -> Matrix:
        return Matrix([list(row) for row in self._rows])


if __name__ == "__main__":
    v = Vector([1, 2, 3])
    w = Vector([10, 20, 30])
    print("v:", v, "| w:", w)
    print("v + w =", v + w)
    print("v + 5  =", v + 5)
    print("5 + v  =", 5 + v)
    print("v · w  =", v * w)  # dot product
    v += 1
    print("v += 1 ->", v)

    A = Matrix([[1, 2], [3, 4], [5, 6]])  # 3×2
    B = Matrix([[7, 8, 9], [10, 11, 12]])  # 2×3
    print("\nA:\n", A, "\nB:\n", B, sep="")
    print("A + 1:\n", A + 1, sep="")
    print("A.t:\n", A.t, sep="")
    print("A * B:\n", A * B, sep="")
    x = Vector([1, 1])
    print("A * x =", A * x)  # 3×2 * 2 -> 3
    y = Vector([1, 1, 1])
    print("y * (A*B) =", y * (A * B))  # (1×3) * (3×3) -> (1×3) → Vector
