import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh as stl_mesh
import streamlit as st

def display_stl(file_path):
    # Load the STL file
    stl_mesh_data = stl_mesh.Mesh.from_file(file_path)

    # Create a new plot
    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')

    # Extract vertices and faces
    for vector in stl_mesh_data.vectors:
        axes.plot([vector[0][0], vector[1][0]], [vector[0][1], vector[1][1]], [vector[0][2], vector[1][2]], color='b')
        axes.plot([vector[1][0], vector[2][0]], [vector[1][1], vector[2][1]], [vector[1][2], vector[2][2]], color='b')
        axes.plot([vector[2][0], vector[0][0]], [vector[2][1], vector[0][1]], [vector[2][2], vector[0][2]], color='b')

    st.pyplot(figure)