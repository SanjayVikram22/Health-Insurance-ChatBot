# import streamlit as st
# from index import ask

# st.title("Health Insurance Chat Bot")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     response = ask(prompt)
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
from index import ask

st.title("Health Insurance Chat Bot")

# Add custom CSS for message alignment
st.markdown("""
    <style>
        .chat-container {
            display: flex;
            margin-bottom: 10px;
        }
        .user-message {
            justify-content: flex-end;
        }
        # .assistant-message {
        #     justify-content: flex-end;
        # }
        .message {
            max-width: 95%;
            padding: 10px 15px;
            border-radius: 12px;
            font-size: 16px;
            background-color: #f1f1f1;
            margin: 4px;
        }
        .user-bubble {
            background-color: white;
            color:black;
        }
        .assistant-bubble {
            background-color: white;
            color:black;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "assistant-message"
    bubble_class = "user-bubble" if message["role"] == "user" else "assistant-bubble"
    st.markdown(
        f"""
        <div class="chat-container {role_class}">
            <div class="message {bubble_class}">{message["content"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# React to user input
if prompt := st.chat_input("Ask me anything about health insurance..."):
    # Add and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(
        f"""
        <div class="chat-container user-message">
            <div class="message user-bubble">{prompt}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Generate and display assistant response
    response = ask(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    st.markdown(
        f"""
        <div class="chat-container assistant-message">
            <div class="message assistant-bubble">{response}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
