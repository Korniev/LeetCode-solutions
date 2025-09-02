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

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __bool__(self):
        return bool(self.x or self.y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(v1 + v2)  # Vector2D(4, 6)
print(v1 + 10)  # Vector2D(11, 12)
print(10 + v1)  # Vector2D(11, 12)

v1 += v2
print(v1)

print(v1 == Vector2D(4, 6))
