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
st.sidebar.title("Navigation")

# Button for Entities with emoji
entities_button = st.sidebar.button("🔍 Entities")

# Button for Intents with emoji
intents_button = st.sidebar.button("💡 Intents")

# Button for Fulfillments with emoji
fulfillments_button = st.sidebar.button("✅ Fulfillments")

# Logic based on button presses
if entities_button:
    st.title("💬 Entities")
elif intents_button:
    st.title("💬 Intents")
elif fulfillments_button:
    st.title("💬 Fulfillments")
else:
    st.title("💬 Chatbot - Home")
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
