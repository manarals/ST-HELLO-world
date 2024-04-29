import streamlit as st

# Predefined questions and answers
qa_pairs = {
    "How are you?": "I'm good, thank you!",
    "What is your name?": "My name is ChatBot.",
    "How can I help you?": "You can ask me anything.",
    # Add more questions and answers as needed
}

def get_answer(question):
    for key in qa_pairs.keys():
        if question.lower() in key.lower():
            return qa_pairs[key]
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

if __name__ == "__main__":
    main()
