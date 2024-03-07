import streamlit as st
import pandas as pd

# Sample data for entities, intents, and fulfillments
sample_entities = [
    {"name": "Entity1", "type": "Entity Type1"},
    {"name": "Entity2", "type": "Entity Type2"},
    {"name": "Entity3", "type": "Entity Type3"}
]

sample_intents = [
    {"name": "Intent1", "action": "Action1"},
    {"name": "Intent2", "action": "Action2"},
    {"name": "Intent3", "action": "Action3"}
]

sample_fulfillments = [
    {"name": "Fulfillment1", "type": "Type1"},
    {"name": "Fulfillment2", "type": "Type2"},
    {"name": "Fulfillment3", "type": "Type3"}
]

def display_table(data, columns):
    df = pd.DataFrame(data)
    st.table(df[columns])

def main():
    # Custom CSS for ChatGPT-inspired design
    st.markdown(
        """
        <style>
            /* ChatGPT-inspired design */
            body {
                font-family: Arial, sans-serif;
                background-color: #f3f6f8;
            }
            .stApp {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
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
            .sidebar .sidebar-content {
                background-color: #2196F3;
            }
            .sidebar .sidebar-content .block-container {
                color: white;
            }
            .stRadio div div {
                color: white;
            }
            .stRadio input:checked + label {
                background-color: #4CAF50;
            }
            .stRadio input:checked + label:after {
                background-color: white;
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
    page = st.sidebar.button(
        "Navigation",
        ["Entities", "Intents", "Fulfillments", "Chatbot"],
        index=3  # Chatbot is default page
    )

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
        # Embed Dialogflow bot iframe
        st.markdown(
            """
            <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/64e14a52-901d-4cb4-b277-0193ed8cb812"></iframe>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
