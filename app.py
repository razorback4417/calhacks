import streamlit as st

# Create a client with your token.
from typing import Any, List, Optional, Tuple, Union

from kittycad.client import Client

from kittycad.api.ai import create_text_to_cad
from kittycad.models import Error, TextToCad
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody


def example_create_text_to_cad():
    # Create our client.
    client = Client("0fa1b36e-cf55-4b47-8649-f779d5ac87e4")

    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.FBX,
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCad = result
    print(body)


#navigation
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

