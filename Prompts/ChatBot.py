from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Create the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Initialize conversation
messages = [
    SystemMessage(
        content="You are a friendly AI assistant."
    )
]

print("Chatbot")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Add user's message
    messages.append(
        HumanMessage(content=user_input)
    )

    # Get model response
    result = model.invoke(messages)

    # Add AI response to history
    messages.append(
        AIMessage(content=result.content)
    )

    print(f"AI: {result.content}\n")