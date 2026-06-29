from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

person = Person(
    name="Jane",
    age="25",      # String
    city="Los Angeles"
)

print(person)
print(type(person.age))