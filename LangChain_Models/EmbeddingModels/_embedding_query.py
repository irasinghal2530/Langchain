import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

text = "India is a beautiful country."

vector = embeddings.embed_query(text)

print(type(vector))
print(len(vector))
print(vector[:10])  # First 10 dimensions