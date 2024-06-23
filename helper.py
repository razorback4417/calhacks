import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh as stl_mesh
import streamlit as st

import os
import time
from dotenv import load_dotenv
from kittycad.api.ai import create_text_to_cad, get_text_to_cad_model_for_user
from kittycad.client import ClientFromEnv
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody

load_dotenv()

def display_stl(file_path, scale=0.5):
    # Load the STL file
    stl_mesh_data = stl_mesh.Mesh.from_file(file_path)

    # Create a new plot
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    # Extract vertices and faces
    for vector in stl_mesh_data.vectors:
        axes.plot([vector[0][0] * scale, vector[1][0] * scale],
                  [vector[0][1] * scale, vector[1][1] * scale],
                  [vector[0][2] * scale, vector[1][2] * scale], color='b')
        axes.plot([vector[1][0] * scale, vector[2][0] * scale],
                  [vector[1][1] * scale, vector[2][1] * scale],
                  [vector[1][2] * scale, vector[2][2] * scale], color='b')
        axes.plot([vector[2][0] * scale, vector[0][0] * scale],
                  [vector[2][1] * scale, vector[0][1] * scale],
                  [vector[2][2] * scale, vector[0][2] * scale], color='b')

    st.pyplot(figure, use_container_width=True)  # Use container width to control the size

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