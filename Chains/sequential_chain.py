from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini Package
from langchain_core.prompts import ChatPromptTemplate       # Modern Prompt Template
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# First prompt: Expects {topic}, outputs a report
prompt1 = ChatPromptTemplate.from_template("Generate a short report about {topic}")

# Initializing Google's flagship multimodal model (Gemini 2.5 Flash)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Second prompt: Expects {report} (which comes automatically from the string output of chain1)
prompt2 = ChatPromptTemplate.from_template("Summarize the following report in about 2-3 lines: {report}")

# LangChain automatically feeds that string directly into prompt2's single input variable.
chain= prompt1 | model | StrOutputParser() | prompt2 | model | StrOutputParser()

# Run the sequential chain
result = chain.invoke({'topic': 'AI'})

print(result)

