import streamlit as st

with st.sidebar:
    st.text_input("Chatbot API Key", key="chatbot_api_key", type="password")
    "[Get an API key](https://example.com)"
    "[View the source code](https://example.com)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://example.com)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.write(msg["role"], ": ", msg["content"])

if prompt := st.text_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.write("user", ": ", prompt)
    # Replace this part with your bot logic
    response = "This is a response from the bot."
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write("assistant", ": ", response)
