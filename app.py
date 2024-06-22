import streamlit as st
from typing import Any, List, Optional, Tuple, Union


# --- BACKEND ---
from kittycad.client import Client
from kittycad.api.ai import create_text_to_cad
from kittycad.models import Error, TextToCad
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody


def example_create_text_to_cad(user_prompt: str):
    # Create our client.
    print("here2")
    client = Client(token="0fa1b36e-cf55-4b47-8649-f779d5ac87e4")
    print("here3")

    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.STL,
        body=TextToCadCreateBody(
            prompt=user_prompt,  # Use the actual user input
        ),
    )

    if isinstance(result, Error):
        # Handle error case
        print(f"Error: {result.detail}")
    elif result is None:
        # Handle case where result is None
        print("No result returned.")
    else:
        # Handle success case
        print(f"Success: CAD file created with ID {result.id}")
        print(f"Success: CAD file created with outputs {result.outputs}")

# --- FRONTEND ---
st.title('Prompt to CAD File')
user_input = st.text_input('What do you want to 3D Print?')

if st.button('Create CAD File'):
    # Call the function and capture the result
    result = example_create_text_to_cad(user_input)