import streamlit as st

#navigation bar -> note that app.py is the "app" page by default. We will not edit this for now.
st.selectbox(
    ["prompt"],
)

# Set the app title
st.title('CAD Text Generation App')

# Add a welcome message
st.write('Welcome')

# Create a text input
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# Display the customized message
st.write('Customized Message:', user_input)

