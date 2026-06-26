'''
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "LBW"
})

print(prompt)
'''

### running it with gemini 

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "LBW"
})

result = model.invoke(prompt)

print(result.content)