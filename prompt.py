import streamlit as st
from streamlit_option_menu import option_menu

def main():
    # Custom CSS for vertical line and input box color
    st.markdown(
        """
        <style>
        .split {
            display: flex;
            flex-direction: row;
        }
        .left {
            flex: 50%;
            padding: 10px;
        }
        .right {
            flex: 50%;
            padding: 10px;
        }
        .vl {
            border-left: 1px solid #ccc;
            height: 100%;
            position: absolute;
            left: 50%;
            margin-left: -3px;
            top: 0;
        }
        input[type="text"] {
            background-color: white !important;
            color: black;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #ccc;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("CAD-Eng 🖨️")

    st.markdown('<div class="split">', unsafe_allow_html=True)

    # Left column
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Lets get started! 🚀")
        st.write("Here you can interact with our system and get an STL file output based on your input.")

        prompt_input = st.text_input("Enter here what do you want to print...")

        if st.button("Print!"):
            stl_output = generate_stl_file(prompt_input)
            right_column.write(stl_output)

        st.subheader("Got Questions? Ask Oski!")

        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []

        user_input = st.text_input("Hi, I am Oski! I was LITERALLY built to help you 😁", key="chat_input")

        if st.button("Ask!", key="send_button"):
            if user_input:
                response = get_chatbot_response(user_input)
                st.session_state['chat_history'].append((user_input, response))

        chat_history_container = st.container()
        with chat_history_container:
            for user_msg, bot_msg in st.session_state['chat_history']:
                st.write(f"**User:** {user_msg}")
                st.write(f"**Oski:** {bot_msg}")

    # Vertical line
    st.markdown('<div class="vl"></div>', unsafe_allow_html=True)

    # Right column
    with right_column:
        st.header("Output 💡")
        if 'stl_output' in locals():
            st.write(st.session_state['stl_output'] if 'stl_output' in st.session_state else "")

    # End of the split container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
