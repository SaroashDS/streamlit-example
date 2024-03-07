import streamlit as st

# Sample dictionary for bot responses
bot_responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you?": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!"
}

# Streamlit app layout
st.sidebar.title("Navigation")

# Button for Entities with emoji
entities_button = st.sidebar.button("🔍 Entities")

# Button for Intents with emoji
intents_button = st.sidebar.button("💡 Intents")

# Button for Fulfillments with emoji
fulfillments_button = st.sidebar.button("✅ Fulfillments")

# Button for Home with emoji
home_button = st.sidebar.button("🏠 Home")

# Function to generate bot response
def generate_response(user_input):
    user_input = user_input.lower()
    if user_input in bot_responses:
        return bot_responses[user_input]
    else:
        return "Sorry, I didn't understand that."

# Logic based on button presses
if entities_button:
    st.title("💬 Entities")
    # Add Entity button
    if st.button("Add Entity"):
        # Logic to add entity
        pass
    # Display sample entities
    st.write("Sample Entities:")

elif intents_button:
    st.title("💬 Intents")
    # Add Intent button
    if st.button("Add Intent"):
        # Logic to add intent
        pass
    # Display sample intents
    st.write("Sample Intents:")

elif fulfillments_button:
    st.title("💬 Fulfillments")
    # Add Fulfillment button
    if st.button("Add Fulfillment"):
        # Logic to add fulfillment
        pass
    # Display sample fulfillments

elif home_button:
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
        chat_area.text("Bot: " + bot_response if bot_response else "Sorry, I didn't understand that.")
