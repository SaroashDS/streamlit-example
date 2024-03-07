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
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar navigation using buttons
    page = st.sidebar.button("Entities")

    if page:
        st.subheader("Entities")
        display_table(sample_entities, ["name", "type"])

    page = st.sidebar.button("Intents")

    if page:
        st.subheader("Intents")
        display_table(sample_intents, ["name", "action"])

    page = st.sidebar.button("Fulfillments")

    if page:
        st.subheader("Fulfillments")
        display_table(sample_fulfillments, ["name", "type"])

    page = st.sidebar.button("Chatbot")

    if page:
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
