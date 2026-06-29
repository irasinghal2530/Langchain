from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    city: str

person1: Person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person1)

# No runtime validation in TypedDict
person2: Person = {
    "name": "Jane",
    "age": "25",   # Should be int, but Python allows it at runtime
    "city": "Los Angeles"
}

print(person2)