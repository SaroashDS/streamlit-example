import streamlit as st

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
    st.write("<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
    st.table(data[columns])

# Main Streamlit app
def main():
    st.title("Google Dialogflow Interface")
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
        st.write("Chatbot will be displayed here")

if __name__ == "__main__":
    main()
