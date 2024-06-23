# Prompt to CAD File Generator

## Overview

The Prompt to CAD File Generator is a tool designed to help people who are new to Computer-Aided Design (CAD) easily create entry-level designs. By simply providing a text prompt, users can generate 3D models in STL format. Additionally, the tool features a gallery where users can view and download STL files created by others, fostering a community of shared designs and inspiration.

## Features

- **Text to CAD Conversion**: Generate 3D models from text prompts using the KittyCAD API.
- **STL File Viewer**: Visualize generated STL files directly within the application.
- **Gallery**: Browse and search through a gallery of STL files created by other users.
- **Download STL Files**: Download STL files for personal use or further modification.

## Installation

To get started with the Prompt to CAD File Generator, follow these steps:

1. **Clone the repository**:
```sh
git clone https://github.com/razorback4417/calhacks.git
cd calhacks
```

2. **Install the required dependencies**:

```sh
pip install -r requirements.txt
```

## Usage

1. **Run the Streamlit application**:
```sh
streamlit run app.py
```


2. **Navigate to the application in your web browser**:
    Streamlit will provide a local URL (usually `http://localhost:8501`) where you can access the application.

3. **Generate a CAD File**:
    - Enter a text prompt in the input field.
    - Click the "Create CAD File" button.
    - The generated STL file will be displayed and can be downloaded.

4. **View the Gallery**:
    - Click the "Go to Gallery" button to navigate to the gallery page.
    - Use the search bar to filter creations by prompts.
    - View and download STL files created by other users.

## Project Structure
```sh
my_app/
├── app.py # Main application file
├── helper.py # Helper functions (e.g., display_stl)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── pages/ # Directory for different pages
│ ├── gallery.py # Gallery page
│ ├── home.py # Home page
│ └── prompt.py # Prompt page
├── generatedFiles/ # Directory for generated STL files and prompts
├── .venv/ # Virtual environment
├── pycache/ # Compiled Python files
└── myenv/ # Additional environment files
```

## Dependencies

The project relies on the following Python packages:

- `streamlit`: For building the web application.
- `kittycad`: For interacting with the KittyCAD API.
- `numpy`: For numerical operations.
- `matplotlib`: For plotting and visualizing STL files.
- `numpy-stl`: For handling STL files.


## Acknowledgements

- **KittyCAD**: For providing the API to convert text prompts to CAD files.
- **Streamlit**: For making it easy to build and share web applications.
