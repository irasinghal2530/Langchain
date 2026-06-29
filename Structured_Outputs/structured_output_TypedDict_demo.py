from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Define the schema
class Review(TypedDict):
    summary: str
    sentiment: str

# Create structured output model
structured_model = model.with_structured_output(Review)

# Invoke the model
result = structured_model.invoke(
    """AI is both a boon and a bane. With all the upsides that AI has, and all the benefits that people are deriving from it, it is still creating a lot of negative impacts, and many people are misusing it to a great extent."""
)

print(result["summary"])
print(result["sentiment"])