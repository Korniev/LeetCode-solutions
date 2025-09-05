class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            print(f"{self.name} must be positive")
            return
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Cannot delete {self.name}")
        return


class Person:
    age = PositiveNumber("age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)
print(p.age)  # 30

p.age = 40
print(p.age)  # 40

p.age = -5  # ❌ ValueError

del p.age

print("----------------")


class Rectangle:
    width = PositiveNumber("width")
    height = PositiveNumber("height")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(3, 4)
print(r.area)  # 12
r.width = -5

print("----------------")


class EmailDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError(f"{self.name} must be a string with @")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete {self.name}")


class User:
    email = EmailDescriptor("email")

    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f"User(email={self.email})"

    def __repr__(self):
        return f"User({self.email!r})"


user = User("test@example.com")
print(user)

user.email = "test@example.com"
print(user.email)

user.email = "example.com"
print(user.email)

