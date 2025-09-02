from functools import total_ordering


@total_ordering
class Vector1D:
    def __init__(self, x):
        self.x = x

    def __bool__(self):
        return bool(self.x)

    def __eq__(self, other):
        if isinstance(other, Vector1D):
            return self.x == other.x
        if isinstance(other, (int, float)):
            return self.x == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector1D):
            return self.x < other.x
        if isinstance(other, (int, float)):
            return self.x < other
        return NotImplemented

    def __hash__(self):
        return hash(self.x)

    def __repr__(self):
        return f"Vector1D({self.x})"


v1 = Vector1D(5)
v2 = Vector1D(5)
v3 = Vector1D(10)

# dict
d = {v1: "hello"}
print(d[v2])

# set
s = {v1, v2, v3}
print(s)
