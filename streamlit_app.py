import streamlit as st
import pandas as pd

def main():
    # Title and custom CSS for ChatGPT-inspired design
    st.title("Custom Abacus Chatbot Interface")
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #f3f6f8;
                font-family: 'Arial', sans-serif;
            }

            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
            }

            .stButton>button:hover {
                background-color: #45a049;
            }

            .stTextInput>div>div>input {
                border-radius: 20px;
                border: 2px solid #ddd;
                padding: 10px;
                width: calc(100% - 80px);
            }

            .stTextInput>div>div>button {
                border-radius: 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }

            .chat-container {
                background-color: white;
                border-radius: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                margin-bottom: 20px;
                max-width: 600px;
            }

            .user-message {
                background-color: #e5f0ff;
                color: black;
                border-radius: 20px;
                padding: 10px 15px;
                margin-bottom: 10px;
                max-width: 70%;
                float: right;
            }

            .bot-message {
                background-color: #f3f6f8;
                color: black;
                border-radius: 20px;
                padding: 10px 15px;
                margin-bottom: 10px;
                max-width: 70%;
                float: left;
            }

            .subheader {
                font-size: 24px;
                font-weight: bold;
                color: #4CAF50;
                margin-top: 20px;
                margin-bottom: 10px;
            }

            .table-container {
                background-color: white;
                border-radius: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                margin-bottom: 20px;
            }

            table {
                width: 100%;
                border-collapse: collapse;
            }

            th, td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }

            th {
                background-color: #4CAF50;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Intents", "Entities", "Fulfillments", "Chatbot"])

    if page == "Entities":
        st.subheader("Entities")
        display_table(sample_entities, ["name", "type"])

    elif page == "Intents":
        st.subheader("Intents")
        display_table(sample_intents, ["name", "action"])

    elif page == "Fulfillments":
        st.subheader("Fulfillments")
        display_table(sample_fulfillments, ["name", "type"])

    else:
        st.subheader("Chatbot")

        # Chat container
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

        # Bot messages
        st.markdown("<div class='bot-message'>Hello! How can I assist you today?</div>", unsafe_allow_html=True)

        # User input
        user_input = st.text_input("You:", "")

        # Send button
        if st.button("Send"):
            st.markdown(f"<div class='user-message'>{user_input}</div>", unsafe_allow_html=True)
            # Here you would add the logic to process the user input and generate a bot response
            # Replace the following line with your own bot response logic
            st.markdown("<div class='bot-message'>This is a placeholder response from the bot.</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
