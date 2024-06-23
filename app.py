import os
import streamlit as st
import time
import numpy as np
from kittycad.api.ai import create_text_to_cad, get_text_to_cad_model_for_user
from kittycad.client import ClientFromEnv
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody
from helper import display_stl  # Import the display_stl function

# Create our client.
client = ClientFromEnv()

def prompt_to_cad(user_prompt: str):
    # Create the directory if it doesn't exist
    os.makedirs("generatedFiles", exist_ok=True)

    # Extract the first word of the prompt
    first_word = user_prompt.split()[0]

    # Prompt the API to generate a 3D model from text.
    response = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.STL,
        body=TextToCadCreateBody(
            prompt=user_prompt,
        ),
    )

    # Polling to check if the task is complete
    while response.completed_at is None:
        # Wait for 5 seconds before checking again
        time.sleep(5)

        # Check the status of the task
        response = get_text_to_cad_model_for_user.sync(
            client=client,
            id=response.id,
        )

    if response.status == ApiCallStatus.FAILED:
        # Print out the error message
        print(f"Text-to-CAD failed: {response.error}")

    elif response.status == ApiCallStatus.COMPLETED:
        # Print out the names of the generated files
        print(f"Text-to-CAD completed and returned {len(response.outputs)} files:")
        for name in response.outputs:
            print(f"  * {name}")

        # Save the STL data as a uniquely named file
        final_result = response.outputs["source.stl"]
        file_path = f"generatedFiles/{first_word}-output.stl"
        with open(file_path, "w", encoding="utf-8") as output_file:
            output_file.write(final_result.get_decoded().decode("utf-8"))
            print(f"Saved output to {output_file.name}")

        # Save the prompt
        with open("generatedFiles/prompts.txt", "a") as prompt_file:
            prompt_file.write(f"{file_path},{user_prompt}\n")

        return file_path

# --- FRONTEND ---
st.title('Prompt to CAD File')
user_input = st.text_input('What do you want to 3D Print?')

if st.button('Create CAD File'):
    # Call the function and capture the result
    file_path = prompt_to_cad(user_input)

    if file_path:
        st.success(f"File created: {file_path}")
        display_stl(file_path)
else:
    # Display a default STL file if no button is pressed
    # display_stl('/Users/theol/Documents/june22/generatedFiles/box-output.stl')
    pass