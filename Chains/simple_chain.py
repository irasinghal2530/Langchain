from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI  # Updated package for Google
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Setup modern chat prompt
prompt = ChatPromptTemplate.from_template("Write 1 interesting fact about {topic}")

# Initialize the Google Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

parser = StrOutputParser()

# The LangChain Expression Language (LCEL) chain
chain = prompt | model | parser

# Invoke the chain with a properly formatted dictionary
result = chain.invoke({'topic': 'AI'})

print(result)