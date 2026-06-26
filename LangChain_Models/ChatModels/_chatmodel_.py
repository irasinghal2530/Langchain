# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model = "gpt-4")
# result=model.invoke("What is the capital of India")
# print(result.content)

###use free tier models from gemini

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

result = model.invoke("What is the capital of India")

print(result.content)