import sys


class PointDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointDict(x={self.x}, y={self.y})"


class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointSlots(x={self.x!r}, y={self.y!r})"


N = 1_000_000
pd = [PointDict(i, i+1) for i in range(N)]
ps = [PointSlots(i, i+1) for i in range(N)]

dict_size = sum(sys.getsizeof(p) + sys.getsizeof(p.__dict__) for p in pd)
slots_size = sum(sys.getsizeof(p) for p in ps)
print(repr(dict_size))
print(repr(slots_size))
print(f"Total for PointDict ({N:,}): {dict_size/1e6:.2f} MB")
print(f"Total for PointSlots ({N:,}): {slots_size/1e6:.2f} MB")
