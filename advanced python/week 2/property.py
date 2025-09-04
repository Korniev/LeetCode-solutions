class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            print("Age cannot be negative")
            return
        self._age = age

    @age.deleter
    def age(self):
        print("Age deleted")
        self._age = None

    def __str__(self):
        return f"Person({self.name!r}, {self.age!r})"

    def __repr__(self):
        return f"Person({self.name!r}, {self.age!r})"


p = Person("Alice", 30)
print(p.name)  # Alice
print(p.age)  # 30

p.age = 40
print(p.age)  # 40

p.age = -5  # ValueError

del p.age
print(p.age)  # None
print(str(p))
print(repr(p))

print("----------------")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width < 0:
            print("Width cannot be negative")
            return
        self._width = width

    @height.setter
    def height(self, height):
        if height < 0:
            print("Height cannot be negative")
            return
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"


r = Rectangle(3, 4)
print(r.width)  # 3
print(r.height)  # 4
print(r.area)  # 12
print(r.perimeter)  # 14

r.width = 10
print(r.area)  # 40

r.height = -5

print(str(r))
print(repr(r))

