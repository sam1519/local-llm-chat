import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Set the title of the web page
st.title("Local AI Assistant 🦙")

# 1. Initialize the local model
llm = ChatOllama(model="llama3.1:8b", temperature=0.7)

# 2. Set up session state to remember the chat history on the screen
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Draw the previous messages on the screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Create the chat input box at the bottom
if user_question := st.chat_input("Ask me anything..."):
    
    # Display the user's question in the UI
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate and display the AI's response
    with st.chat_message("assistant"):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI running locally."),
            ("human", "{user_input}")
        ])
        
        chain = prompt | llm
        response = chain.invoke({"user_input": user_question})
        
        st.markdown(response.content)
        
        # Save the AI's response to the history
        st.session_state.messages.append({"role": "assistant", "content": response.content})