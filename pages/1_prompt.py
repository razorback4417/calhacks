import streamlit as st
from helper import display_stl, prompt_to_cad  # Import the display_stl and prompt_to_cad functions
from chatbot import get_response

# Custom CSS for vertical line and input box color
st.markdown(
    """
    <style>
    .split {
        display: flex;
        flex-direction: row;
        gap: 20px;
    }
    .left {
        flex: 50%;
        padding: 10px;
        margin-right: 10px;
    }
    .right {
        flex: 50%;
        padding: 10px;
    }
    input[type="text"] {
        # background-color: white !important;
        # color: black;
        # padding: 8px;
        # border-radius: 5px;
        # border: 1px solid #ccc;
        # margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("CAD-Eng 🖨️")

st.markdown('<div class="split">', unsafe_allow_html=True)

# Left column
left_column, right_column = st.columns(2)


# --- FRONTEND ---

with left_column:
    st.subheader("Lets get started! 🚀")
    st.write("Here you can interact with our system and get an 3D printable file based on your input.")

    printer_options = [
        "Bambu Lab P1P",
        "Mingda Magician X2",
        "Creality Ender-5 S1",
        "Snapmaker J1",
        "Anycubic Kobra Plus",
        "Elegoo Neptune 4 Pro"
    ]
    selected_printer = st.selectbox("Select your 3D Printer:", printer_options)


    user_input = st.text_input("What do you want to print...")

    if st.button("Print!"):
        file_path = prompt_to_cad(user_input)

        if file_path:
            st.success(f"File created: {file_path}")
            displayContents = display_stl(file_path)

# Right column
with right_column:
    st.subheader("Got Questions? Ask Oski!")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    user_input = st.text_input("Hi, I am Oski! I was LITERALLY built to help you 😁", key="chat_input")

    if st.button("Ask!"):
        if not user_input:
            st.warning("Please enter a question before clicking Ask.", icon = "⚠️")
        generated_content = get_response(user_input)
        # st.success("Titles generated successfully!")
        st.text_area("", value=generated_content, height=300)

    # if st.button("Ask!", key="send_button"):
    #     if user_input:
    #         response = chat_with_the_gpt(user_input)
    #         st.session_state['chat_history'].append((user_input, response))

    # chat_history_container = st.container()
    # with chat_history_container:
    #     for user_msg, bot_msg in st.session_state['chat_history']:
    #         st.write(f"**User:** {user_msg}")
    #         st.write(f"**Oski:** {bot_msg}")

# End of the split container
st.markdown('</div>', unsafe_allow_html=True)