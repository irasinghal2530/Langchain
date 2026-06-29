from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class MovieReview(BaseModel):
    title: str
    rating: int
    genre: str
    summary: str
    recommended: bool

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

structured_model = model.with_structured_output(MovieReview)

result = structured_model.invoke("""
Review the movie Interstellar.
Return:
- movie title
- rating out of 10
- genre
- one sentence summary
- whether you recommend it
""")

print(result)
print(type(result))