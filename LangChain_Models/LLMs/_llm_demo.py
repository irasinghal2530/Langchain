import os
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

llm=OpenAI(model="gpt-3.5-turbo")

response=llm.invoke("What is the capital of India?")

print(response.content)


# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash"
# )

# response = llm.invoke("What is the capital of India?")

# print(response.content)