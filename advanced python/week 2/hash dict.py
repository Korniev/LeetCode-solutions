class Key:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        print(f"hash({self.value}) -> {self.value % 10}")
        return self.value % 10   # make hash

    def __eq__(self, other):
        print(f"__eq__({self.value}, {other.value})")
        return self.value == other.value

    def __repr__(self):
        return f"Key({self.value})"


d = {}
k1 = Key(10)
k2 = Key(20)
k3 = Key(30)

d[k1] = "a"
d[k2] = "b"
print(d)

print(d[k1])
print(d[k3])  # k3 has same hash as k2 but different value
