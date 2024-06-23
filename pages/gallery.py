import streamlit as st
import os
from helper import display_stl  # Import the display_stl function

from streamlit_option_menu import option_menu

def main():
    st.title('Gallery of Creations')

    # Search bar for prompts
    search_query = st.text_input('Search by prompt')

    # Check if the prompts file exists
    if os.path.exists("generatedFiles/prompts.txt"):
        with open("generatedFiles/prompts.txt", "r") as prompt_file:
            lines = prompt_file.readlines()

        # Filter lines based on search query
        if search_query:
            lines = [line for line in lines if search_query.lower() in line.lower()]

        if lines:
            for line in lines:
                file_path, prompt = line.strip().split(",", 1)
                st.subheader(f"Prompt: {prompt}")
                st.text(f"File: {file_path}")
                display_stl(file_path, scale=0.5)  # Display the STL file scaled down
                st.download_button(
                    label="Download STL",
                    data=open(file_path, "rb").read(),
                    file_name=os.path.basename(file_path),
                    mime="application/octet-stream"
                )
        else:
            st.write("No creations found matching the search query.")
    else:
        st.write("No creations found.")

if __name__ == "__main__":
    main()