import streamlit as st

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
        # Display entities table here

    elif page == "Intents":
        st.subheader("Intents")
        # Display intents table here

    elif page == "Fulfillments":
        st.subheader("Fulfillments")
        # Display fulfillments table here

    else:
        st.subheader("Chatbot")
        # Embed the Dialogflow chatbot iframe
        st.markdown(
            """
            <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/64e14a52-901d-4cb4-b277-0193ed8cb812"></iframe>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
