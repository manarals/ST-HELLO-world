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

    # Chat interface
    conversation = st.text_area("Conversation", value="", height=200, key="conversation")

    # User input
    user_question = st.text_input("User Input")

    if st.button("Send"):
        # Append user's question to the conversation
        conversation += f"\nUser: {user_question}"

        # Get the answer
        answer = get_answer(user_question)

        # Append chatbot's answer to the conversation
        conversation += f"\nChatBot: {answer}"

        # Clear the user's input
        user_question = ""

    # Display the updated conversation
    st.text_area("Conversation", value=conversation, height=200, key="conversation", disabled=True)

    # Display the user input field
    st.text_input("User Input", value=user_question)

if __name__ == "__main__":
    main()
