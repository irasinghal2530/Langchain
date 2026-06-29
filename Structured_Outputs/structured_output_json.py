from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

schema = {
    "title": "MovieReview",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "rating": {
            "type": "integer"
        },
        "genre": {
            "type": "string"
        },
        "recommended": {
            "type": "boolean"
        }
    },
    "required": [
        "title",
        "rating",
        "genre",
        "recommended"
    ]
}

structured_model = model.with_structured_output(schema)

result = structured_model.invoke(
    "Review the movie Interstellar."
)

print(result)
print(type(result))