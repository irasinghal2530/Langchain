from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel 

load_dotenv()

# Using Gemini models
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt1 = ChatPromptTemplate.from_template("Write a short poem about {topic}")
prompt2 = ChatPromptTemplate.from_template("Write a short story about {topic}")

chain1 = prompt1 | model1 | StrOutputParser()
chain2 = prompt2 | model2 | StrOutputParser()

#Use RunnableParallel with named keys for easy access
parallel_chain = RunnableParallel({
    "poem": chain1,
    "story": chain2
})

# Invoke with the required dictionary
result = parallel_chain.invoke({'topic': 'AI'})

# The result is returned as a dictionary matching your keys
print("--- POEM ---")
print(result["poem"])

print("\n--- STORY ---")
print(result["story"])