import streamlit as st
from streamlit_option_menu import option_menu

def home():
    import home
    home.main()

def prompt():
    import prompt
    prompt.main()

# Streamlit app layout
st.set_page_config(page_title="CAD-Eng", page_icon="🖨️", layout="wide")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "CAD-Eng 🖨️"],
        icons=["house", "tools"],
        menu_icon="cast",
        default_index=0,  # Set Home as the default
    )

# Set query parameters based on selection
if selected == "Home":
    st.experimental_set_query_params(page="home")
elif selected == "CAD-Eng 🖨️":
    st.experimental_set_query_params(page="prompt")

# Get the query parameter to decide which page to show
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]  # Default to Home

if page == "home":
    home()
elif page == "prompt":
    prompt()
