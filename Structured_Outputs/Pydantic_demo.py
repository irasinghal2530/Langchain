### Pydantic demo
'''Pydantic is a data validation and data parsing library for python. It ensures that the data you work with is correct, structured and type-safe.'''

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

person1: Person = Person(
    name="John",
    age=30,
    city="New York"
)
print(person1)
print(type(person1))

# # No runtime validation in TypedDict
# person2: Person = {
#     "name": "Jane",
#     "age": "25",   # Should be int, but Python allows it at runtime
#     "city": "Los Angeles"
# }
# print(person2)

