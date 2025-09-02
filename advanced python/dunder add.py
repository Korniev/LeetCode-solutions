class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector2D(self.x + other, self.y + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
        else:
            return NotImplemented
        return self

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector2D(self.x - other, self.y - other)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(other - self.x, other - self.y)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
        else:
            return NotImplemented
        return self

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            # scalar dot product
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            return NotImplemented
        return self

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __bool__(self):
        return bool(self.x or self.y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1 - v2)    # Vector2D(2, 2)
print(v1 - 1)     # Vector2D(2, 3)
print(10 - v1)    # Vector2D(7, 6)

v1 -= v2
print(v1)         # Vector2D(2, 2)

print(v1 * 2)     # Vector2D(4, 4)
print(2 * v1)     # Vector2D(4, 4)
print(v1 * v2)    # 8  (dot product)

v1 *= 3
print(v1)         # Vector2D(6, 6)
