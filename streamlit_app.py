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

# User input text box
user_input = st.text_input("User Input")

# Button to submit user input
if st.button("Send"):
    # Display user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate and display bot response
    bot_response = generate_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Chat area to display messages
chat_area = st.empty()

# Display messages
chat_content = ""
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    if role == "user":
        chat_content += f"User: {content}\n"
    else:
        chat_content += f"Bot: {content}\n"

chat_area.text(chat_content)
