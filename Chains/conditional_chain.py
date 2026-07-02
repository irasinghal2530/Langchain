from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 1. Define the separate destination chains
tech_prompt = ChatPromptTemplate.from_template("You are a senior IT specialist. Fix this issue: {query}")
tech_chain = tech_prompt | model | StrOutputParser()

billing_prompt = ChatPromptTemplate.from_template("You are a billing supervisor. Handle this accounting issue: {query}")
billing_chain = billing_prompt | model | StrOutputParser()

# 2. Define a routing function to inspect the input
def route_input(inputs):
    # We ask a quick question to a model or write logic to classify the text
    query = inputs["query"].lower()
    
    if "money" in query or "invoice" in query or "charge" in query:
        return billing_chain
    else:
        return tech_chain
        
conditional_chain = RunnableLambda(route_input)

# 4. Test it out!
print("--- Test 1 (Billing Path) ---")
print(conditional_chain.invoke({"query": "Why was I charged twice for my invoice last week?"}))

print("\n--- Test 2 (Tech Path) ---")
print(conditional_chain.invoke({"query": "My computer screen went entirely black and won't turn on."}))