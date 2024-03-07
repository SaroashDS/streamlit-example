import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Entities", "Intents", "Fulfillments"])

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.write(msg["role"], ": ", msg["content"])

if page == "Entities":
    st.session_state.messages.append({"role": "user", "content": "Entities page"})
    st.write("user", ": ", "Entities page")
    # Logic to navigate to entities page

elif page == "Intents":
    st.session_state.messages.append({"role": "user", "content": "Intents page"})
    st.write("user", ": ", "Intents page")
    # Logic to navigate to intents page

elif page == "Fulfillments":
    st.session_state.messages.append({"role": "user", "content": "Fulfillments page"})
    st.write("user", ": ", "Fulfillments page")
    # Logic to navigate to fulfillments page

else:
    if st.button("Send"):
        prompt = st.text_input("Your message")
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.write("user", ": ", prompt)
            # Logic for bot response
