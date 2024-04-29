import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def handle_user_input(user_input):
    if user_input.lower() in ["yes", "hi", "please"]:
        st.write("Please choose a number:")
        st.write("1. Orange")
        st.write("2. Apple")
        st.write("3. Banana")
    elif user_input == "1":
        st.write("You chose orange. It's a great choice!")
    elif user_input == "2":
        st.write("You chose apple. Excellent!")
    elif user_input == "3":
        st.write("You chose banana. Yummy!")
    else:
        st.write("Stay safe!")

        
st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Handle user input and display assistant response in chat message container
    with st.chat_message("assistant"):
        handle_user_input(prompt)
