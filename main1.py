import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import google.generativeai as genai

# Set page title and favicon
st.set_page_config(page_title="Plant Disease Detection", page_icon="🍊")

# Custom styles
st.markdown("""
<style>
.main {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
h1 {
    color: #FFFFFF;
    text-align: center;
}
h2 {
    font-family: Georgia, serif;
    color: #333333;
}
button {
    background-color: #FF5733;
    color: white;
    padding: 0.25em 0.5em;
    text-transform: uppercase;
    border-radius: 5px;
    border: none;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>Plant Disease Detection</h1>", unsafe_allow_html=True)
st.markdown("<h1> By Simple Question & Answer</h1>", unsafe_allow_html=True)
# Sidebar information
st.sidebar.markdown("<h1>4th Year Btech Project by Ayush Chatterjee, Pritam Saha, Sandipan Patra & Sk Samim Aktar</h2>",
                    unsafe_allow_html=True)



# Replace the google_api_key here
GOOGLE_API_KEY = "AIzaSyAn9qZB-o5R09MSYL_TD-hDK82fztcaHws"  # Replace with your Google API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load Gemini Pro model and get responses
geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])


def get_gemini_response(query):
    # Sends the conversation history with the added message and returns the model's response.
    instantResponse = chat.send_message(query, stream=True)
    return instantResponse


# UI components with custom fonts and colors
st.header("Ask your question about Plants Disease or Symptomps below")
st.markdown("<p style='font-family: Helvetica, sans-serif;'>", unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input for user queries with custom font and color
input_text = st.text_input("Your Question:", key="input", help="Type your question here")
st.markdown("<p style='color: #333333; font-family: Arial, sans-serif;'>", unsafe_allow_html=True)

# Button to submit query with custom color
submit_button = st.button("Get Answer", key="button", help="Click to get answer")

if submit_button and input_text:
    # Call the get_gemini_response function by passing the input_text as query and get the response
    output = get_gemini_response(input_text)

    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("Response:")

    # Display the output in the app as Bot response
    for output_chunk in output:
        st.write(output_chunk.text)
        st.session_state['chat_history'].append(("Bot", output_chunk.text))

st.subheader("Chat History:")
# Display chat history in the app with custom font and color
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
st.markdown("<p style='font-family: Helvetica, sans-serif;'>", unsafe_allow_html=True)