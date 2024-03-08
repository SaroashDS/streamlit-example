import streamlit as st

# Sample dictionary for bot responses (you can replace this with your populated dictionary)
bot_responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you?": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!"
}

# Function to generate bot responses
def generate_response(user_input):
    user_input = user_input.lower()
    if user_input in bot_responses:
        return bot_responses[user_input]
    else:
        return "Sorry, I didn't understand that."

# Streamlit app layout
st.title("Chatbot Interface")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat area to display messages
chat_area = st.empty()

# User input text box
user_input = st.text_input("User Input")

# Button to submit user input
if st.button("Send"):
    # Display user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate and display bot response
    bot_response = generate_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Display messages
num_messages = len(st.session_state.messages)
if num_messages > 0:
    num_messages_displayed = min(num_messages, 4)
    for i in range(num_messages - num_messages_displayed, num_messages):
        role = st.session_state.messages[i]["role"]
        content = st.session_state.messages[i]["content"]
        if role == "user":
            chat_area.text("User: " + content)
        else:
            chat_area.text("Bot: " + content)

    if num_messages > 4:
        st.slider("Scroll to view older messages", 0, num_messages - 4, value=num_messages - 4)
