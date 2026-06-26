### Embedding multiple documents
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Python is a programming language.",
    "Delhi is the capital of India.",
    "LangChain is an LLM application framework."
]

vectors = embeddings.embed_documents(documents)

print(f"Number of embeddings: {len(vectors)}")
print(f"Dimensions: {len(vectors[0])}")