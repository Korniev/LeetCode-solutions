class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["age"])

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def __repr__(self) -> str:
        return f"User({self.name!r}, {self.age!r})"

    def __str__(self) -> str:
        status = "adult" if User.is_adult(self.age) else "minor"
        return f"User {self.name} ({self.age}, {status})"


user = User("Alice", 30)
print(user)

user2 = User.from_dict({"name": "Bob", "age": 25})
print(user2)

print(User.is_adult(17))
print(User.is_adult(18))

print(repr(user))
