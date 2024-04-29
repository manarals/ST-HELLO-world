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
    if user_input.lower() in ["yes", "hi", "please", "chat", "hello", "salam", "bot"]:
        st.write("Hello there!\nPlease choose a number so I can assist you...")
        st.write("1. What is MoqlatAI")
        st.write("2. What is Diabetic Retinopathy")
        st.write("3. What are the stages of Diabetic Retinopathy")
    elif user_input == "1":
        st.write("MoqlatAI is an AI-powered website that utilizes advanced deep learning algorithms to detect Diabetic Retinopathy.\n\n **Mission:** \n"
          "Our mission is to contribute to Saudi Arabia's Vision 2030 by integrating technology into the healthcare sector, driving societal transformational success,"
          "that allows you to flex and grow your business with the best solutions.\n\n **Vision:** \n Our vision is to empower healthcare professionals with advanced disease detection tools, ensuring exceptional patient care"
          "and well-being.")
    elif user_input == "2":
        st.write("**Diabetic retinopathy** is a diabetes complication that affects the eyes. It's caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina)."
          " In some cases, diabetic retinopathy can progress to a severe stage where it causes vision loss or even blindness.\n Regular eye exams and managing blood sugar levels are essential for preventing and managing diabetic retinopathy.")
        
    elif user_input == "3":
        st.write("1- **Normal Retina:** In a healthy retina, the blood vessels are typically well-formed and function properly to supply oxygen and nutrients to the retinal tissue. There are no signs of swelling, leakage, or abnormal growth of blood vessels. The macula, the central part of the retina responsible for central vision, is flat and thin, allowing for clear vision.\n"
          "2- **Mild Nonproliferative Retinopathy:** The first stage of diabetic retinopathy involves the development of small areas of swelling in the retinal blood vessels, known as microaneurysms. These microaneurysms may cause minor leakage of fluid into the retina, leading to mild retinal swelling.\n"
          "3- **Moderate Nonproliferative Retinopathy:** As the disease progresses, more blood vessels may become blocked, resulting in areas of the retina being deprived of oxygen (ischemia). This stage is characterized by a greater extent of retinal damage compared to mild nonproliferative retinopathy.\n"
          "4- **Severe Nonproliferative Retinopathy:** In this stage, a significant number of retinal blood vessels are blocked, leading to widespread ischemia in the retina. The lack of oxygen triggers the growth of new, abnormal blood vessels (neovascularization), which marks the transition to the proliferative stage.\n"
          "5- **Proliferative Retinopathy:** This advanced stage is characterized by the growth of abnormal blood vessels into the vitreous, which is the gel-like substance filling the center of the eye. These fragile blood vessels are prone to bleeding, causing vitreous hemorrhage and potentially leading to sudden vision loss.")
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
