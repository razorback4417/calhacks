import streamlit as st
import os
from helper import display_stl  # Import the display_stl function

st.title('Gallery of Creations')

# Check if the prompts file exists
if os.path.exists("generatedFiles/prompts.txt"):
    with open("generatedFiles/prompts.txt", "r") as prompt_file:
        lines = prompt_file.readlines()

    for line in lines:
        file_path, prompt = line.strip().split(",", 1)
        st.subheader(f"Prompt: {prompt}")
        st.text(f"File: {file_path}")
        display_stl(file_path)  # Display the STL file
        st.download_button(
            label="Download STL",
            data=open(file_path, "rb").read(),
            file_name=os.path.basename(file_path),
            mime="application/octet-stream"
        )
else:
    st.write("No creations found.")