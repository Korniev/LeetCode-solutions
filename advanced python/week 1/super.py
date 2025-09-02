class SmartList(list):
    def append(self, item):
        print(f"Додаю {item}")
        super().append(item)

    def extend(self, iterable):
        print(f"Розширюю списком {list(iterable)}")
        super().extend(iterable)

    def remove(self, item):
        print(f"Видаляю {item}")
        super().remove(item)

    def __repr__(self):
        return f"SmartList({super().__repr__()})"


sl = SmartList([1, 2])
sl.append(3)
# Додаю 3
sl.extend([4, 5])
# Розширюю списком [4, 5]
sl.remove(2)
# Видаляю 2
print(sl)
# SmartList([1, 3, 4, 5])