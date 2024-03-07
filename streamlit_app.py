import streamlit as st

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.write(msg["role"], ": ", msg["content"])

if st.button("Entities"):
    st.session_state.messages.append({"role": "user", "content": "Entities page"})
    st.write("user", ": ", "Entities page")
    # Logic to navigate to entities page

if st.button("Intents"):
    st.session_state.messages.append({"role": "user", "content": "Intents page"})
    st.write("user", ": ", "Intents page")
    # Logic to navigate to intents page

if st.button("Fulfillments"):
    st.session_state.messages.append({"role": "user", "content": "Fulfillments page"})
    st.write("user", ": ", "Fulfillments page")
    # Logic to navigate to fulfillments page

if st.button("Back to Home"):
    st.session_state.messages.append({"role": "user", "content": "Back to Home"})
    st.write("user", ": ", "Back to Home")
    # Logic to navigate back to home page
