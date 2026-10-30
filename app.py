from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Initialize the connection to your local model
llm = ChatOllama(model="llama3.1:8b", temperature=0.7)

# Set up the prompt structure
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI running locally. Give clear and concise answers."),
    ("human", "{user_input}")
])

# Connect the prompt to the model
chain = prompt | llm

print("🤖 Local AI is ready! (Type 'quit' or 'exit' to stop)")
print("-" * 50)

# Create an infinite loop to chat with the model
while True:
    user_question = input("\nYou: ")
    
    if user_question.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break
        
    # Send the user's message to the local model
    response = chain.invoke({"user_input": user_question})
    print(f"\nAI: {response.content}")