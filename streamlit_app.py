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

# Function to display entities, intents, and fulfillments in a table
def display_table(data, columns):
    df = pd.DataFrame(data)
    st.table(df[columns])

# Main Streamlit app
def main():
    st.title("Custom Abacus Chatbot Interface")
    st.markdown(
        """
        <style>
            .css-1qj5a3p {
                padding: 1rem 3rem;
                font-size: 1.5rem;
            }
            .css-12q4g5o {
                background-color: #2196F3 !important;
            }
            .css-ixm2db {
                animation: css-2pcclh-unfadingAnimation 1s ease-in-out;
            }
            @keyframes css-2pcclh-unfadingAnimation {
                0% {
                    opacity: 0;
                }
                100% {
                    opacity: 1;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
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
        st.markdown(
            """
            <iframe
                width="350"
                height="430"
                src="https://bot.dialogflow.com/64e14a52-901d-4cb4-b277-0193ed8cb812"
                allow="microphone; camera; geolocation"
                style="border: none;"
            ></iframe>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
