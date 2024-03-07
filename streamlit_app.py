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

# Chat area to display messages
chat_area = st.empty()

# User input text box
user_input = st.text_input("User Input")

# Button to submit user input
if st.button("Send"):
    # Display user input
    chat_area.text("User: " + user_input)
    
    # Generate and display bot response
    bot_response = generate_response(user_input)
    chat_area.text("Bot: " + bot_response)
