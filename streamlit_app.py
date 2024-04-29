import streamlit as st

st.write("hello world")
import streamlit as st

# Predefined questions and answers
qa_pairs = {
    "1. How are you?": "I'm good, thank you!",
    "2. What is your name?": "My name is ChatBot.",
    "3. How can I help you?": "You can ask me anything.",
    # Add more questions and answers as needed
}

def get_answer(question):
    if question in qa_pairs:
        return qa_pairs[question]
    else:
        return "I'm sorry, I don't have an answer to that question."

def main():
    st.title("ChatBot")
    st.markdown("### Ask me anything!")

    # User input
    user_question = st.chat_input("Enter your question")

    # Get the answer
    answer = get_answer(user_question)

    # Display the answer to the user
    st.success(f"Answer: {answer}")

main()
